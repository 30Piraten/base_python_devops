import pathlib

path = pathlib.Path("bash.bin")

result = path.read_bytes()

print(result)
