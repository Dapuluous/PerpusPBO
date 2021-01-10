from app.config.dbManager import *

class Karyawan(QueryManagement):
	__tableName = "tb_karyawan"

	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertKaryawan(self, value):
		self.sql = f"INSERT INTO {self.__tableName} (username, password, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllKaryawan(self):
		self.sql = f"SELECT idKaryawan, username, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level FROM {self.__tableName}"
		self.val = ['ID', 'Username', 'Nama User', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Bergabung', 'Level']

		return self.executeFetchAll()

	def fetchSingleKaryawan(self, idInput):
		self.sql = f"SELECT idKaryawan, username, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level FROM {self.__tableName} WHERE idKaryawan = %s"
		self.val = (idInput,)
		self.val2 = ['ID', 'Username', 'Nama User', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Bergabung', 'Level']

		return self.executeFetchSinglePrint()

	def updateKaryawan(self, value):
		self.sql = f"UPDATE {self.__tableName} SET username = %s, password = %s, namaKaryawan = %s, jenisKelamin = %s, umur = %s, alamat = %s, tanggalBergabung = %s WHERE idKaryawan = %s"
		self.val = value

		self.executeCommit()

	def deleteKaryawan(self, idInput):
		self.sql = f"DELETE FROM {self.__tableName} WHERE idKaryawan = %s"
		self.val = (idInput,)

		self.executeCommit()