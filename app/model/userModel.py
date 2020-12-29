from app.config.dbManager import *

class User(QueryManagement):
	__tableName = "tb_karyawan"

	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def setLogin(self, username, password):
		self.sql = f"SELECT idKaryawan, namaKaryawan, level FROM {self.__tableName} WHERE username = %s AND password = %s"
		self.val = (username, password)
		
		return self.executeFetchSingle()