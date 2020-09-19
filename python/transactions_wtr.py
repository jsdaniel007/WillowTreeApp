#!/usr/bin/env python

# Imports
from db_helper import *

# Table Creation Methods
def init_Transactions_Table(connection):
	create_transactions_table = """
	CREATE TABLE IF NOT EXISTS Transactions (
		TR_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		Date DATETIME NOT NULL,
		Count INTEGER NOT NULL,
		Product_ID INTEGER NOT NULL,
		Customer_Name CHAR(100),
		FOREIGN KEY (Product_ID) REFERENCES Products (SKU_ID)
	);
	"""

	execute_query(connection, create_transactions_table)

# add a transaction based on a list of data provided by the user
def addTransaction(connection, transaction_data):
	transaction_columns = ['Date', 'Count', 'Product_ID', 'Customer_Name']
	insert_query(connection, 'Transactions', transaction_columns, transaction_data)

# Will edit an existing transaction based on user set_condition based on SKU_ID
def editTransaction(connection, set_condition, TR_ID):
	edit_query(connection, 'Transactions', set_condition, 'TR_ID = ' + TR_ID)

# Will delete an existing transaction based on SKU_ID
def delTransaction(connection, TR_ID):
	delete_query(connection, 'Transactions', 'TR_ID = ' + TR_ID)


# Driver Code
if __name__ == '__main__':

	connection = create_connection("wtrdata.sqlite")
	#init_Product_Table(connection)
	#init_Transactions_Table(connection)

	# Create the Product Table
	init_Transactions_Table(connection)

	#Prep some sample data
	product_columns = ['Date', 'Count', 'Product_ID', 'Customer_Name']
	product_data = ['\'2020-07-18\'', '\'4\'', '\'1\'', '\'Chris McClure\'']
	insert_query(connection, 'Transactions', product_columns, product_data)

	# YAY! 
	select_query = "SELECT * FROM Transactions INNER JOIN Products ON Transactions.Product_ID = Products.SKU_ID"
	transactions = execute_read_query(connection, select_query)
	printDB(connection, 'Transactions', select_query)

	#delete_query(connection, 'Transactions')

	for transaction in transactions:
		print(transaction)
