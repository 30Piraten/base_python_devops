import os

# case


def find_file(file_name="tree.py"):

    current_directory = os.getcwd()
    full_path = os.path.join(current_directory, file_name)
    print(f"Checking {full_path}")

    if os.path.exists(full_path):
        return full_path

    home_dir = os.path.expanduser("~/")
    full_path = os.path.join(home_dir, file_name)
    print(f"Checking {full_path}")

    if os.path.exists(full_path):
        return full_path

    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    full_path = os.path.join(parent_path, file_name)
    print(f"Checking {full_path}")

    if os.path.exists(full_path):
        return full_path

    print(f"File {file_name} has not been found")


# trigger
file_name = find_file()
if file_name:
    print(f"Found file at: {file_name}")
