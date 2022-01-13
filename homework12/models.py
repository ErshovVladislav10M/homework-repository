"""
Using ORM framework of your choice, create models classes
created in Homework 6 (Teachers, Students, Homework and others).
- Target database should be sqlite (filename main.db localted in
current directory)
- ORM framework should support migrations.

Utilizing that framework capabilities, create
 - a migration file, creating all necessary database structures.
 - a migration file (separate) creating at least one record in each
created database table
 - (*) optional task: write standalone script (get_report.py) that
retrieves and stores the following information into CSV file report.csv
     for all done (completed) homeworks:
         Student name (who completed homework)
         Creation date
         Teacher name who created homework


Utilize ORM capabilities as much as possible, avoiding executing
raw SQL queries.
"""
import datetime

import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text

metadata = sqlalchemy.MetaData()

Homework = Table(
    "Homework",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("text", Text, nullable=False),
    Column("deadline", Integer(), nullable=False),
    Column("created", sqlalchemy.DateTime(), default=datetime.datetime.now()),
)

HomeworkResult = Table(
    "HomeworkResult",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("homework", ForeignKey("Homework.id"), nullable=False),
    Column("solution", Text(), nullable=False),
    Column("author", ForeignKey("Student.id"), nullable=False),
    Column("created", sqlalchemy.DateTime(), default=datetime.datetime.now()),
    Column("grade", Integer(), default=0),
)

Person = Table(
    "Person",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("last_name", String(50), nullable=False),
    Column("first_name", String(50), nullable=False),
)

Student = Table(
    "Student",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("person", ForeignKey("Person.id"), nullable=False),
)

Teacher = Table(
    "Teacher",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("person", ForeignKey("Person.id"), nullable=False),
)

Base.metadata.create_all(engine)
