import os
from pathlib import Path


def find_rc(rc_name=".examplerc"):

    # create a search directory
    list_rc = [
        os.environ.get("/D/"),  # check env variable
        Path.cwd(),  # current working directory
        Path.home(),  # user's home directory
        Path(__file__).resolve().parent  # current file directory
    ]

    for path in list_rc:
        if path is not None:
            config_path = Path(path / rc_name)
            if config_path.exists():
                print(f"Checking {config_path}")
                return config_path.as_posix()

    print(f"File {rc_name} has not been found")


rc_file = find_rc()
if rc_file:
    print(f"rc_file found at: {rc_file}")
