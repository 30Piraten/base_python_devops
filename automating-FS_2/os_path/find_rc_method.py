# case study - finding an "rc" file

import os


def find_rc(rc_name="tree.py"):

    # checking for Env variable
    var_name = "CONFIG_APP"
    if var_name in os.environ:
        var_path = os.path.join(f"${var_name}", rc_name)
        # var_path = os.path.join(os.environ[var_name], rc_name)
        config_path = os.path.expandvars(var_path)
        print(f"Checking {config_path}, 1")

        if os.path.exists(config_path):
            return config_path

    # check the current working directory
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}, 2")
    if os.path.exists(config_path):
        return config_path

    # check user home directory
    home_dir = os.path.expanduser("~/")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}, 3")
    if os.path.exists(config_path):
        return config_path

    # check directory of this file
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}, 4")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")


# case
rc_file = find_rc()
if rc_file:
    print(f"Found rc file at: {rc_file}")

# print(find_rc())
