### README: Function Summaries and Unit Testing

This README provides summaries for the functions and unit testing requirements in the project.

#### 0. Integers Addition

- Function: `add_integer(a, b=98)`
- Description: This function adds two integers.
- Conditions:
  - `a` and `b` must be integers or floats; otherwise, it raises a `TypeError` exception.
  - If `a` or `b` is a float, it is cast to an integer.
  - Returns an integer, the sum of `a` and `b`.
  - No module imports allowed.

#### 1. Divide a Matrix

- Function: `matrix_divided(matrix, div)`
- Description: This function divides all elements of a matrix by a specified divisor.
- Conditions:
  - `matrix` must be a list of lists containing integers or floats; otherwise, it raises a `TypeError` exception.
  - All rows of the matrix must have the same size.
  - `div` must be a number (integer or float); otherwise, it raises a `TypeError` exception.
  - `div` cannot be zero; otherwise, it raises a `ZeroDivisionError` exception.
  - Returns a new matrix with elements divided and rounded to 2 decimal places.
  - No module imports allowed.

#### 2. Say My Name

- Function: `say_my_name(first_name, last_name="")`
- Description: This function prints "My name is <first name> <last name>".
- Conditions:
  - `first_name` and `last_name` must be strings; otherwise, it raises a `TypeError` exception.
  - No module imports allowed.

#### 5. Max Integer - Unittest

- Description: This task involves writing unit tests for the `max_integer` function.
- Requirements:
  - Create a folder named "tests."
  - Use the `unittest` module for testing.
  - Create Python test files with the extension ".py" inside the "tests" folder.
  - Run tests using the command: `python3 -m unittest tests.6-max_integer_test`
  - Ensure that all tests can be passed by the `max_integer` function.
  - Collaboration on test cases is encouraged to cover various edge cases.

AUTHOR Nonkululeko Khanyile (Yandah)

