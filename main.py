"""
This is the entry point for the Simple Calculator project

It takes data from stdin and prints them out in the terminal, like this:

> quit
<program exits>

"""

QUIT_COMMAND = "quit"

if __name__ == "__main__":

    # Loop over user input until the string 'quit' is encountered
    while command := input("> ").lower():

        if command == QUIT_COMMAND:
            break

        print(command)
