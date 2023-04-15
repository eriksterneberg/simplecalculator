.PHONY: build test run

# Run UT locally
test:
	@ echo "Running tests..."
	@ python3.11 -m unittest discover tests/ "test_*.py"

# Build simplecalculator using Docker
build:
	@ docker build -t simplecalculator .

# Run an ephemeral container and invoke SimpleCalculator with a filename as a command line argument
run:
	@ docker container run --rm simplecalculator python main.py $$filename

# Run an ephemeral container and invoke the SimpleCalculator console
console:
	@ docker container run --rm -it simplecalculator python main.py

