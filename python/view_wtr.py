#!/usr/bin/env python

from tkinter import *
from tkinter.ttk import *

#Global Vars
PADX = (15, 15)
PADY = (10, 10)

# Methods
# Create and place a table using a TreeView tkinter widget
def create_Table(where, row = 4, column = 4):
	treeV = Treeview(where, selectmode = "extended", height = row, columns = column,)

	return treeV # so it can be placed outside of function
# Creates main window of the app
root = Tk()
root.title("wtrApplication")
#root.geometry('800x800')

# GUI INITIALIZATION
# The frame that other frames will be attached to
mainFrame = Frame(root)
mainFrame.pack()

# Title of the screen + Switch Button
titleFrame = Frame(mainFrame)
titleFrame.pack()

transLabel = Label(titleFrame, text="Transaction Record")
transLabel.pack()

# Packing elements into the grid
switchButton = Button(titleFrame, text="Switch Screens")
switchButton.pack()

# Create a frame for the table
tableFrame = Frame(mainFrame)
tableFrame.pack()

# TODO: Create your table using TreeView
treeVMain = create_Table(tableFrame)
treeVMain.pack()


# Addition Transaction Buttons
addTransBut = Button(tableFrame, text="Add Transaction").pack()
addTransLabel = Label(tableFrame, text="Add a Transaction Line to the record").pack()

# Edit Transaction Line Buttons
editTransBut = Button(tableFrame, text="Edit Transaction").pack()
editTransLabel = Label(tableFrame, text="Select a Transaction Line to Edit").pack()

# Remove Transaction Line Buttons
remTransBut = Button(tableFrame, text="Remove Transaction").pack()
remTransLabel = Label(tableFrame, text="Remove a Transaction Line from the record").pack()


root.mainloop()
