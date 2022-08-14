import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", password = "Pawan@54463")
cursor = mydb.cursor()
#cursor.execute("create database aryan")
q = "create table aryan.ineuron(employee_id int (10), employee_name varchar(80), mail_id varchar(50), salary int(6), attendence int (5) )"
cursor.execute(q)

