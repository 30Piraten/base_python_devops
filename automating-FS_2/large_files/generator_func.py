# generator function for reading large files

def line_reader(file_path):
    with open(file_path, "r") as source_file:
        for line in source_file:
            yield line


reader = line_reader("big-data.txt")

# write file to a new one
with open("big-data-corrected.txt", "w") as target_file:
    for line in reader:
        target_file.write(line)
