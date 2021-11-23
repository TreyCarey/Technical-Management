#Import Dependencies

#Tkinter is the GUI Framework i'm using
from tkinter import *
from tkinter.ttk import *

#Global Variables
programName = "New Window"

#Creates the TK() Object
master = Tk()

#Sets the Geometry & Title of main root window
master.geometry("1024x768")
master.title(programName)

welcomeLabel = Label(master, text = "Welcome to " + programName + "!")
welcomeLabel.pack()

optionsText = Label(master, text = "Please choose one of the following options")
optionsText.pack()

#Make the frame for the buttons
middleFrame = Frame(master)
middleFrame.pack()

#Launch Asset Manager
assetManagerButton = Button(middleFrame, text = "Asset Manager")
assetManagerButton.pack(side = TOP)

#Input List Button
inputListButton = Button(middleFrame, text = "Input List")
inputListButton.pack()

#Stage Plot Button
stagePlotButton = Button(middleFrame, text = "Stage Plot")
stagePlotButton.pack(side = BOTTOM)

mainloop()