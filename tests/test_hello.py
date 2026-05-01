from python_package_template import Config, HelloWorld


def test_default_name(capsys):
    HelloWorld()
    captured = capsys.readouterr()
    assert captured.out == "hello World\n"


def test_custom_name(capsys):
    HelloWorld(Config(name="Alice"))
    captured = capsys.readouterr()
    assert captured.out == "hello Alice\n"
