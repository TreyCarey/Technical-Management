#Import Dependencies

#Tkinter is the GUI Framework i'm using
from tkinter import *
from tkinter.ttk import *

#Global Variables
programName = "New Window"

#Creates the TK() Object
master = Tk()

#Sets the Geometry of main
#Root window
master.geometry("200x200")

master.title(programName)

#Function to open a new window
#On a button click
def openNewWindow():

    #TopLevel Object which will be treated as a new window
    newWindow = Toplevel(master)

    #Sets the title of the TopLevel widget
    newWindow.title(programName)

    #Sets the Geometry of TopLevel
    newWindow.geometry("200x200")


mainloop()
