# simplecalculator
Demo app to showcase writing basic Python syntax

## Description
The task is to build a simple calculator that can take commands from stdin or from a file.

Syntax:
```
<register> <operation> <value> OR print <register>
```

All registers are alphanumeric, which means a combination of [a-z] and [0-9], with at least one of the former.

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

## Suggestions for Extensions
- Add new operations in the operations.py to extend with division, etc. A blanket catch-all try/except will catch any error raised, in which case the operation will be ignored.
- To increase accuracy of floating point arithmetic (for when division is used), the base data type float could be replaced with decimal (https://docs.python.org/3/library/decimal.html)
- To support a no-argument command like 'reset' (delete all input data stored in session), simply edit the parse method and add a handler, similar to how print is handled.