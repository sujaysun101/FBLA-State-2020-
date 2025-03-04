CREATE DATABASE ServiceHours;

CREATE TABLE Student (
  student_id INT(16) PRIMARY KEY,
  student_name VARCHAR(255) NOT NULL,
student_grade INT(16) NOT NULL
);

CREATE TABLE Project_category_master (
  category_id INT(16) PRIMARY KEY AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL
);

CREATE TABLE Student_hours (
  student_id INT(16) NOT NULL,
  category_id INT(16) NOT NULL,
service_hours double NOT NULL,
Foreign Key (student_id) REFERENCES Student(student_id),
Foreign Key (category_id) REFERENCES Project_category_master(category_id));