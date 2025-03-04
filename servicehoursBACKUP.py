#Import the relevant packages/libraries to be used in the program for creating GUI, connecting to database, display messages to the user, etc.

from tkinter import *
import tkinter.messagebox as MessageBox #to display messages in the application indicating that actions on the db are successful
from tkinter import ttk #For the dropdown/combo box menu
from dataoperations import * #Import functions from dataoperations.py to get and update records from the student database
from pdfgenerator import * #Import functions from pdfgenerator.py to get records from the service hours database and create PDF to view or print

#Test to see that the python file is created and the environment is setup correctly to run the python program. This line can be removed from the file after it executes successfully. 

#print('Test Working Python Program')  

#Create the GUI

root = Tk() #create GUI window
root.geometry('800x400') #set the dimensions height/width of the GUI window (root)
root.title("Student Community Service Hours") #Set the title of the GUI window (root)
root.configure(background="light blue")

#Creating labels for the form fields for user to enter data. The labels are created in compliance with ADA standards ensuring differently enabled users are able to use the system.

id = Label(root,text='Student ID',font=('bold',12))
id.pack()
id.place(x=20,y=30) #positioning the label accordingly in the GUI by setting margins

project_id=Label(root,text='Project Category',font=('bold',12))
project_id.place(x=20,y=60) #positioning the label accordingly in the GUI by setting margins

hours=Label(root,text='Service Hours',font=('bold',12))
hours.place(x=20,y=90) #positioning the label accordingly in the GUI by setting margins

#Creating text boxes for user to enter data

e_id=Entry()
e_id.place(x=200,y=30) #positioning the text box accordingly in the GUI by setting margins and aligning with the label

#Creating text boxes for user to enter data
e_project_id=Entry()
e_project_id.place(x=200,y=60)

#Creating text boxes for user to enter data
e_hours=Entry()
e_hours.place(x=200,y=90)

#Create button to insert record in the db
insertbutton=Button(root,text="Insert",font=("italic",12),bg="white",command=lambda:insertHours(e_id.get(),e_project_id.get(),e_hours.get()))
insertbutton.place(x=20,y=300)
#Create button to edit record in the db
updatebutton=Button(root,text="Update",font=("italic",12),bg="white",command=lambda:updateHours(e_id.get(),e_project_id.get(),e_hours.get()))
updatebutton.place(x=90,y=300)
#Create button to delete record from the db
deletebutton=Button(root,text="Delete",font=("italic",12),bg="white",command=lambda:deleteHours(e_id.get(),e_project_id.get()))
deletebutton.place(x=160,y=300)
#Create button to fetch single record from the db
get=Button(root,text="Get record",font=("italic",12),bg="white",command=root.destroy)
get.place(x=250,y=300)
#Create button to fetch all records from the db
get_all_student_records=Button(root,text="Get all records",font=("italic",12),bg="white",command=root.destroy)
get_all_student_records.place(x=350,y=300)
#Create List box to display all student records when the get all records button is clicked
get_all_records=Listbox(root)
get_all_records.place(x=550,y=30)
#Create button to fetch all records from the db and print into pdf file
get_all_student_records_into_pdf=Button(root,text="Create Report",font=("italic",12),bg="white",command=root.destroy)
get_all_student_records_into_pdf.place(x=450,y=300)
#Dropdown box for list of project categories
dropdown=ttk.Combobox(root,value=["Project categories","","",""])

root.option_add('*tearOff', FALSE)

#Create Menu for the GUI window 'root'
menu=Menu(root)
root.config(menu=menu)

#File menu
file=Menu(menu)
file.add_command(label='Generate Report - Service Hours',command=lambda:getAllRecordsIntoPdf())
file.add_command(label='Generate Report - Students',command=lambda:getAllStudentsIntoPdf())
file.add_command(label='Generate Report - Project Categories',command=lambda:getAllCategoriesIntoPdf())
file.add_command(label='Exit',command=root.destroy) #We can also use root.exit() command
menu.add_cascade(label='File',menu=file)

#Help menu
help=Menu(menu)
help.add_command(label='View Help',command=root.destroy)
help.add_command(label='About',command=root.destroy)
menu.add_cascade(label='Help',menu=help)

#Run/activate the mainloop event
root.mainloop()

