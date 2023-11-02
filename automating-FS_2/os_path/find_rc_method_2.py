import os


def find_rc(rc_name="tree.py"):

    # Check for the environment variable "CONFIG_APP"
    var_name = "CONFIG_APP"
    # Get the value of the environment variable
    var_path = os.environ.get(var_name)

    if var_path is not None:
        config_path = os.path.join(var_path, rc_name)
        print(f"Checking {config_path}, 1")

        if os.path.exists(config_path):
            return config_path

    # Check the current working directory
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}, 2")
    if os.path.exists(config_path):
        return config_path

    # Check user home directory
    home_dir = os.path.expanduser("~")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}, 3")
    if os.path.exists(config_path):
        return config_path

    # Check the directory of this script
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}, 4")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")


# Case
rc_file = find_rc()
if rc_file:
    print(f"Found rc file at: {rc_file}")
