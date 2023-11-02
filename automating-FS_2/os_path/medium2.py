
import os


def find_file(file_name="tree.py"):
    list_dir = [
        os.getcwd(),
        os.path.expanduser("~/"),
        os.path.dirname(os.path.abspath(__file__))
    ]

    for path in list_dir:
        if path is not None:
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                print(f"Checking {file_path}")
                return file_path

    print(f"File {file_name} has not been found")


# case
file_name = find_file()
if file_name:
    print(f"Found file at: {file_name}")
