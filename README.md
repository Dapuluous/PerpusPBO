# PerpusPBO
This application is made to fulfill a pass-requirement on "Pemrograman Berbasis Obyek" subject.
Basically, this is a simple application for library management stuff written using Python. As for now, the application is still work in progress which means you will encounter some unexpected bugs so be sure to stay tuned!

# Requirements
- Python 3.7.5 or newer
- [prettytable 2.0.0](https://pypi.org/project/prettytable/)
- [MySQL Connector 8.0.22](https://dev.mysql.com/downloads/connector/python/)
- [XAMPP 7.3.5 or newer (For MySQL database)](https://www.apachefriends.org/download.html)

# How to Run
First, you need to create a file named `conn.py` and put your database credential info inside `conn.py`
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

I don't provide the .sql database until the professor has marked our project as done to avoid 100% code plagiarism among the students. You may review my code and take it as your inspiration. Good luck!

# Kelompok
- Muhammad Dhaffa Mahendra (192410103005)
- Muhammad Zufar Syah (192410103074)
