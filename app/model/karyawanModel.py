from app.config.dbManager import *

class Karyawan(QueryManagement):
	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertKaryawan(self, value):
		self.sql = "INSERT INTO tb_karyawan (username, password, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllKaryawan(self):
		self.sql = "SELECT idKaryawan, username, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level FROM tb_karyawan"
		self.val = ['ID', 'Username', 'Nama User', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Bergabung', 'Level']

		return self.executeFetchAll()

	def fetchSingleKaryawan(self, idInput):
		self.sql = "SELECT * FROM tb_karyawan WHERE idKaryawan = %s"
		self.val = (idInput,)

		return self.executeFetchSingle()

	def updateKaryawan(self, value):
		self.sql = "UPDATE tb_karyawan SET username = %s, password = %s, namaKaryawan = %s, jenisKelamin = %s, umur = %s, alamat = %s, tanggalBergabung = %s WHERE idKaryawan = %s"
		self.val = value

		self.executeCommit("Update")

	def deleteKaryawan(self, idInput):
		self.sql = "DELETE FROM tb_karyawan WHERE idKaryawan = %s"
		self.val = (idInput,)

		self.executeCommit("Delete")