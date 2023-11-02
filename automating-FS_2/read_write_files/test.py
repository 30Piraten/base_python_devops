
def func(username):
    print(f"The user's username is: {username}")


func("Gary")


while True:
    print("What is your name? ")
    get_name = input()

    if len(get_name) != 0:
        print(f"Your name is: {get_name}")
        break
    else:
        print("Please enter something valid.")
