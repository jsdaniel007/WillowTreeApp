#!/usr/bin/env python

from tkinter import *
from tkinter.ttk import *


# Creates the main window of the application
root = Tk()
root.title("First_Program")
#root.geometry('600x600')

# Packing into grids
Label(root, text="Label 1").grid(row = 0, column = 0)
Label(root, text="Label 2").grid(row = 1, column = 0)

# Entry Objects?
e1 = Entry(root)
e2 = Entry(root)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


button1 = Button(root, text="Button 1")
button1.grid(columnspan=2, row=2, column=0)

button2 = Button(root, text="Button 2")
button2.grid(columnspan=2, row=2, column=2)

# Calling mainloop method, used for drawing to the screen
root.mainloop()
