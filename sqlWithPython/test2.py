import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", password = "Pawan@54463")
cursor = mydb.cursor()
s = "insert into aryan.ineuron values(101, 'pawan kumar', 'pawanaryan93@gmail.com', 100, 30)"
p = "insert into aryan.ineuron values(105, 'aryan kumar', 'pawan.mehta93@gmail.com', 200, 30)"
cursor.execute(s)
cursor.execute(p)
mydb.commit()
cursor.execute("select * from aryan.ineuron")
for i in cursor.fetchall():
    print(i)