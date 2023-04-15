# simplecalculator
Demo app to showcase writing Python FP-style

## Why this project?
Todo

## How to Build
Todo

## How to Test
Todo

## Roadmap
- [ ] Create a main.py file that takes input from stdin one line at a time and prints it in the terminal.
- [ ] Entering "quit" (case in-sensitive) should exit.
- [ ] Invalid commands should be logged to console. This includes values that causes operations to fail, such as "a divide 0".
- [ ] Add a class that takes the input and returns a command to quit if the input was "quit" (case in-sensitive).
- [ ] Upgrade class to store operations under keys like "A add 2", the keys also being case in-sensitive. Also add an internal "evaluate" method to evaluate thunks for a certain key.
- [ ] Upgrade class to take the command "print <key>", upon which operations "thunks" are evaluated.
- [ ] Upgrade class to be able to use keys as values, evaluated as needed when "print <key>" command is used.
- [ ] Upgrade main.py to alternatively take a file as input, in which case each line is considered a command. The program should exit after the last line is handled.