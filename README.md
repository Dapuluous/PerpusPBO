# PerpusPBO
This application is made to fulfill a pass-requirement on "Pemrograman Berbasis Obyek" subject.
Basically, this is a simple application for library management stuff written using Python. As for now, the application is still work in progress which means you will encounter some unexpected bugs so be sure to stay tuned!

# Requirements
- Python 3.7.5 or newer
- [prettytable 2.0.0](https://pypi.org/project/prettytable/)
- [MySQL Connector 8.0.22](https://dev.mysql.com/downloads/connector/python/)
- [XAMPP 7.3.5 or newer (For MySQL database)](https://www.apachefriends.org/download.html)

# How to Run
- Make sure all requirements above were installed in your device.
- Open XAMPP then start `Apache` & `MySQL`
- Open `conn.py` and edit the code according to your database credential.
```py
import mysql.connector

try:
	mydb = mysql.connector.connect (
		host = "yourHostname",
		user = "yourDBUsername",
		password = "yourDBPassword",
		database = "yourDatabaseName"
	)
	
	mycursor = mydb.cursor()
except:
	print("No database server detected. Please ensure you have your database server running!")
	exit()
```
- Create a database with `pythonpbo` as the name and import the tables using the provided .sql `(pythonpbo.sql)`

# Kelompok
- Muhammad Dhaffa Mahendra (192410103005)
- Muhammad Zufar Syah (192410103074)
