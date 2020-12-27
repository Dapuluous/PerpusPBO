from app.config.dbManager import *

class User(QueryManagement):
	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def setLogin(self, username, password):
		self.sql = "SELECT idKaryawan, namaKaryawan, level FROM tb_karyawan WHERE username = %s AND password = %s"
		self.val = (username, password)
		
		return self.executeFetchSingle()