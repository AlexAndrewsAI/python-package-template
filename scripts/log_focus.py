#!/usr/bin/env python3
"""
Python port of log-focus.sh.

Polls the focused X11 window once per second and writes each focus change
to a single SQLite table instead of date-stamped CSV files. The `timestamp`
column is a real DATETIME (bound as a Python datetime object), so rows can
be filtered with normal comparisons, e.g.:

    SELECT * FROM window_focus WHERE timestamp >= '2026-08-21';
"""

import os
import shutil
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# Resolve the repo-root "out" directory relative to this script's location,
# so it works regardless of where the script is called from.
SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR.parent / "out"
DB_PATH = OUT_DIR / "window_focus.db"

POLL_INTERVAL_SECONDS = 1

# Refresh this session's "end" timestamp periodically, so if the process is
# force-killed (SIGKILL/power loss) the recorded downtime is off by at most
# one heartbeat interval rather than being unknown.
HEARTBEAT_INTERVAL_SECONDS = 60

# Bind datetime objects as ISO-8601 text and parse the DATETIME column back
# into datetime objects on read (PARSE_DECLTYPES below makes this automatic).
sqlite3.register_adapter(datetime, lambda dt: dt.isoformat(sep=" "))
sqlite3.register_converter("DATETIME", lambda raw: datetime.fromisoformat(raw.decode()))

SCHEMA = """
CREATE TABLE IF NOT EXISTS window_focus (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME    NOT NULL,
    window_id INTEGER,
    title     TEXT,
    wm_class  TEXT
);
CREATE INDEX IF NOT EXISTS idx_window_focus_timestamp ON window_focus (timestamp);

-- One row per run of this program. "end" is refreshed by a periodic
-- heartbeat, so a force-killed process shows at most one heartbeat interval
-- of drift; a NULL "end" only remains if the very first heartbeat never ran
-- (recovery closes it on next startup). Gaps between rows show downtime.
-- "end" is quoted because END is a reserved SQL keyword.
CREATE TABLE IF NOT EXISTS contiguous_running (
    id    INTEGER  PRIMARY KEY AUTOINCREMENT,
    start DATETIME NOT NULL,
    "end" DATETIME
);
CREATE INDEX IF NOT EXISTS idx_contiguous_running_start ON contiguous_running ("start");
"""


def close_stale_session(conn: sqlite3.Connection) -> None:
    """Close any session left open by a previous unclean exit.

    The best available end time is the most recent window_focus timestamp,
    i.e. the last moment we can prove the tracker was still alive.
    """
    row = conn.execute(
        'SELECT id, start FROM contiguous_running WHERE "end" IS NULL ORDER BY id DESC LIMIT 1'
    ).fetchone()
    if row is None:
        return

    session_id, start = row
    last_seen = conn.execute(
        "SELECT MAX(timestamp) FROM window_focus WHERE timestamp >= ?", (start,)
    ).fetchone()[0]
    end = last_seen or start

    conn.execute(
        'UPDATE contiguous_running SET "end" = ? WHERE id = ?', (end, session_id)
    )
    conn.commit()
    print(f"note: closed stale session {session_id} at {end} (previous run ended uncleanly)")


def open_db() -> sqlite3.Connection:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.executescript(SCHEMA)
    close_stale_session(conn)
    return conn


def run_command(*args: str) -> str | None:
    """Run a command, returning stripped stdout or None if it failed."""
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (subprocess.SubprocessError, OSError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def get_focused_window() -> tuple[str | None, str | None, str | None]:
    """Return (window_id, title, wm_class); all None when no focused window."""
    window_id = run_command("xdotool", "getwindowfocus")
    if not window_id or window_id == "0":
        return None, None, None

    title = run_command("xdotool", "getwindowname", window_id)

    # xprop output looks like: WM_CLASS(STRING) = "konsole", "konsole"
    raw_wm_class = run_command("xprop", "-id", window_id, "WM_CLASS")
    wm_class = raw_wm_class.split("= ", 1)[1] if raw_wm_class and "= " in raw_wm_class else ""

    return window_id, title, wm_class


def main() -> int:
    for tool in ("xdotool", "xprop"):
        if not shutil.which(tool):
            print(f"error: required tool '{tool}' not found on PATH", file=sys.stderr)
            return 1

    conn = open_db()

    # Open a new contiguous-running session for this invocation.
    now = datetime.now().replace(microsecond=0)
    cursor = conn.execute("INSERT INTO contiguous_running (start) VALUES (?)", (now,))
    conn.commit()
    session_id = cursor.lastrowid
    print(f"session {session_id} started at {now}")

    last_state = ""
    last_heartbeat = datetime.now()
    try:
        while True:
            now = datetime.now()

            # Heartbeat: keep this session's "end" fresh so a force-kill
            # (SIGKILL, power loss) still leaves an accurate end timestamp.
            if (now - last_heartbeat).total_seconds() >= HEARTBEAT_INTERVAL_SECONDS:
                conn.execute(
                    'UPDATE contiguous_running SET "end" = ? WHERE id = ?',
                    (now.replace(microsecond=0), session_id),
                )
                conn.commit()
                last_heartbeat = now

            window_id, title, wm_class = get_focused_window()

            if window_id is not None:
                state = f"{window_id}|{title}|{wm_class}"
            else:
                state = "NO_WINDOW"

            if state != last_state:
                now = datetime.now().replace(microsecond=0)

                if window_id is not None:
                    print(f"{now} {window_id} | {title} | {wm_class}")
                    conn.execute(
                        "INSERT INTO window_focus (timestamp, window_id, title, wm_class)"
                        " VALUES (?, ?, ?, ?)",
                        (now, int(window_id), title, wm_class),
                    )
                else:
                    print(f"{now} No focused window")
                    conn.execute(
                        "INSERT INTO window_focus (timestamp, window_id, title, wm_class)"
                        " VALUES (?, NULL, NULL, NULL)",
                        (now,),
                    )

                conn.commit()
                last_state = state

            time.sleep(POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        pass
    finally:
        # Close the session so gaps between sessions reflect real downtime.
        end = datetime.now().replace(microsecond=0)
        conn.execute(
            'UPDATE contiguous_running SET "end" = ? WHERE id = ?', (end, session_id)
        )
        conn.commit()
        print(f"session {session_id} ended at {end}")
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
