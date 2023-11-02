import os


def walk_path(parent_path):
    for root, directories, files in os.walk(parent_path):
        print(f"Checking: {root}")

        for file_name in files:
            file_path = os.path.join(root, file_name)
            stats = os.stat(file_path)
            last_access = stats.st_atime
            size = stats.st_size

            print(f"File: {file_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tstats: {stats}")
            print(f"\tsize: {size}")


current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)

walk_path(parent_dir)
