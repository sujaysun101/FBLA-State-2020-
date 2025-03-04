import mysql.connector as mysql
from reportlab import *
import tkinter.messagebox as MessageBox #to display messages in the application indicating that actions on the db are successful

#Create functions to perform different actions and execute the user stories/business requirements identified for the Student Community Hours project

#create function to insert record into the database
def insertHours(id,project_id,hours):
	try:
		
		#print (e_id)
		#print ("id: "+id)
		#Check to see all required fields are completed before inserting record into the db
		if(id=="" or project_id=="" or hours==""):
			MessageBox.showinfo("Insert records", "Please ensure all the mandatory fields are entered")
		else:
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to exucute SQL query
			cursor=con.cursor()
			#insert Student id, Name and Grade in the db
			cursor.execute("insert into student_hours values('"+id+"','"+project_id+"','"+hours+"')")
			#commit the record in the db
			cursor.execute("commit");
			MessageBox.showinfo("Insert records", "Student's service hours are entered successfully")
			con.close();
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of insert record function")

def deleteHours(student_id,category_id): #delete function to delete record from the database
	#Check to see all required fields are completed before deleting record from the db
	try:

		if(id=="" or category_id==""):
			MessageBox.showinfo("Delete records", "Please ensure the Student ID and Project Category ID fields are entered")

		elif(len(student_id.strip())!=0 and (category_id.strip())==0):
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to execute SQL query
			cursor=con.cursor()
			#delete Student record from the db
			cursor.execute("delete from student_hours where student_id='"+student_id+"'")
			#commit the delete in the db
			cursor.execute("commit");
			MessageBox.showinfo("Delete records", "Student's service hours deleted successfully")
			#Close the db connection and free up resources
			con.close();
		elif(len(student_id.strip())!=0 and (category_id.strip())!=0):
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to exucute SQL query
			cursor=con.cursor()
			#delete Student record from the db
			cursor.execute("delete from student_hours where student_id='"+student_id+"' and category_id='"+category_id+"'")
			#commit the delete in the db
			cursor.execute("commit");
			MessageBox.showinfo("Delete records", "Student's service hours deleted successfully")
			#Close the db connection and free up resources
			con.close();

	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of delete record function")


def updateHours(student_id,category_id,hours):

	try:
		#Check to see all required fields are completed before inserting student into the db
		if(student_id=="" or category_id=="" or hours==""):
			MessageBox.showinfo("Update records", "Please ensure all the mandatory fields are entered")
		else:
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to execute SQL query
			cursor=con.cursor()
			#insert Student id, Name and Community hours in the db
			cursor.execute("Update student_hours Set service_hours='"+hours+"' Where student_id='"+student_id+"' and category_id='"+category_id+"'")
			#commit the record in the db
			cursor.execute("commit");
			MessageBox.showinfo("Update records", "Student service hours updated successfully")
			con.close();
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of update record function")
	
def insertStudent(student_id,name,grade):
	try:
		#id=e_id.get();
		#name=e_name.get();
		#grade=e_grade.get();
		#Check to see all required fields are completed before inserting student into the db
		if(student_id=="" or name=="" or grade==""):
			MessageBox.showinfo("Insert student", "Please ensure all the mandatory fields are entered")
		else:
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to exucute SQL query
			cursor=con.cursor()
			#insert Student id, Name and Grade in the db
			cursor.execute("insert into student values('"+student_id+"','"+name+"','"+grade+"')")
			#commit the student in the db
			cursor.execute("commit");
			MessageBox.showinfo("Insert student", "Student entered successfully")
			con.close();
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of insert student function")

