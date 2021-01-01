from app.config.dbManager import *
from datetime import datetime, timedelta
import datetime

class Transaksi(QueryManagement):
	__tableName = "tb_transaksi"
	__tableName2 = "tb_buku"
	__tableName3 = "tb_anggota"
	__tableName4 = "tb_karyawan"

	def __init__(self, sql=None, val=None):
		QueryManagement.__init__(self, sql, val)

	def insertTransaksi(self, value):
		self.sql = f"INSERT INTO {self.__tableName} (idBuku, idAnggota, idKaryawan, tanggalPinjam, tanggalKembali, statusKembali) VALUES (%s, %s, %s, %s, %s, %s)"
		self.val = value

		self.executeInsert()

	def fetchAllTransaksi(self):
		self.sql = f"SELECT d.idTransaksi, a.judulBuku, b.namaAnggota, c.namaKaryawan, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM {self.__tableName} d INNER JOIN {self.__tableName2} a using(idBuku) INNER JOIN {self.__tableName3} b using(idAnggota) INNER JOIN {self.__tableName4} c using(idKaryawan)"
		self.val = ['ID', 'Judul Buku', 'Nama Anggota', 'Petugas Yang Melayani', 'Tanggal Pinjam', 'Tanggal Kembali', 'Status Kembali']

		return self.executeFetchAll()

	def fetchSingleTransaksi(self, idInput):
		self.sql = f"SELECT d.idTransaksi, a.judulBuku, b.namaKaryawan, c.namaAnggota, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM {self.__tableName} d INNER JOIN {self.__tableName2} a using(idBuku) INNER JOIN {self.__tableName4} b using(idKaryawan) INNER JOIN {self.__tableName3} c using(idAnggota) where idTransaksi = %s"
		self.val = (idInput,)

		return self.executeFetchSingle()

	def updateTransaksi(self, value):
		self.sql = f"UPDATE {self.__tableName} SET statusKembali = %s where idTransaksi = %s"
		self.val = value

		self.executeCommit("Update")

	def deleteTransaksi(self, idInput):
		self.sql = f"DELETE FROM {self.__tableName} WHERE idTransaksi = %s"
		self.val = (idInput,)

		self.executeCommit("Delete")

	def printNota(self, idInput, namaUser):
		self.fetchSingleTransaksi(idInput)
		result = self.executeFetchSingle()

		column = ['Judul Buku', 'Nama', 'Denda (Rp)', 'Petugas']
		dataList = [result[1], result[2], self.countDenda(str(result[4]), str(result[5])), namaUser]

		table = PrettyTable(column)		
		table.add_row(dataList)

		print(table)
		print("Terima kasih telah berkunjung ke perpustakaan!")

	def countDenda(self, tanggalPinjamInit, tanggalKembaliInit):
		tanggalSekarangInit = str(datetime.datetime.today().strftime('%Y-%m-%d'))

		year, month, day = map(int, tanggalPinjamInit.split('-'))
		year2, month2, day2 = map(int, tanggalKembaliInit.split('-'))
		year3, month3, day3 = map(int, tanggalSekarangInit.split('-'))

		tanggalPinjam = datetime.date(year, month, day)
		tanggalKembali = datetime.date(year2, month2, day2)
		tanggalSekarang = datetime.date(year3, month3, day3)

		jumlahHariTerlambat = tanggalKembali - tanggalPinjam
		
		patokanDenda = tanggalSekarang - tanggalKembali

		if(jumlahHariTerlambat.days >= 3):
			denda = patokanDenda.days * 3000	
		else:
			denda = 0

		return denda