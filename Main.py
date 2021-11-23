#Import Dependencies

#Tkinter is the GUI Framework i'm using
from tkinter import *
from tkinter.ttk import *

#Global Variables
programName = "Technical Manager"
versionNumber = "V0.01"

#Creates the TK() Object
master = Tk()

#Sets the Geometry & Title of main root window
master.geometry("256x256")
master.title(programName)

#Make the frame for the buttons
middleFrame = Frame(master)
middleFrame.pack(fill = "both", expand = True, padx = 20, pady = 20)

#Create Welcome Label
welcomeLabel = Label(middleFrame, text = "Welcome to " + programName + "!")
welcomeLabel.pack(side = TOP)

#Create options text
optionsText = Label(middleFrame, text = "Please choose one of the following options")
optionsText.pack(side = TOP, pady = 20)

#Launch Asset Manager
assetManagerButton = Button(middleFrame, text = "Asset Manager")
assetManagerButton.pack(side = TOP, fill = "x")

#Input List Button
inputListButton = Button(middleFrame, text = "Input List")
inputListButton.pack(side = TOP, fill = "x")

#Stage Plot Button
stagePlotButton = Button(middleFrame, text = "Stage Plot")
stagePlotButton.pack(side = TOP, fill = "x")

#Create Versioning Label
versionLabel = Label(middleFrame, text = versionNumber)
versionLabel.pack(side = BOTTOM, pady = 10)

mainloop()