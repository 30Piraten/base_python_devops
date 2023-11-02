# opening and reading binary files with the
# "with" statement:- pdf, jpeg, etc

file_path = "bash-scripting.pdf"

with open(file_path, "rb") as open_file:
    read_binary = open_file.read()

# print(read_binary)
print(read_binary[0])
print(read_binary[:2])
