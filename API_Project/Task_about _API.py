# 1. write a program to insert a record in sql table via API database.

import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", password = "Pawan@54463")
cursor = mydb.cursor()