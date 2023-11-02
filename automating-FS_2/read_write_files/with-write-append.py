sample = """

while True:
    print("What is your name? ")
    get_name = input()

    if len(get_name) != 0:
        print(f"Your name is: {get_name}")
        break
    else:
        print("Please enter something valid.")
"""

with open("test.py", "a") as opened_file:
    opened_file.write(sample)