def deleteStudent(student_id,student_name): #delete function to delete student from the database
	#Check to see all required fields are completed before deleting student from the db
	try:

		if(student_id==""):
			MessageBox.showinfo("Delete student", "Please ensure the Student ID field is entered")

		elif(len(student_id.strip())!=0 and (student_name.strip())==0):
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to execute SQL query
			cursor=con.cursor()
			#delete Student from the db
			cursor.execute("delete from student where student_id='"+student_id+"'")
			#commit the delete in the db
			cursor.execute("commit");
			MessageBox.showinfo("Delete student", "Student deleted successfully")
			#Close the db connection and free up resources
			con.close();
		elif(len(student_id.strip())!=0 and (student_name.strip())!=0):
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to exucute SQL query
			cursor=con.cursor()
			#delete Student from the db
			cursor.execute("delete from student where student_id='"+student_id+"' and student_name='"+student_name+"'")
			#commit the delete in the db
			cursor.execute("commit");
			MessageBox.showinfo("Delete student", "Student deleted successfully")
			#Close the db connection and free up resources
			con.close();

	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of delete student function")


def updateStudent(student_id,name,grade):

	try:
		#hours=e_hours.get();
		#Check to see all required fields are completed before inserting record into the db
		if(id=="" or name=="" or grade==""):
			MessageBox.showinfo("Update student", "Please ensure all the mandatory fields are entered")
		else:
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to execute SQL query
			cursor=con.cursor()
			#insert Student id, Name and Grade in the db
			cursor.execute("Update student Set student_grade='"+grade+"' Where student_id='"+student_id+"' and student_name='"+name+"'")
			#commit the record in the db
			cursor.execute("commit");
			MessageBox.showinfo("Update student", "Student updated successfully")
			con.close();
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of update student function")
	

def InsertCategories(project_id):
	try:
		#project_id=e_project_id.get();
		#Check to see all required fields are completed before inserting record into the db
		if(project_id==""):
			MessageBox.showinfo("Insert category records", "Please ensure all the mandatory fields are entered")
		else:
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to exucute SQL query
			cursor=con.cursor()
			#insert Project id in the db
			cursor.execute("insert into project_category_master (category_name) values('"+project_id+"')")
			#commit the record in the db
			cursor.execute("commit");
			MessageBox.showinfo("Insert category records", "Category record is entered successfully")
			con.close();
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of insert record function")

#create function to get student hours from the database
def getStudentHours(id):
	try:
		#Check to see all required fields are completed before inserting record into the db
		if(id==""):
			MessageBox.showinfo("Get Student hours", "Please ensure the Student ID field is entered")
		else:
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
			#cursor to exucute SQL query
			cursor=con.cursor()
			#Get Student service hours from the db
			cursor.execute("select * from student_hours where student_id='"+id+"'")
			
			records=cursor.fetchall()
			
			#	Print data retrieved from the database to test/debug
			#	print (records) 
			
			con.close();
			print (records)
			return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of get student hours function")

#create function to get all student hours from the database
def getAllStudentHours():
	try:
		
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
		#cursor to exucute SQL query
		cursor=con.cursor()
		#Get Student service hours from the db
		cursor.execute("select * from student_hours")
			
		records=cursor.fetchall()
		#	Print data retrieved from the database to test/debug
		#	print (records) 
		con.close();
		print (records)
		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of get student hours function")

#create function to get all students from the database
def getAllStudents():
	try:
		
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
		#cursor to exucute SQL query
		cursor=con.cursor()
		#Get Student service hours from the db
		cursor.execute("select * from student")
			
		records=cursor.fetchall()
		#	Print data retrieved from the database to test/debug
		#	print (records) 
		con.close();
		print (records)
		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of get students function")

#create function to get all project category IDs from the database to populate the combo box in the GUI for student service hours screen
def getAllCategoryIDs():
	try:
		
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
		#cursor to exucute SQL query
		cursor=con.cursor()
		#Get Project Category ID from the db
		cursor.execute("select category_id from project_category_master")
			
		records=cursor.fetchall()
		#	Print data retrieved from the database to test/debug
		#	print (records) 
		con.close();
		print (records)
		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		print("End of get project category IDs function")

#create function to get all project categories from the database
def getAllCategories():
	try:
		
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
		#cursor to exucute SQL query
		cursor=con.cursor()
		#Get Project Categories from the db
		cursor.execute("select * from project_category_master")
			
		records=cursor.fetchall()
		#	Print data retrieved from the database to test/debug
		#	print (records) 
		print (records)
		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		print("End of get project categories function")


