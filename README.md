# simplecalculator
Demo app to showcase writing Python FP-style

## Description
The task is to build a simple calculator that can take commands from stdin or from a file.

Clarifications:
1. The app can technically support numeric-only registers, but this was disallowed for readability reasons

## How to Build
There are no dependencies, except Python >= 3.8.

## How to Test
Run this command to execute unit tests:
```commandline
$ make test
```

Run test cases in assignment:
```commandline
$ python main.py test1.txt
5
3
6
$ python main.py test2.txt
11
$ python main.py test3.txt
90
```

## How to run
The app takes data from stdin and prints them out in the terminal, like this:
```commandline
$ python main.py
> quit
<program exits>
```

It can also take contents from a file as input:
``` commandline
$ python main.py input.txt
```

## Roadmap
- [X] Create a main.py file that takes input from stdin one line at a time and prints it in the terminal.
- [X] Entering "quit" (case in-sensitive) should exit.
- [X] Upgrade main.py to alternatively take a file as input, in which case each line is considered a command. The program should exit after the last line is handled. 
- [X] Add class to store operations under keys like "A add 2", the keys also being case in-sensitive. Also add an internal "evaluate" method to evaluate thunks for a certain key.
- [X] Upgrade class to take the command "print <key>", upon which operations "thunks" are evaluated.
- [X] Invalid commands should be logged to console. This includes values that causes operations to fail, such as "a divide 0". 
- [X] Upgrade class to be able to use keys as values, evaluated as needed when "print <key>" command is used.
- [ ] Detect and break loops

