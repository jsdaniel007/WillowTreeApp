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
class DataScreen():
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
class Window():
	def __init__(self):

		pass

# Class for the control panel for TR and Inventory
class controlPanel():
	def __init__(self):

		pass

# Class to structure the main application
# Note: args and kwargs are for accepting any number of Objects to init the app
class MainApplication(tk.Frame):
	# Using Instace attributes instead of class attributes
	def __init__(self, parent, *args, **kwargs): # parent = root
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		# <args/kwargs are your gui classes being set here like self.parent>
		self.header = Header(parent, "Transaction Record", "Switch Screens")

		# Now take your elements and pack them
		self.header.place('top')

# Methods

if __name__ == '__main__':
	root = tk.Tk()
	MainApplication(root).pack(side='top', fill='both', expand=True)
	root.mainloop()
