.PHONY: test

test:
	@ echo "Running tests..."
	@ python3.11 -m unittest discover simplecalculator/tests/ "test_*.py"
