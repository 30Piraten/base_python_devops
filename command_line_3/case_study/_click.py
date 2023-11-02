import click


@click.command()
@click.option("--username", help="Please enter a username")
def get_user_input(username):
    if username.startswith("p"):
        print("Sorry we can't load your name")
    else:
        print(f"Welcome, {username}!")


result = get_user_input()
if __name__ == "__main__":
    print(result)
