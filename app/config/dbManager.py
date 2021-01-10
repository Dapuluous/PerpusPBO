import mysql.connector
from prettytable import PrettyTable

class Database:
	def __init__(self):
		try:
			self.mydb = mysql.connector.connect (
				host = "localhost",
				user = "root",
				password = "",
				database = "pythonpbo"
			)

			self.mycursor = self.mydb.cursor()
		except:
			print("No database server detected. Please ensure you have your database server running!")
			exit()

class QueryManagement(Database):
	def __init__(self, sql=None, val=None, val2=None):
		Database.__init__(self)
		self.sql = sql
		self.val = val
		self.val2 = val2

	def executeInsert(self):
		self.mycursor.executemany(self.sql, self.val)
		self.mydb.commit()

	def executeFetchAll(self):
		self.mycursor.execute(self.sql)
		result = self.mycursor.fetchall()

		if(len(result) == 0):
			print("Tidak ada data ditemukan.")
		else:
			table = PrettyTable(self.val)

			for x in range (0, len(result)):
				dataList = []

				for y in range(0, len(result[0])):
					dataList.append(result[x][y])
				
				table.add_row(dataList)

			print(table)
			return result

	def executeFetchSingle(self):
		self.mycursor.execute(self.sql, self.val)
		return self.mycursor.fetchone()

	def executeFetchSinglePrint(self):
		self.mycursor.execute(self.sql, self.val)
		result = self.mycursor.fetchone()

		dataList = []

		if(len(result) == 0):
			print("Tidak ada data ditemukan.")
		else:
			table = PrettyTable(self.val2)
			for x in range (0, len(result)):
				dataList.append(result[x])
			
			table.add_row(dataList)
			print(table)

		return result

	def executeCommit(self):
		self.mycursor.execute(self.sql, self.val)
		self.mydb.commit()