import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", password = "Pawan@54463")
cursor = mydb.cursor()

#age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,y
#58,management,married,tertiary,no,2143,yes,no,unknown,5,may,261,1,-1,0,unknown,no
#44,technician,single,secondary,no,29,yes,no,unknown,5,may,151,1,-1,0,unknown,no
#33,entrepreneur,married,secondary,no,2,yes,yes,unknown,5,may,76,1,-1,0,unknown,no
#47,blue-collar,married,unknown,no,1506,yes,no,unknown,5,may,92,1,-1,0,unknown,no
#33,unknown,single,unknown,no,1,no,no,unknown,5,may,198,1,-1,0,unknown,no
#35,management,married,tertiary,no,231,yes,no,unknown,5,may,139,1,-1,0,unknown,no
#28,management,single,tertiary,no,447,yes,yes,unknown,5,may,217,1,-1,0,unknown,no
#42,entrepreneur,divorced,tertiary,yes,2,yes,no,unknown,5,may,380,1,-1,0,unknown,no