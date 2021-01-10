# Requirements
- Python 3.7.5 or newer
- [Pyglet 1.15.4](https://pypi.org/project/pyglet/)
```pip install pyglet```
- [prettytable 2.0.0](https://pypi.org/project/prettytable/)
```pip install prettytable```
- [MySQL Connector 8.0.22](https://dev.mysql.com/downloads/connector/python/)
```pip install mysql-connector-python```
- [XAMPP 7.3.5 or newer (For MySQL database)](https://www.apachefriends.org/download.html)

# How to Run
- Make sure all requirements above were installed in your device. or just install `XAMPP` then open terminal/cmd then type `pip install -r requirement.txt`
- Open XAMPP then start `Apache` & `MySQL`
- Edit `dbManager.py` according to your database credential. This file can be found in `app/config/dbManager.py`
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
