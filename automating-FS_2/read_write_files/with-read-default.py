# using the "with" statements to
# read and open files

from read import file_path

with open(file_path, "r") as open_file:
    text = open_file.readlines()
    # text_2 = open_file.readline()

print()
print(text)
print("..................")
print(text[:1])
# print(text_2)

open_file.closed
