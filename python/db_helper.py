#!/usr/bin/env python

# Imports
import sqlite3
from sqlite3 import Error

# Classes
# Methods

# Used to connect to an sqlite DB, denoted by 'path' of DB
def create_connection(path):
	connection = None
	try:
		connection = sqlite3.connect(path)
		print("Connection to SQLite DB Success!")
	except Error as e:
		print(f'The error \'{e}\' occurred')

	return connection


# Execute CREATE TABLE, INSERT, UPDATE, DELETE, etc.
def execute_query(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		print("Query executed successfully")
	except Error as e:
		print(f'the error \'{e}\' occurred')


# Execute for SELECT commands, including JOIN,
def execute_read_query(connection, query):
	cursor = connection.cursor()
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		print("Query executed successfully")
		return result
	except Error as e:
		print(f'The error \'{e}\' occurred')


# Will be used for adding to the database from GUI
def select_query(connection, columns, table, condition="", raw_query=""):
	select_query = "SELECT " + columns + " FROM " + table

	if not condition == "":
		select_query += " WHERE " + condition
	elif not raw_query == "":
		select_query = raw_query

	execute_read_query(connection, select_query)


# creates SQL INSERT from string text provided by the prompt
def insert_query(connection, table, columnArr, valuesArr):
	#using the column and values to automate SQL statements
	insert_query =  "INSERT INTO " + table + " (" + createCommaList(columnArr) + ") VALUES (" + createCommaList(valuesArr) + ");"

	execute_query(connection, insert_query)

#uses UPDATE query to change
def edit_query(connection, table, set_condition, condition):
	update_query = "UPDATE " + table + " SET " + set_condition + " WHERE " + condition + ";"

	execute_query(connection, update_query)

# creates SQL DELETE from string text provided
def delete_query(connection, table, condition=""):
	delete_query = "DELETE FROM " + table + " WHERE " + condition + ';'

	#delete all records in the table, keeping DB Structure
	if condition == "":
		delete_query = "DELETE FROM " + table + ';'

	execute_query(connection, delete_query)

#Can't handle JOIN's yet, but can print regular tables, SQL
def printDB(connection, table, select_query):
	column_Str = ""
	column_prints = "PRAGMA table_info(" + table + ");"
	columns = execute_read_query(connection, column_prints)
	database = execute_read_query(connection, select_query)

	#print column labels
	for col in range(len(columns)):
		column_Str += columns[col][1] + ' | '

	print(column_Str)
	for data in database: #Print DB Contents
		print(data)


# Returns a string of the elements comma seperated for an INSERT INTO statement
def createCommaList(elements):
	delimiter = ', '
	clist = ""

	# Append the elements into a comma-string
	for ele in range(len(elements)):
		if ele == (len(elements) - 1):
			delimiter = ''

		clist += elements[ele] + delimiter

	return clist

if __name__ == '__main__':
	connection = create_connection("wtrdata.sqlite")

	printDB(connection, 'Products', 'SELECT * FROM Products')
