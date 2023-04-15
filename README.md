# simplecalculator
Demo app to showcase writing basic Python syntax

## Description
The task is to build a simple calculator that can take commands from stdin or from a file.

On Definition of Alphanumeric:
Alphanumeric means a combination of [a-z] and [0-9], with at least one of the former.

On Circular Dependencies:
Circular dependencies are avoided by only evaluating pending thunks for a register once. Consider the following case:
```
a add b
b add a
a add 10
print a
```
The above will be evaluated like this:
```
a = 0 + b
    b = 0 + a = 0 + 0 = 0
    => a = 0
a = a + 10 = 0 + 10 = 10
```


## How to Build
To run locally, install Python version 3.11.

Build with Docker:
```commandline
$ make build
```


## How to Test Locally
Run this command to execute unit tests:
```commandline
$ make test
```

Run test cases from text files, locally:
```commandline
$ python3.11 main.py tests/test1.txt
5
3
6
$ python3.11 main.py tests/test2.txt
11
$ python3.11 main.py tests/test3.txt
90
```

Run as interactive application:
```commandline
$ python3.11 main.py
> a add 10
> print a
10 
> quit
<program exits>
```


## How to Test Using Docker
Run test cases from text files using Docker
```commandline
$ make filename=test3.txt run
90
```

Invoke console:
```commandline
$ make console
> a add 10
> print a
10 
> quit
<program exits>
```


## Roadmap
- [X] Create a main.py file that takes input from stdin one line at a time and prints it in the terminal.
- [X] Entering "quit" (case in-sensitive) should exit.
- [X] Upgrade main.py to alternatively take a file as input, in which case each line is considered a command. The program should exit after the last line is handled. 
- [X] Add class to store operations under keys like "A add 2", the keys also being case in-sensitive. Also add an internal "evaluate" method to evaluate thunks for a certain key.
- [X] Upgrade class to take the command "print <key>", upon which operations "thunks" are evaluated.
- [X] Invalid commands should be logged to console. This includes values that causes operations to fail, such as "a divide 0". 
- [X] Upgrade class to be able to use keys as values, evaluated as needed when "print <key>" command is used.
- [X] Handle circular dependencies
- [X] Handle graceful exit for user input CTRL+C and CTRL+D
- [X] Add build with Docker
