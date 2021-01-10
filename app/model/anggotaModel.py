from app.config.dbManager import *

class Anggota(QueryManagement):
	__tableName = "tb_anggota"

	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertAnggota(self, value):
		self.sql = f"INSERT INTO {self.__tableName} (namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota) VALUES (%s, %s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllAnggota(self):
		self.sql = f"SELECT * FROM {self.__tableName}"
		self.val = ['ID', 'Nama', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Daftar', 'Status']

		return self.executeFetchAll()

	def fetchSingleAnggota(self, idInput):
		self.sql = f"SELECT * FROM {self.__tableName} where idAnggota = %s"
		self.val = (idInput,)
		self.val2 = ['ID', 'Nama', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Daftar', 'Status']

		return self.executeFetchSinglePrint()

	def updateAnggota(self, value):
		self.sql = f"UPDATE {self.__tableName} SET namaAnggota = %s, jenisKelamin = %s, umur = %s, alamat = %s, statusAnggota = %s where idAnggota = %s"
		self.val = value

		self.executeCommit()

	def deleteAnggota(self, idInput):
		self.sql = f"DELETE FROM {self.__tableName} WHERE idAnggota = %s"
		self.val = (idInput,)

		self.executeCommit()