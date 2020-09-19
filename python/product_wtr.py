#!/usr/bin/env python

"""
Using the Database Helper functions we defined earlier, this file is for
using our helpers to create a product, and performing our database features
involving the product table
"""

#Imports
from db_helper import *


# Table Creation Methods
def init_Product_Table(connection):
	create_product_table = """
	CREATE TABLE IF NOT EXISTS Products (
		SKU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		Product_Name CHAR(75) NOT NULL,
		Total_Quantity INTEGER NOT NULL,
		Retail_Price DOUBLE NOT NULL,
		Shipping_Cost DOUBLE
	);
	"""

	execute_query(connection, create_product_table)

# add a product based on a list of data provided by the user
def addProduct(connection, product_data):
	product_columns = ['Product_Name', 'Total_Quantity', 'Retail_Price', 'Shipping_Cost']
	insert_query(connection, 'Products', product_columns, product_data)

# Will edit an existing product based on user set_condition based on SKU_ID
def editProduct(connection, set_condition, SKU_ID):
	edit_query(connection, 'Products', set_condition, 'SKU_ID = ' + SKU_ID)

# Will delete an existing product based on SKU_ID
def delProduct(connection, SKU_ID):
	delete_query(connection, 'Products', 'SKU_ID = ' + SKU_ID)


# Driver Code
if __name__ == '__main__':

	connection = create_connection("wtrdata.sqlite")
	#init_Product_Table(connection)
	#init_Transactions_Table(connection)

	# Create the Product Table
	init_Product_Table(connection)

	#Prep some sample data
	product_data = ['\'Blue Bottle\'', '\'99\'', '\'8.99\'', '\'1.99\'']
	addProduct(connection, product_data)

	select_query = "SELECT * FROM Products"
	products = execute_read_query(connection, select_query)

	delete_query(connection, 'Products', 'SKU_ID>2')

	printDB(connection, 'Products')
	for product in products:
		print(product)
