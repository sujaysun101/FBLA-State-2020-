from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import *

#Open About screen in a new window, so user is able to view information about the application
def openabout():
	#Creating the About GUI window
	root = Tk()
	root.title("About")
	root.geometry("900x400+120+120")
	
	#ScrolledText object to hold the About contents
	about_text = ScrolledText(root,wrap=WORD,font=("Courier",12, "bold"))
	about_text.grid(row=1,column=0)
	
	#Populating the About contents into the ScrolledText widget
	about_text.tag_configure("centered", justify="center") #Center align the text
	about_text.insert(END, "\n\n\n\n\n\n\n",("centered",))
	about_text.insert(END, "Chapter Student Community Service Hours For NYS FBLA State Competition 2020\n\n",("centered",))
	about_text.insert(END, "Developed by Sujay Sundar (9th Grade)\n\n",("centered",))
	about_text.insert(END, "Version 1.0\n\n",("centered",))
	
	#Disabling the ScrolledText widget so user cannot modify content
	about_text.configure(state=DISABLED) #Center align the text

	#Exit button to quit from About screen
	exit = Button(root, text="Exit", command=root.destroy)
	exit.grid(row=0,column=0)