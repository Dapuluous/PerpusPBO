from app.config.dbManager import *
from datetime import datetime, timedelta
import datetime

class Transaksi(QueryManagement):
	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertTransaksi(self, value):
		self.sql = "INSERT INTO tb_transaksi (idBuku, idAnggota, idKaryawan, tanggalPinjam, tanggalKembali, statusKembali) VALUES (%s, %s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllTransaksi(self):
		self.sql = "SELECT d.idTransaksi, a.judulBuku, b.namaAnggota, c.namaKaryawan, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM tb_transaksi d INNER JOIN tb_buku a using(idBuku) INNER JOIN tb_anggota b using(idAnggota) INNER JOIN tb_karyawan c using(idKaryawan)"
		self.val = ['ID', 'Judul Buku', 'Nama Anggota', 'Petugas Yang Melayani', 'Tanggal Pinjam', 'Tanggal Kembali', 'Status Kembali']

		return self.executeFetchAll()

	def fetchSingleTransaksi(self, idInput):
		self.sql = "SELECT d.idTransaksi, a.judulBuku, b.namaKaryawan, c.namaAnggota, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM tb_transaksi d INNER JOIN tb_buku a using(idBuku) INNER JOIN tb_karyawan b using(idKaryawan) INNER JOIN tb_Anggota c using(idAnggota) where idTransaksi = %s"
		self.val = (idInput,)

		return self.executeFetchSingle()

	def updateTransaksi(self, value):
		self.sql = "UPDATE tb_transaksi SET statusKembali = %s where idTransaksi = %s"
		self.val = value

		self.executeCommit("Update")

	def deleteTransaksi(self, idInput):
		self.sql = "DELETE FROM tb_transaksi WHERE idTransaksi = %s"
		self.val = (idInput,)

		self.executeCommit("Delete")

	def printNota(self, idInput, namaUser):
		self.fetchSingleTransaksi(idInput)
		result = self.executeFetchSingle()

		column = ['Judul Buku', 'Nama', 'Denda (Rp)', 'Petugas']
		dataList = [result[1], result[2], self.countDenda(str(result[4]), str(result[5])), namaUser]

		table = PrettyTable(column)		
		table.add_row(dataList)

		print("+------------------ Nota -------------------+")
		print(table)
		print("Terima kasih telah berkunjung ke perpustakaan!")
		print("+------------------ Nota -------------------+")

	def countDenda(self, tanggalPinjamInit, tanggalKembaliInit):
		year, month, day = map(int, tanggalPinjamInit.split('-'))
		year2, month2, day2 = map(int, tanggalKembaliInit.split('-'))

		self.tanggalPinjam = datetime.date(year, month, day)
		self.tanggalKembali = datetime.date(year2, month2, day2)

		jumlahHariTerlambat = self.tanggalKembali - self.tanggalPinjam

		if(jumlahHariTerlambat.days > 3):
			denda = (jumlahHariTerlambat.days - 3) * 1000	
		else:
			denda = 0

		return denda