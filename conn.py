import mysql.connector

try:
	mydb = mysql.connector.connect (
		host = "localhost",
		user = "root",
		password = "",
		database = "pythonpbo"
	)
	
	mycursor = mydb.cursor()
except:
	print("No database server detected. Please ensure you have your database server running!")
	exit()