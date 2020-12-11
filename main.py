import conn
import os
import platform
from prettytable import PrettyTable
from datetime import datetime, timedelta
import datetime

if(platform.system() == "Windows"):
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')

class Buku:
	def executeMenu(self):
		print("===== Sub Menu =====")
		print("1. Tambah Buku\n2. Tampilkan Buku\n3. Ubah Data Buku\n4. Hapus Data Buku")
		pilihSubMenu = int(input("Pilihan anda: "))
		
		clear()

		if(pilihSubMenu == 1):
			self.addBook()
		elif(pilihSubMenu == 2):
			self.fetchBook()
		elif(pilihSubMenu == 3):
			self.updateBook()
		elif(pilihSubMenu == 4):
			self.deleteBook()
		else:
			print("Pilihan tidak valid")
	def addBook(self):
		dataList = []
		banyakData = int(input("Masukkan banyak data buku yang akan diinput: "))

		for x in range(0, banyakData):
			print(f"===== Data ke {x+1} =====")
			judulBuku = input("Masukkan judul buku: ")
			pengarang = input("Masukkan nama pengarang: ")
			penerbit = input("Masukkan nama penerbit: ")

			dataList.append((judulBuku, pengarang, penerbit))

		sql = "INSERT INTO tb_buku (judulBuku, pengarang, penerbit) VALUES (%s, %s, %s)"
		val = dataList

		conn.mycursor.executemany(sql, val)

		conn.mydb.commit()

		print(conn.mycursor.rowcount, "data berhasil disimpan")
	def fetchBook(self):
		conn.mycursor.execute("SELECT * FROM tb_buku")

		result = conn.mycursor.fetchall()

		if(len(result) == 0):
			print("Tidak ada data ditemukan")
		else:
			table = PrettyTable(['ID', 'Judul Buku', 'Pengarang', 'Penerbit'])

			for x in range (0, len(result)):
				idBuku, judulBuku, pengarang, penerbit = result[x]
				table.add_row([idBuku, judulBuku, pengarang, penerbit])

			print(table)

		return result
	def fetchBookSingle(self, idBuku):
		whereData = (idBuku,)
		sql = "SELECT * FROM tb_buku where idBuku = %s"

		conn.mycursor.execute(sql, whereData)
		return conn.mycursor.fetchone()
	def updateBook(self):
		dataExist = self.fetchBook()
		
		if(dataExist):
			idBuku = int(input("Masukkan id buku yang ingin diubah: "))
			result = self.fetchBookSingle(idBuku)

			if(result):
				judulBuku = input("Masukkan judul buku yang baru: ")
				pengarang = input("Masukkan nama pengarang yang baru: ")
				penerbit = input("Masukkan nama penerbit yang baru: ")

				sql = "UPDATE tb_buku SET judulBuku = %s, pengarang = %s, penerbit = %s where idBuku = %s"
				whereData = (judulBuku, pengarang, penerbit, idBuku)

				conn.mycursor.execute(sql, whereData)

				conn.mydb.commit()
				print(conn.mycursor.rowcount, "data berhasil diubah")
			else:
				print("Tidak ditemukan data berdasarkan hasil pencarian")
	def deleteBook(self):
		dataExist = self.fetchBook()

		if(dataExist):
			inputData = int(input("Masukkan id buku yang ingin dihapus: "))
			result = self.fetchBookSingle(inputData)
			
			if(result):
				whereData = (inputData,)
				sql = "DELETE FROM tb_buku WHERE idBuku = %s"

				conn.mycursor.execute(sql, whereData)

				conn.mydb.commit()

				print(conn.mycursor.rowcount, "data dihapus")
			else:
				print("Tidak ditemukan data berdasarkan hasil pencarian")

