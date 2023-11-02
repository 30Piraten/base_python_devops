import os


def find_rc(rc_name="tree.py"):
    # define a list of directories
    # to search for the rc file

    list_dir = [
        # os.environ.get("EXAMPLERC_DIR"),  # check env variable
        os.getcwd(),  # check current working directory
        os.path.expanduser("~/"),  # check user's home directory
        # check source file directory
        os.path.dirname(os.path.abspath(__file__))
    ]

    for path in list_dir:
        if path is not None:
            config_path = os.path.join(path, rc_name)
            if os.path.exists(config_path):
                print(f"Checking {config_path}")
                # return the path when the file is found
                return config_path

    print(f"File {rc_name} has not been found")


# case
rc_file = find_rc()
if rc_file:
    print(f"Found rc file at: {rc_file}")
