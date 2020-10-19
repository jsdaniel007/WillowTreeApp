#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk # for treeview
from functools import partial
import enum
import sys

# Description
"""
Purpose: To refactor application behavior to better model an OOP-based approach
using https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
Bryan Oakley's top response
"""


# Classes -- For every major reusable GUI element, we'll have a class for it
class ScreenID(enum.IntEnum):
	NONE = sys.maxsize
	TRANSACTIONS = 0
	TRANS_ENTRY = 1
	PRODUCTS = 2
	PRODUCT_ENTRY = 3

# An abstract class acting as an interface for different GUI screens to derive from
class Screen():
	m_Screen_ID = ScreenID.NONE

	# Initialize sent in variables
	def __init__(self, parent, header, dataTree, controlPanel):
		self.m_Parent = parent
		self.m_Header = header
		self.m_DataView = dataTree
		self.m_ControlPanel = controlPanel

		#Create frames for each objects
		self.headerFrame = tk.LabelFrame(self.m_Parent, text="Header", pady=10)
		self.dataViewFrame = tk.LabelFrame(self.m_Parent, text="TreeView", pady=100)
		self.controlPanelFrame = tk.LabelFrame(self.m_Parent, text="Control Panel")

		self.labelElements()
		self.show()
	# Label the Header, DataTree, and Control Panel objects
	def labelElements(self):
		# Variables for Header, DataView, and ControlPanel
		pass # Generic

	def show(self):
		# Frame packing
		self.headerFrame.pack()
		self.dataViewFrame.pack()
		self.controlPanelFrame.pack()

		# Element Packing
		self.m_Header.show()
		self.m_DataView.dTree.pack(pady=20)
		self.m_ControlPanel.show()

# Child Classes for Main Screens
class TransScreen(Screen):
	m_Screen_ID = ScreenID.TRANSACTIONS

	def __init__(self, parent, header, dataTree, controlPanel):
		super().__init__(parent, header, dataTree, controlPanel)

	def labelElements(self):
		# Transaction Header Text
		TransHeaderLabel = "Transaction Record"
		TransHeaderButton = "Switch to Products"
		self.m_Header.labelElements(TransHeaderLabel, TransHeaderButton)

		# Transaction Control Panel Text
		TransButtonText = ["Add Transaction", "Edit Transaction", "Remove Transaction"]
		TransLabelText = ["Add a Transaction Line to the Record", "Select a Transaction Line to Edit", "Remove a Transaction Line from the Record"]
		self.m_ControlPanel.labelElements(TransButtonText, TransLabelText)

	def show(self):
		super().show()

class ProductScreen(Screen):
	m_Screen_ID = ScreenID.PRODUCTS

	def __init__(self, parent, header, dataTree, controlPanel):
		super().__init__(parent, header, dataTree, controlPanel)

	def labelElements(self):
		# Product Header Text
		ProductHeader = "Product Screen"
		HeaderLabel = "Switch to TR"
		self.m_Header.labelElements(ProductHeader, HeaderLabel)

		# Product Control Panel Text
		ProdButtonText = ["Add Product", "Edit Product", "Remove Product"]
		ProdLabelText = ["Add a Product to the Inventory", "Select a Product to Edit", "Remove a Product from the Inventory"]
		self.m_ControlPanel.labelElements(ProdButtonText, ProdLabelText)

	def show(self):
		super().show()

# Base Class Screen for action button menus (eg. Add Transaction, Edit Transaction, etc.)
class subScreen():
	m_Screen_ID = ScreenID.NONE
	# To be used by base classes
	m_LabelText = ["Base Class"]
	m_Entries = []
	m_Labels = []

	# Add the frames to format the screen
	def __init__(self, parent):
		self.backButton = tk.Button(parent)
		self.formFrame = tk.LabelFrame(parent)
		self.confirmButton = tk.Button(parent)

	# Spawns new screen over original screen for data entry
	def spawnScreen():
		pass

	# fill self with screen elements to be loaded in a child class
	def fillForm(self, parent, entryCount, labels):
		for entry in range(entryCount):
			self.m_Labels.append( tk.Label(parent, text = labels[entry]) )
			self.m_Entries.append( tk.Entry(parent, bd = 5) )

	# Add text to the GUI elements
	def labelElements(self, pairCount, labels):
		self.backButton['text'] = "<< Cancel"
		self.formFrame['text'] = "Form Frame"
		self.fillForm(self.formFrame, pairCount, labels)
		self.confirmButton['text'] = "Confirm"

	# entries: array holding entry variables
	# labels: list holding names for Labels
	def show(self):
		self.backButton.pack()
		self.formFrame.pack()
		for index in range(len(self.m_LabelText)):
			self.m_Labels[index].pack()
			self.m_Entries[index].pack()

		self.confirmButton.pack()

