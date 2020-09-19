#!/usr/bin/env python

from tkinter import *
from tkinter.ttk import *

#Global Vars
PADX = (15, 15)
PADY = (10, 10)

# Methods
# Create and place a table using a TreeView tkinter widget
def create_TreeView(where, row = 10, column = 3):
	#TreeView Widget: w/ multiple select
	treeV = Treeview(where, selectmode = 'extended', height = row, columns = column)

	# Verticle Scroll Bar Widget
	verscrlbar = Scrollbar(where, orient = 'vertical', command = treeV.yview)
	verscrlbar.pack(side = 'right', fill = 'x')

	#configure TreeView
	treeV.configure(xscrollcommmand = verscrlbar.set)
	# Define columns
	treeV['columns'] = ("1", "2", "3")
	# Define heading
	treeV['show'] = 'headings'

	# Assigning the width and anchor to  the
	# respective columns
	treeV.column("1", width = 90, anchor ='c')
	treeV.column("2", width = 90, anchor ='se')
	treeV.column("3", width = 90, anchor ='se')

	# Assigning the heading names to the
	# respective columns
	treeV.heading("1", text ="Name")
	treeV.heading("2", text ="Sex")
	treeV.heading("3", text ="Age")

	# Inserting the items and their features to the
	# columns built
	treeV.insert("", 'end', text ="L1",
             values =("Nidhi", "F", "25"))
	treeV.insert("", 'end', text ="L2",
             values =("Nisha", "F", "23"))
	treeV.insert("", 'end', text ="L3",
             values =("Preeti", "F", "27"))
	treeV.insert("", 'end', text ="L4",
             values =("Rahul", "M", "20"))
	treeV.insert("", 'end', text ="L5",
             values =("Sonu", "F", "18"))
	treeV.insert("", 'end', text ="L6",
             values =("Rohit", "M", "19"))
	treeV.insert("", 'end', text ="L7",
             values =("Geeta", "F", "25"))
	treeV.insert("", 'end', text ="L8",
             values =("Ankit", "M", "22"))
	treeV.insert("", 'end', text ="L10",
             values =("Mukul", "F", "25"))
	treeV.insert("", 'end', text ="L11",
             values =("Mohit", "M", "16"))
	treeV.insert("", 'end', text ="L12",
             values =("Vivek", "M", "22"))
	treeV.insert("", 'end', text ="L13",
             values =("Suman", "F", "30"))

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
treeVMain = create_TreeView(tableFrame)
#treeVMain.pack()


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
