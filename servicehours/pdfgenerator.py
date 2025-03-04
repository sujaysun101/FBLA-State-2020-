import mysql.connector as mysql
from reportlab.lib import colors, styles
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)
from reportlab import *
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import letter
import tkinter.messagebox as MessageBox #to display messages in the application indicating that actions on the db are successful

def getAllRecordsIntoPdf(): #Function to retrieve all student hour records from the database into a pdf file
		pdf = SimpleDocTemplate('Student Service Hours Report.pdf',pagesize=letter)
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
		#cursor to exucute SQL query
		cursor=con.cursor()
		#Get all student hours records from the db
		cursor.execute("select * from student_hours")

		records=cursor.fetchall()
		data = [["Student ID","Project Category ID","Service Hours"]]
		for record in records:
			#Print data retrieved from the database to test/debug
			#print (record) 
			data.append(record) #Append the data from the db to the list object created for the pdf file
		
		table=Table(data, colWidths=140, rowHeights=30, repeatRows=1)

		#Apply some styling on the table that will be displayed in the pdf
		ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.lightskyblue),("BACKGROUND",(0,0),(3,0),colors.lightskyblue), ('FONTSIZE', (0, 0), (-1, -1), 12),("BACKGROUND",(0,1),(-1,0),colors.whitesmoke)])
		table.setStyle(ts)
		data_obj=[]
		data_obj.append(table)
		pdf.build(data_obj)
		MessageBox.showinfo("Report", "PDF Report is generated and saved to your computer successfully!")
		#Close the db connection and free up resources
		con.close();

def getAllStudentsIntoPdf(): #Function to retrieve all students from the database into a pdf file
		pdf = SimpleDocTemplate('Student Report.pdf',pagesize=letter)
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
		#cursor to exucute SQL query
		cursor=con.cursor()
		#Get all students from the db
		cursor.execute("select * from student")

		students=cursor.fetchall()
		data = [["Student ID","Name ID","Grade"]]
		for student in students:
			#Print data retrieved from the database to test/debug
			#print (student) 
			data.append(student) #Append the data from the db to the list object created for the pdf file
		
		table=Table(data, colWidths=140, rowHeights=30, repeatRows=1)

		#Apply some styling on the table that will be displayed in the pdf
		ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.lightskyblue),("BACKGROUND",(0,0),(3,0),colors.lightskyblue), ('FONTSIZE', (0, 0), (-1, -1), 12),("BACKGROUND",(0,1),(-1,0),colors.whitesmoke)])
		table.setStyle(ts)
		data_obj=[]
		data_obj.append(table)
		pdf.build(data_obj)
		MessageBox.showinfo("Report", "PDF Report is generated and saved to your computer successfully!")
		#Close the db connection and free up resources
		con.close();

def getAllCategoriesIntoPdf(): #Function to retrieve all category records from the database into a pdf file
		pdf = SimpleDocTemplate('Project Categories Report.pdf',pagesize=letter)
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="StudentHours")
		#cursor to exucute SQL query
		cursor=con.cursor()
		#Get all category records from the db
		cursor.execute("select * from project_category_master")

		records=cursor.fetchall()
		data = [["Project Category ID","Category Name"]]
		for record in records:
			#Print data retrieved from the database to test/debug
			#print (record) 
			data.append(record) #Append the data from the db to the list object created for the pdf file
		
		table=Table(data, colWidths=140, rowHeights=30, repeatRows=1)

		#Apply some styling on the table that will be displayed in the pdf
		ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.lightskyblue),("BACKGROUND",(0,0),(3,0),colors.lightskyblue), ('FONTSIZE', (0, 0), (-1, -1), 12),("BACKGROUND",(0,1),(-1,0),colors.whitesmoke)])
		table.setStyle(ts)
		data_obj=[]
		data_obj.append(table)
		pdf.build(data_obj)
		MessageBox.showinfo("Report", "PDF Report is generated and saved to your computer successfully!")
		#Close the db connection and free up resources
		con.close();


