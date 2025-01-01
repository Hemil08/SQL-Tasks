# ------------------------------

# TASK 1: CREATE A SIMPLE TABLE

# ------------------------------

import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

# create student table

create_table_query = """
    CREATE TABLE students(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL,
        city TEXT
    );

"""

# create courses table

create_table_query2 = """
CREATE TABLE courses(
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        duration_weeks INTEGER,
        fee REAL
    );
"""

# create the enrollment table
create_enrollments_query = """
CREATE TABLE enrollments(
    id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(id) REFERENCES stundets(id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id),
    PRIMARY KEY(id,course_id)
)
"""


cursor.execute(create_table_query)
cursor.execute(create_table_query2)
cursor.execute(create_enrollments_query)

# -----------------------------------

# Task 2: INSERT DATA INTO TABLES

# -----------------------------------

insert_students_query = """
    INSERT INTO students(name,age,grade,city) VALUES
    ('Alice',20,85.5,'New York'),
    ('Bob',22,90.0,'Los Angeles'),
    ('Charlie',19,78.0,'Chicago'),
    ('Diana',21,88.5,'New York')
"""

insert_courses_query = """
    INSERT INTO courses(course_id,course_name,duration_weeks,fee) VALUES
    (101,'Python Basics',4,300.0),
    (102,'Data Science',12,1200.0),
    (103,'Web Development',8,800.0),
    (104,'Machine Learning',10,1500.0)
"""

insert_enrollments_query = """
    INSERT INTO enrollments(id,course_id) VALUES 
    (1,102),
    (2,103),
    (3,102)
"""

cursor.execute(insert_students_query)
cursor.execute(insert_courses_query)
cursor.execute(insert_enrollments_query)

connection.commit()

# -------------------------------

# TASK 3: QUERY DATA

# -------------------------------

# Retrieve all students who live in New York.

query_data1 = "SELECT * FROM students WHERE city=\"New York\";"

# Retrieve all courses with a fee greater than $1000.

query_data2 = "SELECT * FROM courses WHERE fee>1000.0"

# Find the student(s) with the highest grade.

query_data3 = "SELECT * FROM students WHERE grade=(SELECT MAX(grade) FROM students)"

# Retrieve students who are older than 20 years and live in Chicago.

query_data4 = "SELECT * FROM students WHERE age>20 AND city=\"Chicago\";"

# Find courses where the duration is 8 weeks or more, sorted by fee in descending order.

query_data5 = "SELECT * FROM courses WHERE duration_weeks>7 ORDER BY fee DESC"

# Retrieve the average grade of all students.

query_data6 = "SELECT AVG(grade) AS aveerage_grade FROM students"

# -------------------------------

# TASK 4: UPDATE DATA

# -------------------------------

# Increase the fee of all courses with a duration greater than 8 weeks by $200.

update_query1 = """
UPDATE courses
SET fee = fee + 200
WHERE duration_weeks > 8
"""

# Update the city of all students named Bob to San Francisco.

update_query2 = """
UPDATE students
SET city = "San Francisco"
"""

# Reduce the grade of students living in Chicago by 5 points.

update_query3 = """
UPDATE students
SET grade = grade - 5
WHERE city="Chicago"
"""

# Change the name of the course with course_id = 101 to Python for Beginners.

update_query4 = """
UPDATE courses
SET course_name = "Python for Beginners"
WHERE course_id = 101
"""

cursor.execute(update_query4)
connection.commit()

updated_courses_query = "SELECT * FROM  courses"
updated_students_query = "SELECT * FROM students"


# cursor.execute(updated_students_query)
# cursor.execute(updated_courses_query)

# -------------------------------

# TASK 5: DELETE DATA

# -------------------------------

# Remove all students with a grade below 80.

delete_query1 = """
DELETE FROM students
WHERE grade<80
"""

# Delete all courses with a fee less than $500.

delete_query2 = """
DELETE FROM courses
WHERE fee<500
"""

# Remove the student(s) with the name Diana.

delete_query3 = """
DELETE FROM students
WHERE name = "Diana"
"""

# Delete all courses with a duration less than 6 weeks.

delete_query4 = """
DELETE FROM courses
WHERE duration_weeks<6
"""

# cursor.execute(delete_query4)
# connection.commit()

deleted_courses_query = "SELECT * FROM courses"
deleted_students_query = "SELECT * FROM students"
cursor.execute(deleted_courses_query)

# -------------------------------

# TASK 6: COMBINING QUERIES

# -------------------------------

# Retrieve the names of students who are enrolled in courses with a fee greater than $1000 (assume a table enrollments that links students to courses by id and course_id).

combining_query1 = """
SELECT students.name
FROM students
INNER JOIN enrollments ON students.id = enrollments.id
INNER JOIN courses ON enrollments.course_id = courses.course_id
WHERE courses.fee > 1000;
"""

# Count the number of students living in each city.

combining_query2 = """
SELECT city,COUNT(*) AS student_count
FROM students
GROUP BY city
"""

# Calculate the total fees for courses with durations of 10 weeks or more.

combining_query3 = """
SELECT SUM(fee) as total_fees
FROM courses
WHERE duration_weeks > 9
"""

# Find the highest-paying course and list all students who live in New York.

combining_query4_1 = """
SELECT course_name,fee
FROM courses
ORDER BY fee DESC
LIMIT 1;
"""

combining_query4_2 = """
SELECT name
FROM students
WHERE city="New York";
"""

# Retrieve students whose names start with "A" or end with "e".

combining_query5="""
SELECT name
FROM students
WHERE name LIKE 'A%' OR name LIKE '%e';
"""

# cursor.execute(combining_query5)
# connection.commit()

# --------------------------------------------

# TASK 6: DESIGN AND POPULATE YOUR OWN TABLES

# --------------------------------------------

create_teachers_query="""
CREATE TABLE teachers(
    teacher_id INTEGER PRIMARY KEY,
    teacher_name TEXT NOT NULL,
    subject TEXT NOT NULL,
    salary REAL
)
"""

cursor.execute(create_teachers_query)

insert_teachers_query="""
    INSERT INTO teachers(teacher_name,subject,salary) VALUES
    ('Anuj Sir','Python',4000.00),
    ('Deepak Sir','Sql',3000.00),
    ('Ramesh Sir','React Js',8000.00),
    ('Nitika Mam','Javascript',5000.00)
"""
cursor.execute(insert_teachers_query)

# Find teachers who teach Python.

query1  = """
SELECT teacher_name 
FROM teachers
WHERE subject = 'Python'
"""

# Increase the salaries of teachers earning less than $4000 by 10%.

query2 = """
UPDATE teachers
SET salary = salary*1.10
WHERE salary<4000
"""

# Delete teachers with salaries greater than $6000.

query3 = """
DELETE FROM teachers
WHERE salary > 6000
"""

cursor.execute(query3)
connection.commit()

select_teachers_query = "SELECT * FROM  teachers;"
cursor.execute(select_teachers_query)


results = cursor.fetchall()

columns = [description[0] for description in cursor.description]

import pandas as pd

df = pd.DataFrame(results,columns=columns)

print(df)