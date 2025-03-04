from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import *
from PIL import Image, ImageTk

#Open Help menu screen in a new window, so user is able to refer to Help Contents as the user works in the application (GUI)
def openhelp():
	#Creating the Help GUI window
	root = Tk()
	root.title("Help Contents")
	root.geometry("900x500+120+120")
	root.images=[]

	#ScrolledText object to hold the Help contents
	help_text = ScrolledText(root,wrap=WORD,font=("Courier",12, "bold"))
	help_text.grid(row=1,column=0)

	#Populating the Help contents into the ScrolledText widget
	help_text.insert(END, "Community Service Hours:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot1 = PhotoImage(file='../img/ServiceHours.png',master=root)
	root.images.append(screenshot1)
	help_text.image_create(INSERT, image=screenshot1)
	help_text.image=screenshot1

	help_text.insert(END, "\n\nAdd Community Service Hours\n\nTo add service hours for a student, go to File >> Manage Service Hours and enter Student ID, Project Category and Service Hours. Click on the Add Service Hours button.\n\nDelete Community Service Hours\n\nTo delete service hours for a student, go to File >> Manage Service Hours and enter Student ID, Project Category. Click on the Delete Hours button.\n\nUpdate Community Service Hours\n\nTo update service hours for a student, go to File >> Manage Service Hours and enter Student ID, Project Category, Service Hours. Click on the Update Hours button.\n\n")
	help_text.insert(END, "Student Record:\n\n")
	
	#Adding screenshots from the application for the Help screen
	screenshot2 = PhotoImage(file='../img/StudentRecord.png',master=root)
	root.images.append(screenshot2)
	help_text.image_create(END, image=screenshot2)
	help_text.image=screenshot2

	help_text.insert(END, "\n\nAdd New Student\n\nTo add a new student, go to File >> Manage Students and enter Student ID, Student Name, Student Grade. Click on the Add Student button.\n\nUpdate Student\n\nTo update student information, go to File >> Manage Students and enter Student ID, Student Name, Student Grade. Click on the Update Student button.\n\nGet All Student Records\n\nTo view all student records, go to File >> Manage Students and click on the Get All Student Records button.\n\n")
	help_text.insert(END, "Service Project Category:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot3 = PhotoImage(file='../img/ProjectCategory.png',master=root)
	root.images.append(screenshot3)
	help_text.image_create(END, image=screenshot3)
	help_text.image=screenshot3

	help_text.insert(END, "\n\nAdd Project Category\n\nTo add a new project category, go to File >> Manage Project Categories and enter Project Category. Click on the Add Project Category button.\n\nGet All Project Categories\n\nTo view all project categories, go to File >> Manage Project Categories and click on the Get All project Categories button.\n\n")
	help_text.insert(END, "Reports:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot4 = PhotoImage(file='../img/Reports.png',master=root)
	root.images.append(screenshot4)
	help_text.image_create(END, image=screenshot4)
	help_text.image=screenshot4

	help_text.insert(END, "\n\nGenerate Student Service Hours Report\n\nTo generate a student service hours report, go to Download >> Download Report - Service Hours and a PDF version of the report will be downloaded.\n\nGenerate Student Report\n\nTo generate a student information report, go to Download >> Download Report - Students and a PDF version of the report will be downloaded.\n\nGenerate Project Categories Report\n\nTo generate a report of all project categories, go to Download >> Download Report - Project Categories and a PDF version of the report will be downloaded.\n\n")
	help_text.insert(END, "Help:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot5 = PhotoImage(file='../img/Help.png',master=root)
	root.images.append(screenshot5)
	help_text.image_create(END, image=screenshot5)
	help_text.image=screenshot5

	help_text.insert(END, "\n\nApplication Help\n\nFor help on how to use this application, go to Help >> Help Contents\n\n")
	help_text.insert(END, "About the application:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot6 = PhotoImage(file='../img/About.png',master=root)
	root.images.append(screenshot6)
	help_text.image_create(END, image=screenshot6)
	help_text.image=screenshot6

	help_text.insert(END, "\n\nAbout\n\nTo know more about the application, go to Help >> About\n\n")
	help_text.insert(END, "Exit:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot7 = PhotoImage(file='../img/Exit.png',master=root)
	root.images.append(screenshot7)
	help_text.image_create(END, image=screenshot7)
	help_text.image=screenshot7

	help_text.insert(END, "\n\nTo exit the application, go to File >> Exit.\n\n")

	#Disabling the ScrolledText widget so user cannot modify content
	help_text.configure(state=DISABLED)

	#Exit button to quit from Help screen
	exit = Button(root, text="Exit Help", command=root.destroy)
	exit.grid(row=0,column=0)