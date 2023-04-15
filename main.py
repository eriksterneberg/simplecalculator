"""
Entry point for the Simple Calculator project
"""

import sys
from collections.abc import Generator

QUIT_COMMAND = "quit"


def get_lines() -> Generator[str]:
    """
    Lazily returns input lines, either from stdin or from a file. If a filename is specified but the file does not exist,
    the program will print an error and exit.

    :return: Generator[str], a Python generator with strings as the type
    """
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        # Take lines from input file; read lines one at a time to decrease memory usage
        try:
            with open(filename) as f:
                for row in f:
                    yield row.strip().lower()
        except FileNotFoundError:

            # File not found, will exit loop. When 'return' is used this will exit a for loop looping over get_lines.
            print(f"file {filename} does not exist")
            return

    else:
        # Falls back to looping over user input until the string 'quit' is encountered
        while string := input("> "):
            if string == QUIT_COMMAND:
                break
            yield string.lower()


if __name__ == "__main__":
    for line in get_lines():
        print(line)
