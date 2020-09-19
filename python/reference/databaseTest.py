#!/usr/bin/env python

#with sqlite, no need for an online server connection, local-friendly!
import sqlite3
from sqlite3 import Error

# 
count = 0

# Used to connect to an sqlite DB, denoted by 'path' of DB
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB Success!")
    except Error as e:
        print(f'The error \'{e}\' occurred')

    return connection

# will run an sql command 'query'
def execute_query(connection, query):
    count += 1
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully", count)
    except Error as e:
        print(f'the error {e} occurred', count)


def execute_read_query(connection, query):
    count += 1
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query executed successfully", count)
        return result
    except Error as e:
        print(f'The error \'{e}\' occurred', count)


#Driver Code

# Creating a sql file to store the DB
connection = create_connection("sm_app.sqlite")

# CREATING QUERIES EXAMPLE
# forming a query
query = """
CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name CHAR(50) NOT NULL,
    Age INTEGER,
    Gender CHAR(20),
    Nationality CHAR(50)
);
"""

# running a query
execute_query(connection, query)

create_comments_table = """
CREATE TABLE IF NOT EXISTS Comments (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Text CHAR(50) NOT NULL,
    User_ID INTEGER NOT NULL,
    Post_ID INTEGER NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES Users (ID) FOREIGN KEY (Post_ID) REFERENCES Posts (ID)
);
"""

execute_query(connection, create_comments_table)

create_likes_table = """
CREATE TABLE IF NOT EXISTS Likes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    User_ID INTEGER NOT NULL,
    Post_ID INTEGER NOT NULL,
    Gender CHAR(20),
    FOREIGN KEY (User_ID) REFERENCES Users (ID) FOREIGN KEY (Post_ID) REFERENCES Posts (ID)
);
"""

execute_query(connection, create_likes_table)

#INSERT EXAMPLES
insert_users = """
INSERT INTO
    Users(Name, Age, Gender, Nationality)
VALUES
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada');
"""

execute_query(connection, insert_users)

insert_posts = """
INSERT INTO
    Posts (Title, Description, User_ID)
VALUES
    ("Happy", "I am feeling very happy today", 1),
    ("Hot Weather", "The weather is very hot today", 2),
    ("Help", "I need some help with my work", 2),
    ("Great News", "I am getting married!", 1),
    ("Interesting Game", "It was a fantastic game of tennis", 5)
    ("Party", "Anyone up for a late-night rager???", 3);
"""

execute_query(connection, insert_posts)

insert_comments = """
INSERT INTO
  Comments (Text, User_ID, Post_ID)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
  """

execute_query(connection, insert_comments)

insert_likes = """
INSERT INTO
    Likes (User_ID, Post_ID)
VALUES
    (1, 6),
    (2, 3),
    (1, 5),
    (5, 4),
    (2, 4),
    (4, 2),
    (3, 6);
"""
execute_query(connection, insert_likes)

#SELECTING RECORDS EXAMPLES
