-- file: 5-full_table.sql
-- Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'first_table';
