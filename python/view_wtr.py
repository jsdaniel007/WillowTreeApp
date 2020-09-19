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
mainFrame.grid(row=0, column=0)

# Title of the screen + Switch Button
titleFrame = Frame(mainFrame)
titleFrame.grid(row=0, column=0, rowspan=2)

transLabel = Label(titleFrame, text="Transaction Record")
transLabel.grid(columnspan=4, row = 0, column = 0, padx = PADX, pady = PADY)

# Packing elements into the grid
switchButton = Button(titleFrame, text="Switch Screens")
switchButton.grid(columnspan=4, row=1, column=0, padx = PADX, pady = PADY)

# Create a frame for the table
tableFrame = Frame(mainFrame)
tableFrame.grid(row=1, column=0)

# TODO: Create your table using TreeView
treeVMain = create_Table(tableFrame)
treeVMain.grid()


# Addition Transaction Buttons
addTransBut = Button(tableFrame, text="Add Transaction").grid(row=5, column=0, padx = PADX, pady = PADY)
addTransLabel = Label(tableFrame, text="Add a Transaction Line to the record").grid(row=5, column=1, padx = PADX, pady = PADY)

# Edit Transaction Line Buttons
editTransBut = Button(tableFrame, text="Edit Transaction").grid(row=6, column=0)
editTransLabel = Label(tableFrame, text="Select a Transaction Line to Edit").grid(row=6, column=1, padx = PADX, pady = PADY)

# Remove Transaction Line Buttons
remTransBut = Button(tableFrame, text="Remove Transaction").grid(row=5, column=2, padx = PADX, pady = PADY)
remTransLabel = Label(tableFrame, text="Remove a Transaction Line from the record").grid(row=5, column=3, padx = PADX, pady = PADY)


root.mainloop()
