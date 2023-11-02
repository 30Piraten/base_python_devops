import os

current_dir = os.getcwd()
print(current_dir)

# split the leaf level of the path from the parent path
split_leaf = os.path.split(current_dir)

# return the parent path
dirname_parent = os.path.dirname(current_dir)

# return the leaf name
basename_leaf = os.path.basename(current_dir)

# result
print(split_leaf)
print(dirname_parent)
print(basename_leaf)
