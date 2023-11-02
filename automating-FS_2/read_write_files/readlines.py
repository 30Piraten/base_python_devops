# reading a file using the readlines method
from read import file_path

# get access to the file
open_files = open(file_path, "r")
texts = open_files.readlines()

print(texts)
print(texts[1])
print(len(texts))

open_files.close()
