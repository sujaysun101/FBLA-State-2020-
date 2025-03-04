#Import the relevant packages/libraries to be used in the program for creating GUI, connecting to database, display messages to the user, etc.

from tkinter import *
import tkinter.messagebox as MessageBox #to display messages in the application indicating that actions on the db are successful
from tkinter import ttk #For the dropdown/combo box menu
from dataoperations import * #Import functions from dataoperations.py to get and update records from the service hours database
from pdfgenerator import * #Import functions from pdfgenerator.py to get records from the service hours database and create PDF to view or print
from help import*
from about import*

#Create the GUI

root = Tk() #create GUI window
root.geometry('800x400') #set the dimensions height/width of the GUI window (root)
root.title("Student Community Service Hours") #Set the title of the GUI window (root)
root.configure(background="light blue")
root.resizable(0,0) #Disable the maximize window option to prevent distortion of GUI

service_hours_frame=Frame(root,relief='raised', borderwidth=5) #Defining the frame within the parent GUI window for Service Hours screen
student_record_frame=Frame(root,relief='raised', borderwidth=5) #Defining the frame within the parent GUI window for Student Record screen
project_category_frame=Frame(root,relief='raised', borderwidth=5) #Defining the frame within the parent GUI window for Project Category screen

def loadStudentPage():
	#Ensure the other pages/frames are closed/hidden and only the Student page is displayed
	project_category_frame.grid_forget() 
	service_hours_frame.grid_forget()

	#Student page is displayed
	student_record_frame.grid(row=0,column=0,padx=90,pady=20)

def loadServiceHoursPage():
	#Ensure the other pages/frames are closed/hidden and only the Service Hours page is displayed
	project_category_frame.grid_forget()
	student_record_frame.grid_forget()
	
	#Service Hours page is displayed
	service_hours_frame.grid(row=0,column=0,padx=85,pady=30)
	
def loadProjectCategoryPage():
	#Ensure the other pages/frames are closed/hidden and only the Project category page is displayed
	service_hours_frame.grid_forget()
	student_record_frame.grid_forget()

	#Project category page is displayed
	project_category_frame.grid(row=0,column=0,padx=195,pady=45)

#Get a Student's hours to display in the Treeview (TV) object on the GUI
def getStudentHoursForTV(student_id):
	#Debug statement to check if student id is received in this function
	print("Student ID is: "+student_id)

	#Clear the contents of the Treeview object before populating it with the result from the db
	for i in service_hours_tree.get_children():
		service_hours_tree.delete(i)

	results=getStudentHours(student_id)
	
	#Debug statement to check results from the database
	print (results)

	for record in results:
		#Debug statement to check results from the database inside the for loop
		print (results)
		service_hours_tree.insert('',0,text=record[0],values=(record[1],record[2]))

#Get All Student Hours to display in the Treeview (TV) object on the GUI
def getAllStudentHoursForTV():
	
	for i in service_hours_tree.get_children():
		service_hours_tree.delete(i)

	results=getAllStudentHours()
	
	#Debug statement to check results from the database
	print (results)

	for record in results:
		#Debug statement to check results from the database inside the for loop
		print (results)
		service_hours_tree.insert('',0,text=record[0],values=(record[1],record[2]))

#Get All Students to display in the Treeview (TV) object on the GUI
def getAllStudentsForTV():
	
	for i in student_record_tree.get_children():
		student_record_tree.delete(i)

	results=getAllStudents()
	
	#Debug statement to check results from the database
	print (results)

	for record in results:
		#Debug statement to check results from the database inside the for loop
		print (results)
		student_record_tree.insert('',0,text=record[0],values=(record[1],record[2]))

#Get All Project Categories to display in the Treeview (TV) object on the GUI
def getAllCategoriesForTV():
	
	for i in project_category_tree.get_children():
		project_category_tree.delete(i)

	results=getAllCategories()
	
	#Debug statement to check results from the database
	print (results)

	for record in results:
		#Debug statement to check results from the database inside the for loop
		print (results)
		project_category_tree.insert('',0,text=record[0],values=(record[1],)) #Trailing comma is added to print all words of the Project category instead of just the first word

def getAllCategoryIDsInCB():
	results=getAllCategoryIDs()
	
	#Debug statement to check results from the database
	print (results)
	categories=[]
	for record in results:
		#Debug statement to check results from the database inside the for loop
		print (results)
		categories.append(record[0])
	return categories

