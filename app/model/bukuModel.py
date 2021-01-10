from app.config.dbManager import *

class Buku(QueryManagement):
	__tableName = "tb_buku"

	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertBuku(self, value):
		self.sql = f"INSERT INTO {self.__tableName} (judulBuku, pengarang, penerbit, tahunTerbit, jumlahHalaman) VALUES (%s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllBuku(self):
		self.sql = f"SELECT * FROM {self.__tableName}"
		self.val = ['ID', 'Judul Buku', 'Pengarang', 'Penerbit', 'Tahun Terbit', 'Jumlah Halaman']

		return self.executeFetchAll()

	def fetchSingleBuku(self, idInput):
		self.sql = f"SELECT * FROM {self.__tableName} WHERE idBuku = %s"
		self.val = (idInput,)
		self.val2 = ['ID', 'Judul Buku', 'Pengarang', 'Penerbit', 'Tahun Terbit', 'Jumlah Halaman']

		return self.executeFetchSinglePrint()

	def updateBuku(self, value):
		self.sql = f"UPDATE {self.__tableName} SET judulBuku = %s, pengarang = %s, penerbit = %s, tahunTerbit = %s, jumlahHalaman = %s where idBuku = %s"
		self.val = value

		self.executeCommit()

	def deleteBuku(self, idInput):
		self.sql = f"DELETE FROM {self.__tableName} WHERE idBuku = %s"
		self.val = (idInput,)

		self.executeCommit()