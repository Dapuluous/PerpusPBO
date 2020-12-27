from app.config.dbManager import *

class Anggota(QueryManagement):
	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertAnggota(self, value):
		self.sql = "INSERT INTO tb_anggota (namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota) VALUES (%s, %s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllAnggota(self):
		self.sql = "SELECT * FROM tb_anggota"
		self.val = ['ID', 'Nama', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Daftar', 'Status']

		return self.executeFetchAll()

	def fetchSingleAnggota(self, idInput):
		self.sql = "SELECT * FROM tb_anggota where idAnggota = %s"
		self.val = (idInput,)

		return self.executeFetchSingle()

	def updateAnggota(self, value):
		self.sql = "UPDATE tb_anggota SET namaAnggota = %s, jenisKelamin = %s, umur = %s, alamat = %s, statusAnggota = %s where idAnggota = %s"
		self.val = value

		self.executeCommit("Update")

	def deleteAnggota(self, idInput):
		self.sql = "DELETE FROM tb_anggota WHERE idAnggota = %s"
		self.val = (idInput,)

		self.executeCommit("Delete")