#Service Hours Screen starts here

#Creating labels for the form fields for user to enter data. The labels are created in compliance with ADA standards ensuring differently enabled users are able to use the system.

id = Label(service_hours_frame,text='Student ID',font=('bold',12))
id.grid(row=0,column=0) #positioning the label accordingly in the GUI

project_id=Label(service_hours_frame,text='Project Category',font=('bold',12))
project_id.grid(row=1,column=0) #positioning the label accordingly in the GUI by setting margins

hours=Label(service_hours_frame,text='Service Hours',font=('bold',12))
hours.grid(row=2,column=0) #positioning the label accordingly in the GUI

#Creating text boxes for user to enter data
eid=StringVar()
e_id=Entry(service_hours_frame,textvariable=eid)
e_id.grid(row=0,column=1) #positioning the text box accordingly in the GUI

#Dropdown box for list of project categories
pid=StringVar()
pid=ttk.Combobox(service_hours_frame,textvariable=pid,width=17)
pid['values']=getAllCategoryIDsInCB() #Get all the project categories into the combo box/drop down
pid.grid(row=1,column=1)

#Creating text boxes for user to enter data
hours=StringVar()
e_hours=Entry(service_hours_frame,textvariable=hours)
e_hours.grid(row=2,column=1)

#Create button to insert record in the db
insertbutton=Button(service_hours_frame,text="Add Service Hours",font=("italic",12),bg="white",command=lambda:insertHours(eid.get(),pid.get(),hours.get()))
insertbutton.grid(row=5,column=0)
#Create button to edit record in the db
updatebutton=Button(service_hours_frame,text="Update Hours",font=("italic",12),bg="white",command=lambda:updateHours(eid.get(),pid.get(),hours.get()))
updatebutton.grid(row=5,column=1)
#Create button to delete record from the db
deletebutton=Button(service_hours_frame,text="Delete Hours",font=("italic",12),bg="white",command=lambda:deleteHours(eid.get(),pid.get()))
deletebutton.grid(row=5,column=2)
#Create button to fetch single record from the db
get=Button(service_hours_frame,text="Get Student Hours",font=("italic",12),bg="white",command=lambda:getStudentHoursForTV(eid.get()))
get.grid(row=5,column=3)
#Create button to fetch all records from the db into a PDF file
get_all_student_records=Button(service_hours_frame,text="Get All Hours",font=("italic",12),bg="white",command=lambda:getAllStudentHoursForTV())
get_all_student_records.grid(row=5,column=4)

#Create Treeview to display a student's service hours when the get student hours button is clicked
service_hours_tree=ttk.Treeview(service_hours_frame,columns=("ProjectID", "ServiceHours"))
service_hours_tree.grid(row=7,column=0,columnspan=6)
service_hours_tree.heading('#0', text='Student ID')
service_hours_tree.heading("ProjectID", text='Project ID')
service_hours_tree.heading("ServiceHours", text='Service Hours')

#Service Hours Screen ends here

#Student Record Screen starts here		

#Creating labels for the form fields for user to enter data. The labels are created in compliance with ADA standards ensuring differently enabled users are able to use the system.

id = Label(student_record_frame,text='Student ID',font=('bold',12))
id.grid(row=0,column=0) #positioning the label accordingly in the GUI 

name=Label(student_record_frame,text='Student Name',font=('bold',12))
name.grid(row=1,column=0) #positioning the label accordingly in the GUI 

grade=Label(student_record_frame,text='Student Grade',font=('bold',12))
grade.grid(row=2,column=0) #positioning the label accordingly in the GUI 

#Creating text boxes for user to enter data

e_id=Entry(student_record_frame)
e_id.grid(row=0,column=1) #positioning the text box accordingly in the GUI 

#Creating text boxes for user to enter data
e_name=Entry(student_record_frame)
e_name.grid(row=1,column=1)

#Creating radio buttons for user to enter student grade

e_grade=StringVar(value="9"); #Setting a variable to hold the selected radio button value, defaulted to Grade 9

e_grade9=Radiobutton(student_record_frame,text="9  ", variable=e_grade, value="9")
e_grade10=Radiobutton(student_record_frame,text="10", variable=e_grade, value="10")
e_grade11=Radiobutton(student_record_frame,text="11", variable=e_grade, value="11")
e_grade12=Radiobutton(student_record_frame,text="12", variable=e_grade, value="12")

