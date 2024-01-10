
# Project Title
Python - Object-relational mapping

A collection of Python scripts for interacting with MySQL databases and performing Object-Relational Mapping (ORM) using SQLAlchemy.

## Tasks

### 0. Get all states

**Description:** This script lists all states from the database `hbtn_0e_0_usa`.

**Usage:**
```bash
python get_all_states.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- MySQLdb module (import MySQLdb)
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `states.id`

### 1. Filter states

**Description:** This script lists all states with names starting with 'N' (uppercase) from the database `hbtn_0e_0_usa`.

**Usage:**
```bash
python filter_states.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- MySQLdb module (import MySQLdb)
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `states.id`

### 2. Filter states by user input

**Description:** This script takes an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where the name matches the argument.

**Usage:**
```bash
python filter_states_user_input.py <mysql_username> <mysql_password> <database_name> <state_name>
```

**Requirements:**
- MySQLdb module (import MySQLdb)
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `states.id`

### 3. SQL Injection...

**Description:** This script displays all values in the `states` table of `hbtn_0e_0_usa` where the name matches the argument, ensuring safety from SQL injection.

**Usage:**
```bash
python safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
```

**Requirements:**
- MySQLdb module (import MySQLdb)
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `states.id`

### 4. List all cities

**Description:** This script lists all cities from the database `hbtn_0e_4_usa`.

**Usage:**
```bash
python list_all_cities.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- MySQLdb module (import MySQLdb)
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `cities.id`

### 5. All cities by state

**Description:** This script lists all cities of a given state from the database `hbtn_0e_4_usa`.

**Usage:**
```bash
python cities_by_state.py <mysql_username> <mysql_password> <database_name> <state_name>
```

**Requirements:**
- MySQLdb module (import MySQLdb)
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `cities.id`

### 6. First state model

**Description:** This script contains the class definition of a `State` and an instance `Base = declarative_base()` using SQLAlchemy.

**Usage:**
```bash
python first_state_model.py
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306

### 7. All states via SQLAlchemy

**Description:** This script lists all `State` objects from the database `hbtn_0e_6_usa` using SQLAlchemy.

**Usage:**
```bash
python all_states_sqlalchemy.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `states.id`

### 8. First state

**Description:** This script prints the first `State` object from the database `hbtn_0e_6_usa` using SQLAlchemy.

**Usage:**
```bash
python first_state_sqlalchemy.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306
- The state displayed must be the first in `states.id`

### 9. Contains `a`

**Description:** This script lists all `State` objects that contain the letter 'a' from the database `hbtn_0e_6_usa` using SQLAlchemy.

**Usage:**
```bash
python contains_a.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306
- Results sorted in ascending order by `states.id`

### 10. Get a state

**Description:** This script prints the `State` object with the name passed as an argument from the database `hbtn_0e_6_usa` using SQLAlchemy.

**Usage:**
```bash
python get_state.py <mysql_username> <mysql_password> <database_name> <state_name>
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306
- Results display the `states.id`
- If no state has the name searched for, display "Not found"

### 11. Add a new state

**Description:** This script adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa` using SQLAlchemy.

**Usage:**
```bash
python add_new_state.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306
- Prints the new `states.id` after creation

### 12. Update a state

**Description:** This script changes the name of a `State` object from the database `hbtn_0e_6_usa` using SQLAlchemy.

**Usage:**
```bash
python update_state.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306
- Changes the name of the `State` where `id = 2` to "New Mexico"

### 13. Delete states

**Description:** This script deletes all `State` objects with a name containing the letter 'a' from the database `hbtn_0e_6_usa` using SQLAlchemy.

**Usage:**
```bash
python delete_states.py <mysql_username> <mysql_password> <database_name>
```

**Requirements:**
- SQLAlchemy module
- Connection to a MySQL server running on localhost at port 3306

### 14. Cities in state

**Description:** This script lists all `City` objects from the database `hbtn_0e_14_usa` using SQLAlchemy.

**Usage:**
```bash
python model_city_fetch_by_state.py <mysql_username> <mysql_password>
