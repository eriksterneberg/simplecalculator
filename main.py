"""
Entry point for the Simple Calculator project
"""

import sys
import signal
from collections.abc import Generator

from simplecalculator import SimpleCalculator, Actions


shutdown = False


def graceful_exit(signum, frame):
    """
    User can signal graceful shutdown by CTRL+C
    """
    global shutdown
    shutdown = True


signal.signal(signal.SIGINT, graceful_exit)


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
                    if len(row_ := row.strip().lower()) > 0:  # ignore empty lines
                        yield row_
        except FileNotFoundError:

            # File not found, will exit loop. When 'return' is used this will exit a for loop looping over get_lines.
            print(f"file {filename} does not exist")
            return

    else:
        # Falls back to looping over user input until the string 'quit' is encountered.
        while not shutdown:
            try:
                string = input("> ").strip().lower()  # Leading and trailing whitespace is removed.
            except EOFError:
                break  # user signalled EOF using CTRL+D

            if string == Actions.QUIT:
                break

            if string == "":
                continue  # User will expect that an empty input is ignored

            yield string


if __name__ == "__main__":

    # Init a calculator that holds all parsed user input
    calculator = SimpleCalculator()

    # Lazily iterate over input, letting the SimpleCalculator class store or print (evaluate) input
    for line in get_lines():
        calculator.process(line)
