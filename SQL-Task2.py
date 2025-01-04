import sqlite3
import pandas as pd

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

# Create the employees table
create_table_query = """
CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
);
"""

cursor.execute(create_table_query)

# Insert sample data into employees table
insert_data_query = """
INSERT INTO employees (name, department, salary) VALUES 
('Alice', 'HR', 60000),
('Bob', 'Engineering', 75000),
('Charlie', 'Engineering', 70000),
('Diana', 'Marketing', 50000),
('Eve', 'HR', 55000),
('Frank', 'Engineering', 80000),
('Grace', 'Marketing', 52000),
('Hank', 'Sales', 45000),
('Ivy', 'Sales', 47000),
('Jack', 'HR', 62000),
('Karen', 'Engineering', 72000),
('Leo', 'Marketing', 51000),
('Mona', 'Sales', 48000),
('Nina', 'HR', 58000),
('Oscar', 'Engineering', 76000),
('Paul', 'Marketing', 53000),
('Quinn', 'Sales', 49000),
('Rita', 'HR', 60000),
('Sam', 'Engineering', 74000),
('Tina', 'Marketing', 54000),
('Uma', 'Sales', 46000),
('Vince', 'HR', 61000),
('Walt', 'Engineering', 78000),
('Xena', 'Marketing', 55000),
('Yara', 'Sales', 50000),
('Zane', 'HR', 59000);
"""

cursor.execute(insert_data_query)
connection.commit()

# Aggregate functions example

aggregation_query = """
SELECT department,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary

FROM employees
GROUP BY department
ORDER BY average_salary DESC;
"""

cursor.execute(aggregation_query)

# Fetch and display results

results = cursor.fetchall()
columns = [description[0] for description in cursor.description] 
df = pd.DataFrame(results,columns=columns)
# print(df)

# Subquery example
subquery = """
SELECT department
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
"""

cursor.execute(subquery)

# Fetch and display results

results = cursor.fetchall()
# columns = [description[0] for description in cursor.description] 
df = pd.DataFrame(results,columns=["department"])
# print(df)


# Create projects table

create_projects_table = """
CREATE TABLE projects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);
"""

cursor.execute(create_projects_table)

# Insert sample data

insert_projects_data = """
INSERT INTO projects (name,department) VALUES
('Project Alpha', 'Engineering'),
('Project Beta', 'Marketing'),
('Project Gamma', 'HR');
"""

cursor.execute(insert_projects_data)
connection.commit()

# INNER JOIN

inner_join_query = """
SELECT e.name AS employee_name,e.department,p.name AS project_name
FROM employees e 
INNER JOIN projects p ON e.department = p.department;
"""

cursor.execute(inner_join_query)

# Fetch and display results

results = cursor.fetchall()
columns = [description[0] for description in cursor.description] 
df = pd.DataFrame(results,columns=columns)
# print(df)


# LEFT JOIN

left_join_query = """
SELECT e.name AS employee_name,e.department, p.name AS project_name
FROM employees e
LEFT JOIN projects p ON e.department = p.department;
"""

cursor.execute(left_join_query)

# Fetch and display results

results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
df = pd.DataFrame(results, columns=columns)
# print(df)


# RIGHT JOIN

right_join_query = """
SELECT p.name AS project_name,p.department, e.name AS employees_name
FROM projects p
LEFT JOIN employees e ON p.department = e.department;
"""

cursor.execute(right_join_query)

# Fetch and display results
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
df = pd.DataFrame(results, columns=columns)
# print(df)

# UNION 

full_outer_join_query = """
SELECT e.name AS employee_name,e.department,p.name AS project_name
FROM employees e 
LEFT JOIN projects p ON e.department = p.department
UNION
SELECT e.name AS employee_name,e.department,p.name AS project_name
FROM projects p
LEFT JOIN employees e ON p.department = e.department;
"""

cursor.execute(full_outer_join_query)

# Fetch and display results
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
df = pd.DataFrame(results, columns=columns)
# print(df)

# CROSS JOIN 

cross_join_query = """
SELECT e.name AS employee_name,e.department AS employee_department,
       p.name AS project_name,p.department AS project_department
FROM employees e
CROSS JOIN projects p;
"""
cursor.execute(cross_join_query)

results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
df = pd.DataFrame(results, columns=columns)
# print(df)

# CREATE VIEW

create_view = """
CREATE VIEW employee_summary AS
SELECT department,COUNT(*) AS total_employees,AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
"""

cursor.execute(create_view)

# Query the view
query_view = "SELECT * FROM employee_summary;"
cursor.execute(query_view)

# Fetch and display results
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
df = pd.DataFrame(results, columns=columns)
# print(df)


# TRANSACTIONS

# Using transactions

try:
    # Start transaction
    connection.execute("BEGIN;")

    # Insert a new employee
    connection.execute(
        "INSERT INTO employees (name,department,salary) VALUES ('Eve','HR',45000);"
    )

    # Insert another row (simulate an error by violating NOT NULL constraint)
    connection.execute(
        "INSERT INTO employees (name,department,salary) VALUES ('John',NULL,50000)"
    )

    # Commit transaction
    connection.commit()
except sqlite3.Error as e:
    # Rollback transaction in case of error
    print(f"Transaction failed:{e}")
    connection.rollback()

# INDEXES

# create an index on the salary coloumn

create_index = "CREATE INDEX idx_salary ON employees(salary);"
cursor.execute(create_index)

# Query using the index
indexed_query = "SELECT * FROM employees WHERE salary>60000;"
cursor.execute(indexed_query)

# Fetch and display results
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
df = pd.DataFrame(results,columns=columns)
print(df)