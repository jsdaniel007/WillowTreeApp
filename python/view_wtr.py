#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk # for treeview
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

# Use enum ScreenID to denote what titles go in the main application
HeaderText = ["Transaction Record", "Inventory Screen"]
HeaderButText = ["Switch to Products", "Switch to TR"]

TransLabelText = ["Add a Transaction Line to the Record", "Select a Transaction Line to Edit", "Remove a Transaction Line from the Record"]
TransButtonText = ["Add Transaction", "Edit Transaction", "Remove Transaction"]

ProdButtonText = ["Add Product", "Edit Product", "Remove Product"]
ProdLabelText = ["Add a Product to the Inventory", "Select a Product to Edit", "Remove a Product from the Inventory"]

# List for using the enum values to denote arrays
SCREEN_TEXT = [
	[TransButtonText, TransLabelText], # Transaction Record Screen Text List
	[ProdButtonText, ProdLabelText] #Product Record Screen Text List
]

# Classes -- For every major reusable GUI element, we'll have a class for it
class Screen(enum.IntEnum):
	NONE = sys.maxsize
	TRANSACTIONS = 0
	PRODUCTS = 1

# Used as a template for the TRANSACTIONS record and inventory
# 3 Sections: Header, Treeview, and Control Panel
class MainScreen():
	m_Screen_ID = Screen.NONE

	#init EMPTY elements
	def __init__(self, parent):
		#Create 3 frames for the screen
		self.headerFrame = tk.LabelFrame(parent, text="header", pady=TITLE_PAD_Y)
		self.treeViewFrame = tk.LabelFrame(parent, text="treeview", pady=TABLE_PAD_Y)
		self.controlPanelFrame = tk.LabelFrame(parent, text="control Panel",)

		# Initialize the elements passed in
		#self.header = Header(parent, "TRANSACTIONS Record", "Switch Screens")
		self.header = Header(self.headerFrame)
		self.treeView = TreeView(self.treeViewFrame)
		self.controlPanel = ControlPanel(self.controlPanelFrame, LABEL_PAD_X, BOTTOM_S_FRAME_Y)

	def labelElements(self, screen_ID, cpButtonText, cpLabelText):
		# ID Screen based on
		self.m_Screen_ID = screen_ID

		# Header text
		# Use the enum types to declare what the screen should use
		self.header.labelElements(HeaderText[screen_ID], HeaderButText[screen_ID])

		# Treeview Text

		# Control Panel Labeling
		self.controlPanel.labelElements(SCREEN_TEXT[screen_ID][0], SCREEN_TEXT[screen_ID][0])

	def show(self):
		# Frame packing
		self.headerFrame.pack()
		self.treeViewFrame.pack()
		self.controlPanelFrame.pack()

		#Actual Element Packing
		self.header.place('top')
		self.treeView.dTree.pack(pady=20)
		self.controlPanel.place()


# Class for the Header and Switch Screen Buttons
class Header():
	# Padding for Elements
	XPadding = 10
	YPadding = 10
	def __init__(self, parent):
		self.headerTitle = tk.Label(parent)
		self.switchButton = tk.Button(parent)

	def labelElements(self, headerTitle, buttonTitle):
		self.headerTitle['text'] = headerTitle
		self.switchButton['text'] = buttonTitle

	# generic, currently used for switchbutton
	def addCommand(element, command):
		element['command'] = command

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
	# Class contained for show() function
	m_buttons = []
	m_labels = []
	def __init__(self, parent, xPadding, yPadding):
		self.buttonFrame = tk.LabelFrame(parent, text="ButtonFrame", padx=xPadding, pady=yPadding)
		self.buttonFrame.pack(side="left", fill = tk.BOTH, expand=True)
		self.labelFrame = tk.LabelFrame(parent, text="LabelFrame", padx=xPadding, pady=yPadding)
		self.labelFrame.pack(side="right", fill = tk.BOTH, expand=True)


	def labelElements(self, buttonTextArr, labelTextArr):
		for buttonText in buttonTextArr:
			self.m_buttons.append(tk.Button(self.buttonFrame, text=buttonText, pady=LABEL_PAD_Y))

		# Pack the labels into the Label frame
		for labelText in labelTextArr:
			self.m_labels.append(tk.Label(self.labelFrame, text=labelText, pady=LABEL_PAD_Y))

	def place(self):
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

		initScreen = MainScreen(parent)

		# Give the TRANSACTIONS Screen Array to work with
		initScreen.labelElements(Screen.TRANSACTIONS, SCREEN_TEXT[Screen.TRANSACTIONS][0], SCREEN_TEXT[Screen.TRANSACTIONS][1])


		initScreen.show()

def switchScreen(mainScreen):
	if mainScreen.m_Screen_ID == Screen.TRANSACTIONS:
		mainScreen.labelElements(Screen.PRODUCTS, SCREEN_TEXT[Screen.PRODUCTS][0], SCREEN_TEXT[Screen.PRODUCTS][1])
	elif mainScreen.m_Screen_ID == Screen.PRODUCTS:
		mainScreen.labelElements(Screen.TRANSACTIONS, SCREEN_TEXT[Screen.TRANSACTIONS][0], SCREEN_TEXT[Screen.TRANSACTIONS][1])


# Entry Point
if __name__ == '__main__':
	root = tk.Tk()
	MainApplication(root).pack(side='top', fill='both', expand=True)
	root.mainloop()