#Display the radio buttons one below the other
e_grade9.grid(row=2,column=1)
e_grade10.grid(row=3,column=1)
e_grade11.grid(row=4,column=1)
e_grade12.grid(row=5,column=1)

#Create button to insert record in the db
insertbutton=Button(student_record_frame,text="Add Student",font=("italic",12),bg="white",command=lambda:insertStudent(e_id.get(),e_name.get(),e_grade.get()))
insertbutton.grid(row=6,column=0)
#Create button to edit record in the db
updatebutton=Button(student_record_frame,text="Update Student",font=("italic",12),bg="white",command=lambda:updateStudent(e_id.get(),e_name.get(),e_grade.get()))
updatebutton.grid(row=6,column=1)

#Create button to delete record from the db. This button is temporarily disabled to prevent students from being deleted and losing their past service hours.
#deletebutton=Button(student_record_frame,text="Delete Student",font=("italic",12),bg="white",command=lambda:deleteStudent(e_id.get(),e_name.get()))
#deletebutton.grid(row=6,column=2)

#Create button to fetch student records from the db
get=Button(student_record_frame,text="Get All Student Records",font=("italic",12),bg="white",command=lambda:getAllStudentsForTV())
get.grid(row=6,column=2)

#Create Treeview to display all student records when the get students button is clicked
student_record_tree=ttk.Treeview(student_record_frame,columns=("StudentName", "Grade"),height=6)
student_record_tree.grid(row=7,column=0,columnspan=3)
student_record_tree.heading('#0', text='Student ID')
student_record_tree.heading("StudentName", text='Student Name')
student_record_tree.heading("Grade", text='Grade')

#Student Record Screen ends here

#Project Category Screen starts here

#Creating labels for the form fields for user to enter data. The labels are created in compliance with ADA standards ensuring differently enabled users are able to use the system.

project_id=Label(project_category_frame,text='Project Category',font=('bold',12))
project_id.grid(row=0,column=0) #positioning the label accordingly in the GUI 

#Creating text boxes for user to enter data
e_project_id=Entry(project_category_frame)
e_project_id.grid(row=0,column=1) #positioning the label accordingly in the GUI 

#Create button to insert record in the db
insertbutton=Button(project_category_frame,text="Add Project Category",font=("italic",12),bg="white",command=lambda:InsertCategories(e_project_id.get()))
insertbutton.grid(row=1,column=0) #positioning the button accordingly in the GUI 

#Create button to fetch project category records from the db
get=Button(project_category_frame,text="Get All Project Categories",font=("italic",12),bg="white",command=lambda:getAllCategoriesForTV())
get.grid(row=1,column=1)

#Create Treeview to display all project category records when the get all project categories button is clicked
project_category_tree=ttk.Treeview(project_category_frame,columns=("ProjectCategory"),height=10)
project_category_tree.grid(row=2,column=0,columnspan=4)
project_category_tree.heading('#0', text='Category ID')
project_category_tree.heading("ProjectCategory", text='Project Category')

#Project Category Screen ends here

root.option_add('*tearOff', FALSE) #Remove the Tear line that appears in the Menu

#Create Menu for the GUI window 'root'
menu=Menu(root)
root.config(menu=menu)

#File menu
file=Menu(menu)
file.add_command(label='Manage Students',command=lambda:loadStudentPage())
file.add_command(label='Manage Project Categories',command=lambda:loadProjectCategoryPage())
file.add_command(label='Manage Service Hours',command=lambda:loadServiceHoursPage())
file.add_command(label='Exit',command=root.destroy) #We can also use root.exit() command
menu.add_cascade(label='File',menu=file)

#Download menu
download=Menu(menu)
download.add_command(label='Download Report - Service Hours',command=lambda:getAllRecordsIntoPdf())
download.add_command(label='Download Report - Students',command=lambda:getAllStudentsIntoPdf())
download.add_command(label='Download Report - Project Categories',command=lambda:getAllCategoriesIntoPdf())
menu.add_cascade(label='Download',menu=download)

#Help menu
help=Menu(menu)
help.add_command(label='Help Contents',command=lambda:openhelp())
help.add_command(label='About',command=lambda:openabout())
menu.add_cascade(label='Help',menu=help)

#Initialize the application and load the service hours page on startup
loadServiceHoursPage()

#Call the function to load the project categories in the drop down
getAllCategoryIDsInCB()

#Run/activate the mainloop event
root.mainloop()