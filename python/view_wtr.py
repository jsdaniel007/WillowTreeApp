#!/usr/bin/env python

from tkinter import *
from tkinter import ttk # for treeview
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

# Methods


# Creates main window of the app
root = Tk()
root.title("wtrApplication")
#root.geometry('800x800')


# TITLE SECTION -- app title/buttons
# PROBLEM TRACKER -------
# Title of the screen + Switch Button
titleFrame = LabelFrame(root, pady=TITLE_PAD_Y).pack()

transLabel = Label(titleFrame, text="Transaction Record").pack()

switchButton = Button(titleFrame, text="Switch Screens").pack()


# TABLE SECTION -- TreeView to show data received from SQL query of database
# PROBLEM TRACKER -------
# TODO: Create your table using TreeView
# TODO: Populate table from SQL query using JOINS, VIEWS

# Create a frame for the table
tableFrame = LabelFrame(root, pady=TABLE_PAD_Y)
tableFrame.pack(fill = BOTH)

#PROBLEM TRACKER -------
#TODO:
#TODO: fix sizing and find a better manner of padding
my_tree = ttk.Treeview(tableFrame)

# Column Definition + Formatting
my_tree['columns'] = ("ex1", "ex2", "ex3")
my_tree.column("#0", width=100, minwidth=50)
my_tree.column("ex1", anchor=W, width=100)
my_tree.column("ex2", anchor=CENTER, width=100)
my_tree.column("ex3", anchor=W, width=100)

#Column Labels basically
my_tree.heading("#0", text="Phantom", anchor=W)
my_tree.heading("ex1", text="example1", anchor=W)
my_tree.heading("ex2", text="example2", anchor=CENTER)
my_tree.heading("ex3", text="example3", anchor=W)

# Add Data
my_tree.insert(parent='', index='end', iid=0, text="Phantom",
values=("John", 1, "Pepperoni"))
my_tree.insert(parent='', index='end', iid=1, text="Phantom",
values=("Johnny", 2, "Pepperoni"))
my_tree.insert(parent='', index='end', iid=2, text="Phantom",
values=("James", 3, "Pepperoni"))
my_tree.insert(parent='', index='end', iid=3, text="Phantom",
values=("Jackson", 4, "Pepperoni"))
my_tree.insert(parent='', index='end', iid=4, text="Phantom",
values=("Jameson", 5, "Pepperoni"))

my_tree.pack(pady=20)


# BOTTOM SECTION -- Action buttons with labels
buttonFrame = LabelFrame(root, text="this is a frame", padx=LABEL_PAD_X, pady=BOTTOM_S_FRAME_Y)
buttonFrame.pack(side="left", fill = BOTH, expand=True)

labelFrame = LabelFrame(root, text="this is a frame", padx=LABEL_PAD_X, pady=BOTTOM_S_FRAME_Y)
labelFrame.pack(side="right", fill = BOTH, expand=True)

# Addition Transaction Buttons
addTransBut = Button(buttonFrame, text="Add Transaction").pack(side='top', padx=BUTTON_PAD_X, pady=BUTTON_PAD_Y)
addTransLabel = Label(labelFrame, text="Add a Transaction Line to the record", pady=LABEL_PAD_Y).pack(side='top')

# Edit Transaction Line Buttons
editTransBut = Button(buttonFrame, text="Edit Transaction").pack( padx=BUTTON_PAD_X, pady=BUTTON_PAD_Y)
editTransLabel = Label(labelFrame, text="Select a Transaction Line to Edit", pady=LABEL_PAD_Y).pack()

# Remove Transaction Line Buttons
remTransBut = Button(buttonFrame, text="Remove Transaction").pack(side='bottom', padx=BUTTON_PAD_X, pady=BUTTON_PAD_Y)
remTransLabel = Label(labelFrame, text="Remove a Transaction Line from the record", pady=LABEL_PAD_Y).pack(side='bottom')


root.mainloop()
