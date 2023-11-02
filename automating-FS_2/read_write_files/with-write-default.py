# write to a file with the "write" method

text = """
def func(username):
    print(f"The user's username is: {username}")
    
func("Gary")
"""

with open("test.py", "w",) as opened_file:
    opened_file.write(text)
