
### Project Summary

This project consists of the implementation of classes for managing geometric shapes, including rectangles and squares, with functionality for area calculation, display, and more. The implementation strictly adheres to the principles of test-driven development and follows the PEP 8 style guidelines for Python code.

### Class Details

#### 1. Base class

- Manages the `id` attribute for all future classes
- Ensures the elimination of redundant code
- Serves as the base for all other classes

#### 2. First Rectangle

- Inherits from the `Base` class
- Includes private instance attributes for width, height, x, and y with corresponding getters and setters
- Validates attributes for data type and values

#### 3. Validate Attributes

- Validates setter methods and instantiation, excluding the `id` attribute
- Raises appropriate exceptions for invalid data types or values

#### 4. Area First

- Adds a public method `area` to calculate and return the area of the rectangle instance

#### 5. Display #0

- Introduces a public method `display` to print the rectangle instance with the character '#' to the standard output

#### 6. `__str__`

- Overrides the `__str__` method to provide a customized string representation of the rectangle

#### 7. Display #1

- Improves the `display` method to handle the position of the rectangle in the output

#### 8. Update #0

- Adds a public method `update` to assign arguments to each attribute

#### 9. Update #1

- Enhances the `update` method to support key-value arguments

#### 10. And now, the Square!

- Introduces the `Square` class, which inherits from the `Rectangle` class

#### 11. Square Size

- Adds a public getter and setter for the `size` attribute in the `Square` class

#### 12. Square Update

- Updates the `Square` class to support assignment of various attributes

#### 13. Rectangle Instance to Dictionary Representation

- Adds a method to convert a `Rectangle` instance to a dictionary representation

#### 14. Square Instance to Dictionary Representation

- Introduces a method to convert a `Square` instance to a dictionary representation

#### 15. Dictionary to JSON String

- Implements a static method to convert a list of dictionaries to a JSON string representation

#### 16. JSON String to File

- Includes a class method to save a JSON string representation of instances to a file

#### 17. JSON String to Dictionary

- Provides a static method to convert a JSON string representation to a list of dictionaries

#### 18. Dictionary to Instance

- Adds a class method to create an instance from a dictionary representation

#### 19. File to Instances

- Introduces a class method to load instances from a file in JSON format
