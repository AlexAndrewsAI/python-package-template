#!/bin/bash

export DISPLAY=:1
unset WAYLAND_DISPLAY
unset LD_PRELOAD

# Resolve the repo-root "out" directory relative to this script's location,
# so it works regardless of where the script is called from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="$SCRIPT_DIR/../out"

mkdir -p "$OUT_DIR"

CSV=""

# Point CSV at today's dated file, creating it (with header) if missing.
# Called every loop iteration so the log rolls over at midnight. On rollover,
# last_state is cleared so the current window is re-printed into the new file.
use_todays_csv() {
    local today csv
    today="$(date '+%F')"
    csv="$OUT_DIR/${today}.csv"
    if [ "$csv" != "$CSV" ]; then
        CSV="$csv"
        last_state=""
        # Create the CSV header if the file is missing or empty
        if [ ! -s "$CSV" ]; then
            printf 'timestamp,window_id,title,wm_class\n' > "$CSV"
        fi
    fi
}

csv_quote() {
    local value="$1"
    value="${value//\"/\"\"}"
    printf '"%s"' "$value"
}

last_state=""

while true; do
    use_todays_csv

    window_id="$(xdotool getwindowfocus 2>/dev/null)"

    if [ -n "$window_id" ] && [ "$window_id" != "0" ]; then
        title="$(xdotool getwindowname "$window_id" 2>/dev/null)"

        wm_class="$(
            xprop -id "$window_id" WM_CLASS 2>/dev/null |
            sed 's/.*= //'
        )"

        state="$window_id|$title|$wm_class"

        if [ "$state" != "$last_state" ]; then
            timestamp="$(date '+%F %T')"

            printf '%s %s | %s | %s\n' \
                "$timestamp" \
                "$window_id" \
                "$title" \
                "$wm_class"

            printf '%s,%s,%s,%s\n' \
                "$(csv_quote "$timestamp")" \
                "$(csv_quote "$window_id")" \
                "$(csv_quote "$title")" \
                "$(csv_quote "$wm_class")" \
                >> "$CSV"

            last_state="$state"
        fi
    else
        state="NO_WINDOW"

        if [ "$state" != "$last_state" ]; then
            timestamp="$(date '+%F %T')"

            printf '%s No focused window\n' "$timestamp"

            printf '%s,,,\n' \
                "$(csv_quote "$timestamp")" \
                >> "$CSV"

            last_state="$state"
        fi
    fi

    sleep 1
done
