from app.config.dbManager import *

class Buku(QueryManagement):
	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertBuku(self, value):
		self.sql = "INSERT INTO tb_buku (judulBuku, pengarang, penerbit, tahunTerbit, jumlahHalaman) VALUES (%s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllBuku(self):
		self.sql = "SELECT * FROM tb_buku"
		self.val = ['ID', 'Judul Buku', 'Pengarang', 'Penerbit', 'Tahun Terbit', 'Jumlah Halaman']

		return self.executeFetchAll()

	def fetchSingleBuku(self, idInput):
		self.sql = "SELECT * FROM tb_buku WHERE idBuku = %s"
		self.val = (idInput,)

		return self.executeFetchSingle()

	def updateBuku(self, value):
		self.sql = "UPDATE tb_buku SET judulBuku = %s, pengarang = %s, penerbit = %s, tahunTerbit = %s, jumlahHalaman = %s where idBuku = %s"
		self.val = value

		self.executeCommit("Update")

	def deleteBuku(self, idInput):
		self.sql = "DELETE FROM tb_buku WHERE idBuku = %s"
		self.val = (idInput,)

		self.executeCommit("Delete")