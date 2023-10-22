This readme provides an overview of a set of Python functions and classes related to file operations, JSON serialization, and object manipulation. Here's a summarized overview of each task:

1. **Read File**
   - Function `read_file(filename="")` reads and prints a text file (UTF8) to stdout.
   - Utilizes the `with` statement for file handling.
   - Does not handle file permission or file not found exceptions.
   - No module imports allowed.

2. **Write to a File**
   - Function `write_file(filename="", text="")` writes a string to a text file (UTF8) and returns the character count.
   - Uses the `with` statement for file handling.
   - Creates the file if it doesn't exist and overwrites its content if it does.
   - No module imports allowed.

3. **Append to a File**
   - Function `append_write(filename="", text="")` appends a string to a text file (UTF8) and returns the character count.
   - Creates the file if it doesn't exist.
   - Uses the `with` statement for file handling.
   - No module imports allowed.

4. **To JSON String**
   - Function `to_json_string(my_obj)` returns the JSON representation of an object (as a string).
   - Doesn't handle exceptions if the object can't be serialized.

5. **From JSON String to Object**
   - Function `from_json_string(my_str)` returns an object represented by a JSON string.
   - Doesn't handle exceptions if the JSON string doesn't represent an object.

6. **Save Object to File**
   - Function `save_to_json_file(my_obj, filename)` writes an object to a text file using its JSON representation.
   - Uses the `with` statement for file handling.
   - Doesn't handle exceptions if the object can't be serialized.

7. **Create Object from JSON File**
   - Function `load_from_json_file(filename)` creates an object from a JSON file.
   - Uses the `with` statement for file handling.
   - Doesn't handle exceptions if the JSON string doesn't represent an object.

8. **Load, Add, Save**
   - A script that adds all arguments to a Python list and saves them to a JSON file named "add_item.json".
   - Uses the `save_to_json_file` and `load_from_json_file` functions.
   - Doesn't manage file permissions/exceptions.

9. **Class to JSON**
   - Function `class_to_json(obj)` returns a dictionary representation of an object with simple data structures for JSON serialization.
   - Assumes all attributes of the object are serializable (list, dictionary, string, integer, boolean).
   - No module imports allowed.

10. **Student to JSON**
    - Defines a `Student` class with attributes (first_name, last_name, age).
    - Method `to_json` retrieves a dictionary representation of a `Student` instance.
    - No module imports allowed.

11. **Student to JSON with Filter**
    - Extends the `Student` class from task 10.
    - Method `to_json` can filter attributes based on a list of strings.
    - No module imports allowed.

12. **Student to Disk and Reload**
    - Extends the `Student` class from task 11.
    - Method `reload_from_json` replaces all attributes of a `Student` instance from a dictionary.
    - No module imports allowed.

These tasks cover a range of functionalities, including file handling, JSON serialization, and object manipulation, while adhering to specific constraints and requirements.
