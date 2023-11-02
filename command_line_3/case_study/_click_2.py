import click


@click.command()
@click.option("--username", help="Enter your username")
def get_user_input(username):
    if username is None:
        click.echo(
            "Username can't be empty. Please enter a username with the '--username' flag.")
    elif username.startswith("p"):
        click.echo("Sorry, we can't load your name")
    else:
        click.echo(f"Welcome {username}")


result = get_user_input()
if __name__ == "__main__":
    print(result)
