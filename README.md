# SQL Tasks with Python

This project contains a Python script that demonstrates various SQL tasks such as creating tables, inserting data, updating records, and querying a database using SQLite.

## Prerequisites

- Python 3.x
- SQLite (bundled with Python)

## Installation

1. Clone the repository:
   `git clone https://github.com/YourUsername/SQL-Tasks.git`
2. Navigate to the project directory:
   `cd SQL-Tasks`

## Usage

To run the SQL tasks, simply execute the Python script:

`python sql_tasks.py`

## Tasks Included

Task 1: Create a Simple Table
Create a students table with the following columns:
id: Integer, Primary Key
name: Text, Not Null
age: Integer
grade: Real
city: Text
Create a courses table with the following columns:
course_id: Integer, Primary Key
course_name: Text, Not Null
duration_weeks: Integer
fee: Real

Task 2: Insert Data into Tables

Insert the following rows into the students table:

id name age grade city
1 Alice 20 85.5 New York
2 Bob 22 90.0 Los Angeles
3 Charlie 19 78.0 Chicago
4 Diana 21 88.5 New York

Insert the following rows into the courses table:

course_id course_name duration_weeks fee
101 Python Basics 4 300.0
102 Data Science 12 1200.0
103 Web Development 8 800.0

course_id course_name duration_weeks fee
104 Machine Learning 10 1500.0

Task 3: Query Data
Retrieve all students who live in New York.
Retrieve all courses with a fee greater than $1000.
Find the student(s) with the highest grade.
Retrieve students who are older than 20 years and live in Chicago.
Find courses where the duration is 8 weeks or more, sorted by fee in descending order.
Retrieve the average grade of all students.
Task 4: Update Data
Increase the fee of all courses with a duration greater than 8 weeks by $200.
Update the city of all students named Bob to San Francisco.
Reduce the grade of students living in Chicago by 5 points.
Change the name of the course with course_id = 101 to Python for Beginners.
Task 5: Delete Data

Remove all students with a grade below 80.
Delete all courses with a fee less than $500.
Remove the student(s) with the name Diana.
Delete all courses with a duration less than 6 weeks.
Task 6: Advanced Tasks (Combining Queries)
Retrieve the names of students who are enrolled in courses with a fee greater than $1000 (assume a
table enrollments that links students to courses by id and course_id).
Count the number of students living in each city.
Calculate the total fees for courses with durations of 10 weeks or more.
Find the highest-paying course and list all students who live in New York.
Retrieve students whose names start with "A" or end with "e".

Task 7: Design and Populate Your Own Tables

Create a new table teachers with the following columns:
teacher_id: Integer, Primary Key
teacher_name: Text, Not Null
subject: Text, Not Null
salary: Real
Populate the teachers table with at least 5 rows of data.
Write queries to:
Find teachers who teach Python.
Increase the salaries of teachers earning less than $4000 by 10%.
Delete teachers with salaries greater than $6000.
