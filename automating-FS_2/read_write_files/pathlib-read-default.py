import pathlib

path = pathlib.Path("test.py")

result = path.read_text()

print(result)
