import sys

# script that prints "command line" to the console
# only when run from the command line
# -- added client "--prompt"


def cli(text, role):
    send_message = f"{text} {role}"
    return send_message


if __name__ == "__main__":
    text = "Command Line"
    role = "Administrator"
    user = None  # Default value

    if "--help" in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --prompt <ROLE>"
        print(help_message)
        sys.exit(0)

    if "--prompt" in sys.argv:
        # check if there's enough argument after "--prompt"
        index_of_prompt = sys.argv.index("--prompt") + 1
        if index_of_prompt < len(sys.argv):
            user = sys.argv[index_of_prompt]
        else:
            print("Error: Missing user role after --prompt")
            sys.exit(1)

    result = cli(text, user)
    print(result)
