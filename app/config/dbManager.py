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
	def __init__(self, sql=None, val=None):
		Database.__init__(self)
		self.sql = sql
		self.val = val

	def executeInsert(self):
		self.mycursor.executemany(self.sql, self.val)
		self.mydb.commit()
		
		print(self.mycursor.rowcount, "data berhasil disimpan.")

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

	def executeCommit(self, commitType):
		self.mycursor.execute(self.sql, self.val)
		self.mydb.commit()

		if(commitType == "Update"):
			msg = "diubah."
		elif(commitType == "Delete"):
			msg = "dihapus."
		else:
			msg = "diapakan ya hmmm :v?"

		print(f"data berhasil {msg}")