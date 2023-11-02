import sys

# script that prints "command line" to the console
# only when run from the command line

# define a function for this


def cli(text, client):
    send_message = f"{text} {client}"
    print(send_message)


if __name__ == "__main__":
    text = "Command Line"
    client = "Administrator"
    # Here, user is None to avoid name || prompt error
    # when passed to cli function.
    # can also equate user to be "Administrator
    # as default || set as None"
    user = None  # Administrator

    if "--help" in sys.argv:
        help = f"Usage: {sys.argv[0]} --prompt <ROLE>"
        print(help)
        sys.exit(0)

    # Here I have added a logic for users
    # to be able to change the client's name
    if "--prompt" in sys.argv:
        # get the position after prompt flag
        index_of_prompt = sys.argv.index("--prompt") + 1
        if index_of_prompt < len(sys.argv):
            user = sys.argv[index_of_prompt]

    cli(text, user)
