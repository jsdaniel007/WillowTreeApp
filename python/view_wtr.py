#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk # for treeview
from functools import partial
import enum
import sys

# Description
"""Branch: OOP-Refactor
Purpose: To refactor application behavior to better model an OOP-based approach
using https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
Bryan Oakley's top response

Milestones:
Convert Init of application -- IN PROGRESS
Convert new screen to a class
Convert each major visual element into a class (titlebar, treeview, button control panel)
"""

#Global Padding vars
TITLE_PAD_Y = 10

# Table Padding
TABLE_PAD_Y = 100

#
BOTTOM_S_FRAME_Y = 50

# Button Padding for individual elements
BUTTON_PAD_Y = 30
BUTTON_PAD_X = 50

# Label Padding for individual elements
LABEL_PAD_Y = 30
LABEL_PAD_X = 50


# Classes -- For every major reusable GUI element, we'll have a class for it
class ScreenID(enum.IntEnum):
	NONE = sys.maxsize
	TRANSACTIONS = 0
	PRODUCTS = 1

# An abstract class acting as an interface for different GUI screens to derive from
class Screen:
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
		self.m_ControlPanel.labelElements(TransButtonText, TransLabelText)

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
	m_buttons = []
	m_labels = []

	def __init__(self, parent):
		self.buttonFrame = tk.LabelFrame(parent, text="ButtonFrame")
		self.labelFrame = tk.LabelFrame(parent, text="LabelFrame")

	def labelElements(self, buttonTextArr, labelTextArr):
		for buttonText in buttonTextArr:
			self.m_buttons.append(tk.Button(self.buttonFrame, text=buttonText, pady=LABEL_PAD_Y))

		# Pack the labels into the Label frame
		for labelText in labelTextArr:
			self.m_labels.append(tk.Label(self.labelFrame, text=labelText, pady=LABEL_PAD_Y))

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
		initScreen = TransScreen(parent, Header(parent), DataView(parent), ControlPanel(parent))
		initScreen.labelElements()
		initScreen.show()

# Entry Point
if __name__ == '__main__':
	root = tk.Tk()
	MainApplication(root).pack(side='top', fill='both', expand=True)
	root.mainloop()
