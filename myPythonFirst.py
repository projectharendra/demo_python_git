import mysql.connector

mydb = mysql.connector.connect(auth_plugin='mysql_native_password',host="localhost",user='sa',password="Passw0rd",database="demo_db");
mycursor = mydb.cursor()

#mycursor.execute("show databases")

mycursor.execute("select * from student")
#result = mycursor.fetchall()
result = mycursor.fetchone()
for i in result:
	print(i)