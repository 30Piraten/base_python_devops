import os

current_dir = os.getcwd()
directory = []

for _ in range(current_dir.count(os.sep)):
    current_dir = os.path.dirname(current_dir)
    directory.insert(0, current_dir)

for dirs in reversed(directory):
    print(dirs)
