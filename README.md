# PerpusPBO
This application is made to fulfill a pass-requirement on "Pemrograman Berbasis Obyek" subject.
Basically, this is a simple application for library management stuff written using Python. As for now, the application is still work in progress which means you will encounter some unexpected bugs so be sure to stay tuned!

# Requirements
- Python 3.7.5 or newer
- [prettytable 2.0.0](https://pypi.org/project/prettytable/)
- [MySQL Connector 8.0.22](https://dev.mysql.com/downloads/connector/python/)
- [XAMPP 7.3.5 or newer (For MySQL database)](https://www.apachefriends.org/download.html)

# How to Run
First, you need to create a file named `conn.py` and put your database credential info inside the `conn.py`
```py
import mysql.connector

mydb = mysql.connector.connect (
	host = "yourHostName",
	user = "yourUserName",
	password = "yourDbPassword",
	database = "yourSelectedDatabase"
)

mycursor = mydb.cursor()
```
The .sql code is yet to come. I will put it eventually.