# Child Classes for subScreen
class addScreen(subScreen):
	m_LabelText = ["Date", "Quantity", "Product Name", "Customer", "Sale Price", "Gross", "Shipping"  ]
	m_Entries = [] # fill with details

	def __init__(self, parent):
		super().__init__(parent)
		self.labelElements()
		self.show()

	def spawnScreen(self):
		top = tk.Toplevel()
		top.title = "Add Transaction Menu"

	def fillForm(self, parent, entryCount, labels):
		super().fillForm(parent, entryCount, labels)

	def labelElements(self):
		super().labelElements( len(self.m_LabelText), self.m_LabelText)

	def show(self):
		super().show()

# TODO: Work functionality to allow for filling information
class editScreen(subScreen):
	m_LabelText = ["Date", "Quantity", "Product Name", "Customer", "Sale Price", "Gross", "Shipping"]
	m_Entries = []

	def __init__(self, parent):
		super().__init__(parent)
		self.labelElements(parent)
		self.show()

	def spawnScreen(self):
		top = tk.Toplevel()
		top.title = "Edit Transaction Menu"

	def fillForm(self, parent):
		super().fillForm(parent, len(self.m_Entries), self.m_LabelText)

	def labelElements(self):
		super().labelElements(len(self.m_LabelText), self.m_LabelText)

	def show(self):
		super().show()

# Class for the Header Buttons
class Header():

	def __init__(self, parent):
		self.headerTitle = tk.Label(parent)
		self.switchButton = tk.Button(parent)

	def labelElements(self, headerText, buttonText):
		self.headerTitle['text'] = headerText
		self.switchButton['text'] = buttonText

	def show(self):
		self.headerTitle.pack()
		self.switchButton.pack()

# Using a Treeview, show the SQL database queries
class DataView():

	def __init__(self, parent):
		self.dTree = ttk.Treeview(parent)

		# TODO: define columns based on SQL table results
		self.dTree['columns'] = ("ex1", "ex2")

		# TODO: Refactor Programmatically
		self.dTree.column("#0", width=100, minwidth=50)
		self.dTree.column("ex1", anchor = tk.W, width=100)
		self.dTree.heading("#0", text="Phantom", anchor = tk.W)
		self.dTree.heading("ex1", text="example1", anchor = tk.W)

		self.dTree.insert(parent='', index='end', iid=0, text="Phantom",
		values=("John", 1, "Pepperoni"))
		self.dTree.insert(parent='', index='end', iid=1, text="Phantom",
		values=("Johnny", 2, "Sausage"))

# Class for the control panel below the dataView
class ControlPanel():
	m_buttons = [] # index order: add, edit, delete
	m_labels = []

	def __init__(self, parent):
		self.buttonFrame = tk.LabelFrame(parent, text="ButtonFrame")
		self.labelFrame = tk.LabelFrame(parent, text="LabelFrame")

	def labelElements(self, buttonTextArr, labelTextArr):
		for buttonText in buttonTextArr:
			self.m_buttons.append(tk.Button(self.buttonFrame, text=buttonText, pady=30))

		# Pack the labels into the Label frame
		for labelText in labelTextArr:
			self.m_labels.append(tk.Label(self.labelFrame, text=labelText, pady=30))

	def show(self):
		self.buttonFrame.pack(side="left", fill = tk.BOTH, expand=True)
		self.labelFrame.pack(side="right", fill = tk.BOTH, expand=True)

		for button in self.m_buttons:
			button.pack()

		for label in self.m_labels:
			label.pack()

# Class to structure the main application
# Note: args and kwargs are for accepting any number of Objects to init the app
class MainApplication(tk.Frame):
	# Using Instace attributes instead of class attributes
	def __init__(self, parent, *args, **kwargs): # parent = root
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		# Create an Initial Screen
		#initScreen = TransScreen(parent, Header(parent), DataView(parent), ControlPanel(parent))
		#initScreen = ProductScreen(parent, Header(parent), DataView(parent), ControlPanel(parent))
		initScreen = addScreen(parent)


# Entry Point
if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('600x600')
	MainApplication(root).pack(side='top', fill='both', expand=True)
	root.mainloop()
