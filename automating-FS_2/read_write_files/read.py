# Reading a file using the "read" method::


# variable to house the file name
file_path = "sample.txt"

# use the open function to get access
# and read the file: "r"
open_file = open(file_path, "r")

# call the read function on open_file
text = open_file.read()

# extras
length = len(text)
print(text)
print(length)
print(text[23])
print(open_file)
open_file.close()
