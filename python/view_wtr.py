#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk # for treeview

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

# Used as a template for the transaction record and inventory
# 3 Sections: Header, Treeview, and Control Panel
class mainScreen():
	def __init__(self, parent, Header, TreeView, ControlPanel):
		#Create 3 frames for the screen
		self.headerFrame = LabelFrame(parent, pady=TITLE_PAD_Y).pack()
		self.treeViewFrame = LabelFrame(parent, pady=TABLE_PAD_Y).pack()
		#self.controlPanelFrame = LabelFrame(parent).pack()

		# Initialize the elements passed in

	pass

# Class for the Header and Switch Screen Buttons
class Header():
	# Padding for Elements
	XPadding = 10
	YPadding = 10
	def __init__(self, parent, headerTitle, buttonSwitchText):
		self.headerTitle = tk.Label(parent, text = headerTitle)
		self.switchButton = tk.Button(parent, text = buttonSwitchText)

	# places
	def place(self, whatSide):
		self.headerTitle.pack(side=whatSide)
		self.switchButton.pack(side=whatSide)

# Class for the data in the treeview
class TreeView():
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

# Class for the control panel for TR and Inventory
class ControlPanel():
	def __init__(self, parent, xPadding, yPadding, buttonTextArr, labelTextArr):
		self.buttonFrame = tk.LabelFrame(parent, text="ButtonFrame", padx=xPadding, pady=yPadding)
		self.buttonFrame.pack(side="left", fill = tk.BOTH, expand=True)
		self.labelFrame = tk.LabelFrame(parent, text="LabelFrame", padx=xPadding, pady=yPadding)
		self.labelFrame.pack(side="right", fill = tk.BOTH, expand=True)

		#TODO: How will the GUI elements be defined?
		# Pack the buttons into the button frame
		for buttonText in buttonTextArr:
			tk.Button(self.buttonFrame, text=buttonText, pady=LABEL_PAD_Y).pack()

		# Pack the labels into the Label frame
		for labelText in labelTextArr:
			tk.Label(self.labelFrame, text=labelText, pady=LABEL_PAD_Y).pack()


# Class to structure the main application
# Note: args and kwargs are for accepting any number of Objects to init the app
class MainApplication(tk.Frame):
	# Using Instace attributes instead of class attributes
	def __init__(self, parent, *args, **kwargs): # parent = root
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		# <args/kwargs are your gui classes being set here like self.parent>
		self.header = Header(parent, "Transaction Record", "Switch Screens")
		self.treeView = TreeView(parent)

		# Now take your elements and pack them
		self.header.place('top')
		self.treeView.dTree.pack(pady=20)

		#Labels for GUI
		buttonTextArr = ["Add Transaction", "Edit Transaction", "Remove Transaaction"]
		labelTextArr = ["Add a Transaction Line to the Record", "Select a Transaction Line to Edit", "Remove a Transaction Line from the Record"]
		self.controlPanel = ControlPanel(parent, LABEL_PAD_X, BOTTOM_S_FRAME_Y, buttonTextArr, labelTextArr)

# Methods

# Entry Point
if __name__ == '__main__':
	root = tk.Tk()
	MainApplication(root).pack(side='top', fill='both', expand=True)
	root.mainloop()