class Karyawan:
	def executeMenu(self):
		print("===== Sub Menu =====")
		print("1. Tambah Karyawan\n2. Tampilkan Karyawan\n3. Ubah Data Karyawan\n4. Hapus Data Karyawan")
		pilihSubMenu = int(input("Pilihan anda: "))
		
		clear()

		if(pilihSubMenu == 1):
			self.addKaryawan()
		elif(pilihSubMenu == 2):
			self.fetchKaryawan()
		elif(pilihSubMenu == 3):
			self.updateKaryawan()
		elif(pilihSubMenu == 4):
			self.deleteKaryawan()
		else:
			print("Pilihan tidak valid")
	def addKaryawan(self):
		dataList = []
		banyakData = int(input("Masukkan banyak data karyawan yang akan diinput: "))

		for x in range(0, banyakData):
			print(f"===== Data ke {x+1} =====")
			namaKaryawan = input("Masukkan nama karyawan: ")
			jenisKelamin = input("Masukkan jenis kelamin (L/P): ").lower()
			umur = int(input("Masukkan umur: "))
			alamat = input("Masukkan alamat: ")
			tanggalBergabung = input("Masukkan tanggal bergabung (YYYY-MM-DD): ")

			dataList.append((namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung))

		sql = "INSERT INTO tb_karyawan (namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung) VALUES (%s, %s, %s, %s, %s)"
		val = dataList

		conn.mycursor.executemany(sql, val)

		conn.mydb.commit()

		print(conn.mycursor.rowcount, "data berhasil disimpan")
	def fetchKaryawan(self):
		conn.mycursor.execute("SELECT * FROM tb_karyawan")

		result = conn.mycursor.fetchall()

		if(len(result) == 0):
			print("Tidak ada data ditemukan")
		else:
			table = PrettyTable(['ID', 'Nama Karyawan', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Bergabung'])

			for x in range (0, len(result)):
				idBuku, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung = result[x]
				table.add_row([idBuku, namaKaryawan, jenisKelamin.upper(), umur, alamat, tanggalBergabung])

			print(table)

		return result
	def fetchKaryawanSingle(self, idKaryawan):
		whereData = (idKaryawan,)
		sql = "SELECT * FROM tb_karyawan where idKaryawan = %s"

		conn.mycursor.execute(sql, whereData)
		return conn.mycursor.fetchone()
	def updateKaryawan(self):
		dataExist = self.fetchKaryawan()

		if(dataExist):
			idKaryawan = int(input("Masukkan id karyawan yang ingin diubah: "))
			result = self.fetchKaryawanSingle(idKaryawan)

			if(result):
				namaKaryawan = input("Masukkan nama karyawan yang baru: ")
				jenisKelamin = input("Masukkan jenis kelamin yang baru (L/P): ").lower()
				umur = int(input("Masukkan umur yang baru: "))
				alamat = input("Masukkan alamat yang baru: ")
				tanggalBergabung = input("Masukkan tanggal bergabung yang baru (YYYY-MM-DD): ")

				sql = "UPDATE tb_karyawan SET namaKaryawan = %s, jenisKelamin = %s, umur = %s, alamat = %s, tanggalBergabung = %s where idKaryawan = %s"
				whereData = (namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, idKaryawan)

				conn.mycursor.execute(sql, whereData)

				conn.mydb.commit()
				print(conn.mycursor.rowcount, "data berhasil diubah")
			else:
				print("Tidak ditemukan data berdasarkan hasil pencarian")
	def deleteKaryawan(self):
		dataExist = self.fetchKaryawan()

		if(dataExist):
			inputData = int(input("Masukkan id karyawan yang ingin dihapus: "))
			result = self.fetchKaryawanSingle(inputData)

			if(result):
				whereData = (inputData,)
				sql = "DELETE FROM tb_karyawan WHERE idKaryawan = %s"

				conn.mycursor.execute(sql, whereData)

				conn.mydb.commit()

				print(conn.mycursor.rowcount, "data dihapus")
			else:
				print("Tidak ditemukan data berdasarkan hasil pencarian")

class Anggota:
	def executeMenu(self):
		print("===== Sub Menu =====")
		print("1. Tambah Anggota\n2. Tampilkan Anggota\n3. Ubah Data Anggota\n4. Hapus Data Anggota")
		pilihSubMenu = int(input("Pilihan anda: "))
		
		clear()

		if(pilihSubMenu == 1):
			self.addAnggota()
		elif(pilihSubMenu == 2):
			self.fetchAnggota()
		elif(pilihSubMenu == 3):
			self.updateAnggota()
		elif(pilihSubMenu == 4):
			self.deleteAnggota()
		else:
			print("Pilihan tidak valid")
	def addAnggota(self):
		dataList = []
		banyakData = int(input("Masukkan banyak data anggota yang akan diinput: "))

		for x in range(0, banyakData):
			print(f"===== Data ke {x+1} =====")
			namaAnggota = input("Masukkan nama anggota: ")
			jenisKelamin = input("Masukkan jenis kelamin (L/P): ").lower()
			umur = int(input("Masukkan umur: "))
			alamat = input("Masukkan alamat: ")
			tanggalDaftar = datetime.today().strftime('%Y-%m-%d')
			statusAnggota = "1"

			dataList.append((namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota))

		sql = "INSERT INTO tb_anggota (namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota) VALUES (%s, %s, %s, %s, %s, %s)"
		val = dataList

		conn.mycursor.executemany(sql, val)

		conn.mydb.commit()

		print(conn.mycursor.rowcount, "data berhasil disimpan")
	def fetchAnggota(self):
		conn.mycursor.execute("SELECT * FROM tb_anggota")

		result = conn.mycursor.fetchall()

		if(len(result) == 0):
			print("Tidak ada data ditemukan")
		else:
			table = PrettyTable(['ID', 'Nama', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Daftar', 'Status'])

			for x in range (0, len(result)):
				idAnggota, namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota = result[x]

				if(statusAnggota == "1"):
					statusAnggota = "Aktif"
				else:
					statusAnggota = "Tidak Aktif"

				table.add_row([idAnggota, namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota])

			print(table)
			
		return result
	def fetchAnggotaSingle(self, idAnggota):
		whereData = (idAnggota,)
		sql = "SELECT * FROM tb_anggota where idAnggota = %s"

		conn.mycursor.execute(sql, whereData)
		return conn.mycursor.fetchone()
	def updateAnggota(self):
		dataExist = self.fetchAnggota()

		if(dataExist):
			idAnggota = int(input("Masukkan id anggota yang ingin diubah: "))
			result = self.fetchAnggotaSingle(idAnggota)

			if(result):
				namaAnggota = input("Masukkan nama anggota yang baru: ")
				jenisKelamin = input("Masukkan jenis kelamin yang baru (L/P): ").lower()
				umur = int(input("Masukkan umur yang baru: "))
				alamat = input("Masukkan alamat yang baru: ")
				statusAnggota = str(input("Masukkan status anggota yang baru (1 (Aktif)/0 (Tidak Aktif): "))

				sql = "UPDATE tb_anggota SET namaAnggota = %s, jenisKelamin = %s, umur = %s, alamat = %s, statusAnggota = %s where idAnggota = %s"
				whereData = (namaAnggota, jenisKelamin, umur, alamat, statusAnggota, idAnggota)

				conn.mycursor.execute(sql, whereData)

				conn.mydb.commit()
				print(conn.mycursor.rowcount, "data berhasil diubah")
			else:
				print("Tidak ditemukan data berdasarkan hasil pencarian")
	def deleteAnggota(self):
		dataExist = self.fetchAnggota()

		if(dataExist):
			inputData = int(input("Masukkan id anggota yang ingin dihapus: "))
			result = self.fetchAnggotaSingle(inputData)

			if(result):
				whereData = (inputData,)
				sql = "DELETE FROM tb_anggota WHERE idAnggota = %s"

				conn.mycursor.execute(sql, whereData)

				conn.mydb.commit()

				print(conn.mycursor.rowcount, "data dihapus")
			else:
				print("Tidak ditemukan data berdasarkan hasil pencarian")

class Transaksi:
	def executeMenu(self):
		print("===== Sub Menu =====")
		print("1. Tambah Data Peminjaman Buku\n2. Tampilkan Riwayat Peminjaman\n3. Pengembalian Buku\n4. Hapus Data Peminjaman")
		pilihSubMenu = int(input("Pilihan anda: "))
		
		clear()

		if(pilihSubMenu == 1):
			self.addTransaksi()
		elif(pilihSubMenu == 2):
			self.fetchTransaksi()
		elif(pilihSubMenu == 3):
			self.returnBook()
		elif(pilihSubMenu == 4):
			self.deleteTransaksi()
		else:
			print("Pilihan tidak valid")
	def addTransaksi(self):
		dataList = []

		Buku().fetchBook()
		idBuku = int(input("Masukkan ID buku yang ingin dipinjam: "))
		Anggota().fetchAnggota()
		idAnggota = int(input("Masukkan ID anggota yang ingin meminjam: "))
		Karyawan().fetchKaryawan()
		idKaryawan = int(input("Masukkan ID karyawan yang menangani transaksi: "))
		tanggalPinjam = datetime.datetime.today().strftime('%Y-%m-%d')

		initialDate = datetime.datetime.strptime(str(tanggalPinjam), '%Y-%m-%d')
		modifiedDate = initialDate + timedelta(days=3)

		tanggalKembali = datetime.datetime.strftime(modifiedDate, '%Y-%m-%d')
		statusKembali = "0"

		dataList.append((idBuku, idAnggota, idKaryawan, tanggalPinjam, tanggalKembali, statusKembali))

		sql = "INSERT INTO tb_transaksi (idBuku, idAnggota, idKaryawan, tanggalPinjam, tanggalKembali, statusKembali) VALUES (%s, %s, %s, %s, %s, %s)"
		val = dataList

		conn.mycursor.executemany(sql, val)

		conn.mydb.commit()

		print(conn.mycursor.rowcount, "data berhasil disimpan")
	def fetchTransaksi(self):
		conn.mycursor.execute("SELECT d.idTransaksi, a.judulBuku, b.namaAnggota, c.namaKaryawan, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM tb_transaksi d INNER JOIN tb_buku a using(idBuku)  INNER JOIN tb_anggota b using(idAnggota) INNER JOIN tb_karyawan c using(idKaryawan)")

		result = conn.mycursor.fetchall()

		if(len(result) == 0):
			print("Tidak ada data ditemukan")
		else:
			table = PrettyTable(['ID', 'Judul Buku', 'Nama Anggota', 'Petugas Yang Melayani', 'Tanggal Pinjam', 'Tanggal Kembali', 'Status Peminjaman'])

			for x in range (0, len(result)):
				idTransaksi, judulBuku, namaAnggota, namaKaryawan, tanggalPinjam, tanggalKembali, statusKembali = result[x]

				if(statusKembali == "1"):
					statusKembali = "Sudah Kembali"
				else:
					statusKembali = "Belum Kembali"

				table.add_row([idTransaksi, judulBuku, namaAnggota, namaKaryawan, tanggalPinjam, tanggalKembali, statusKembali])

			print(table)

		return result
	def fetchTransaksiSingle(self, idTransaksi):
		whereData = (idTransaksi,)
		sql = "SELECT d.idTransaksi, a.judulBuku, b.namaAnggota, c.namaKaryawan, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM tb_transaksi d INNER JOIN tb_buku a using(idBuku)  INNER JOIN tb_anggota b using(idAnggota) INNER JOIN tb_karyawan c using(idKaryawan) where idTransaksi = %s"

		conn.mycursor.execute(sql, whereData)
		return conn.mycursor.fetchone()
	def returnBook(self):
		self.fetchTransaksi()
		idTransaksi = int(input("Masukkan ID transaksi yang bersangkutan: "))
		statusKembali = str(input("Masukkan status kembali (1 (Sudah Kembali)/0 (Belum Kembali): "))

		sql = "UPDATE tb_transaksi SET statusKembali = %s where idTransaksi = %s"

		whereData = (statusKembali, idTransaksi)

		conn.mycursor.execute(sql, whereData)

		conn.mydb.commit()

		self.notaTransaksi(idTransaksi)
	def deleteTransaksi(self):
		dataExist = self.fetchTransaksi()

		if(dataExist):
			inputData = int(input("Masukkan id transaksi yang ingin dihapus: "))
			result = self.fetchTransaksiSingle(inputData)

			if(result):
				whereData = (inputData,)
				sql = "DELETE FROM tb_transaksi WHERE idTransaksi = %s"

				conn.mycursor.execute(sql, whereData)

				conn.mydb.commit()

				print(conn.mycursor.rowcount, "data dihapus")
			else:
				print("Tidak ditemukan data berdasarkan hasil pencarian")
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
	def notaTransaksi(self, idTransaksi):
		result = self.fetchTransaksiSingle(idTransaksi)

		clear()

		txt = print("========== Nota ===========" +
		f'\nJudul Buku: {result[1]}' +
		f'\nNama: {result[2]}' +
		f'\nDenda: Rp {self.countDenda(str(result[4]), str(result[5]))}' +
		f"\n\nTerima kasih sudah mengembalikan buku perpustakaan. Semoga harimu menyenangkan ^_^" +
		f"\nTertanda Petugas,\n{result[3]}" +
		"\n===========================")

		return txt
def main():
	try:
		while True:
			print("===== Menu Utama =====")
			print("1. Manajemen Buku\n2. Manajemen Karyawan\n3. Manajemen Anggota Perpustakaan\n4. Manajemen Peminjaman\nInputkan selain angka 1 hingga 4 untuk keluar dari aplikasi")
			pilihMenuUtama = int(input("Pilihan anda: "))

			clear()

			if(pilihMenuUtama == 1):
				Buku().executeMenu()
			elif(pilihMenuUtama == 2):
				Karyawan().executeMenu()
			elif(pilihMenuUtama == 3):
				Anggota().executeMenu()
			elif(pilihMenuUtama == 4):
				Transaksi().executeMenu()
			else:
				print("Selamat Tinggal")
				return False
	except:
		clear()
		lanjutMenu = input("Terdapat kesalahan dalam input. Inputkan apa saja untuk melanjutkan: ")

		if(lanjutMenu):
			main()
		else:
			exit()


if __name__ == "__main__":
	clear()
	main()