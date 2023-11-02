import os

current_dir = os.getcwd()


# walking up a directory using os.path.dirname
while os.path.basename(current_dir):
    current_dir = os.path.dirname(current_dir)
    print(current_dir)
