This readme contains information about various Python classes and functions that need to be implemented. Here's a summarized overview of each task:

1. **MyList (Class)**
   - Inherits from `list`.
   - Public method `print_sorted` sorts and prints the list in ascending order.
   - Assumes all list elements are integers.
   - No module imports allowed.

2. **is_same_class (Function)**
   - Returns `True` if the object is exactly an instance of the specified class; otherwise, `False`.
   - No module imports allowed.

3. **is_kind_of_class (Function)**
   - Returns `True` if the object is an instance of or inherits from the specified class; otherwise, `False`.
   - Handles direct and indirect inheritance.
   - No module imports allowed.

4. **inherits_from (Function)**
   - Returns `True` if the object is an instance of a class that inherits directly or indirectly from the specified class; otherwise, `False`.
   - No module imports allowed.

5. **BaseGeometry (Class)**
   - An empty class with no module imports allowed.

6. **BaseGeometry (Class, Improved)**
   - Inherits from `BaseGeometry`.
   - Public method `area` raises an Exception with the message "area() is not implemented".
   - No module imports allowed.

7. **BaseGeometry (Class, Integer Validator)**
   - Inherits from `BaseGeometry`.
   - Public method `area` raises an Exception with the message "area() is not implemented".
   - Public method `integer_validator` validates an integer value.
   - Raises TypeError if the value is not an integer and ValueError if it's less than or equal to 0.
   - No module imports allowed.

8. **Rectangle (Class)**
   - Inherits from `BaseGeometry`.
   - Constructor `__init__` with private width and height.
   - Width and height must be positive integers, validated by `integer_validator`.
   - No getters or setters.

9. **Rectangle (Class, Full)**
   - Inherits from `BaseGeometry`.
   - Constructor `__init__` with private width and height.
   - Width and height must be positive integers, validated by `integer_validator`.
   - Implements the `area()` method.
   - `print()` and `str()` methods return "[Rectangle] <width>/<height>".

10. **Square (Class #1)**
    - Inherits from `Rectangle`.
    - Constructor `__init__` with private size.
    - Size must be a positive integer, validated by `integer_validator`.
    - Implements the `area()` method.

11. **Square (Class #2)**
    - Inherits from `Rectangle`.
    - Constructor `__init__` with private size.
    - Size must be a positive integer, validated by `integer_validator`.
    - Implements the `area()` method.
    - `print()` and `str()` methods return "[Square] <width>/<height>".

Each task has specific requirements and constraints, and module imports are not allowed for any of them.
