from pathlib import Path
import pathlib
import os


def find_rc(rc_name=".examplerc"):
    # check for Env variable
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)

    if example_dir:
        dir_path = pathlib.Path(example_dir)
        config_path = dir_path / rc_name
        print(f"Checking {config_path}")
        if config_path.exists():
            return config_path.as_posix()

    # check the current working directory
    config_path = pathlib.Path.cwd() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()

    # check user home directory
    config_path = pathlib.Path.home() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()

    # check Directory of this File
    file_path = pathlib.Path(__file__).resolve()
    parent_path = file_path.parent
    config_path = parent_path / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()

    print(f"File {rc_name} has not been found")


rc_file = find_rc()
if rc_file:
    print(f"rc file found at: {rc_file}")
