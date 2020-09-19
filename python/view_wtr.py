#!/usr/bin/env python

from tkinter import *
from tkinter.ttk import *

#Global Vars
PADX = (15, 15)
PADY = (10, 10)

# Methods
# Create and place a table in 'where'
def create_Table(where, row, column):
	for r in range(row):
		for c in range(column):
			if r == 0:
				b = Label(where, text="columns?")
			else:
				b = Label(where, text="test")
			b.grid(row=r, column=c, padx = 10, pady = 0)


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
tableFrame = Frame(root)
tableFrame.grid(row=1, column=0)

# RELEVANT TABLE ELEMENTS
#create_Table(tableFrame, 4, 4)

# TODO: at this point you would have the database return a format in the array or something similar
elements = ["C", "C++", "Java", "C#"]

# Choosing selectmode as multiple for selecting multiple options
list_box = Listbox(root, selectmode ="multiple", height=len(elements))
list_box.grid(row=1, column=0)


for each_item in range(len(elements)):
	list_box.insert(END, elements[each_item])


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
