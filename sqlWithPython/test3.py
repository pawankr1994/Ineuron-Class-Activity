import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "Pawan@54463")
cursor = mydb.cursor()
cursor.execute("select employee_id, employee_name from aryan.ineuron")
l = []
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))