binary = b"""
If you are writing nontext content, such
as the contents of a .jpeg file, you are likely to corrupt it if you use either, the w or a flag. This corruption is likely as Python converts line endings to platform-specific ones when it writes text data. To write binary data, you can safely use wb or ab.
"""

file_path = "bash.bin"

with open(file_path, "wb") as b_file:  # use "wb" or "ab"
    b_file.write(binary)

print("Data has been written to the binary file, Bin")
