import conn
import os
import platform
from prettytable import PrettyTable
from datetime import datetime, timedelta
import datetime
import hashlib

if(platform.system() == "Windows"):
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')

loginSession = []

clear()

class QueryManagement:
	def __init__(self, sql = None, val = None):
		self.sql = sql
		self.val = val

	def executeInsert(self):
		conn.mycursor.executemany(self.sql, self.val)
		conn.mydb.commit()
		
		print(conn.mycursor.rowcount, "data berhasil disimpan")

	def executeFetchAll(self):
		conn.mycursor.execute(self.sql)
		result = conn.mycursor.fetchall()

		if(len(result) == 0):
			print("Tidak ada data ditemukan")
		else:
			table = PrettyTable(self.val)

			for x in range (0, len(result)):
				dataList = []

				for y in range(0, len(result[0])):
					dataList.append(result[x][y])
				
				table.add_row(dataList)

			print(table)

		return result

	def executeFetchSingle(self):
		conn.mycursor.execute(self.sql, self.val)
		return conn.mycursor.fetchone()

	def executeCommit(self, commitType):
		conn.mycursor.execute(self.sql, self.val)
		conn.mydb.commit()

		if(commitType == "Update"):
			msg = "diubah"
		else:
			msg = "dihapus"

		print(conn.mycursor.rowcount, f"data berhasil {msg}")

	def executeNota(self, namaPetugas):
		clear()

		conn.mycursor.execute(self.sql, self.val)
		result = conn.mycursor.fetchone()

		column = ['Judul Buku', 'Nama', 'Denda (Rp)', 'Petugas']

		dataList = [result[1], result[2], self.countDenda(str(result[4]), str(result[5])), namaPetugas]
		
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

class Akun(QueryManagement):
	def __init__(self):
		QueryManagement.__init__(self, sql, val)

	def login(username, password):
		sql = "SELECT idKaryawan, namaKaryawan, level FROM tb_karyawan WHERE username = %s AND password = %s"
		val = (username, password)

		return QueryManagement(sql, val).executeFetchSingle()
class Main(QueryManagement):
	def __init__(self):
		QueryManagement.__init__(self, sql, val)

	def fetchAllData(choiceType):
		if(choiceType == "Book"):
			sql = "SELECT * FROM tb_buku"
			val = ['ID', 'Judul Buku', 'Pengarang', 'Penerbit']
		elif(choiceType == "Karyawan"):
			sql = "SELECT idKaryawan, username, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung FROM tb_karyawan WHERE level = '2'"
			val = ['ID', 'Username', 'Nama Karyawan', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Bergabung']
		elif(choiceType == "Anggota"):
			sql = "SELECT * FROM tb_anggota"
			val = ['ID', 'Nama', 'Jenis Kelamin', 'Umur', 'Alamat', 'Tanggal Daftar', 'Status']
		else:
			sql = "SELECT d.idTransaksi, a.judulBuku, b.namaAnggota, c.namaKaryawan, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM tb_transaksi d INNER JOIN tb_buku a using(idBuku)  INNER JOIN tb_anggota b using(idAnggota) INNER JOIN tb_karyawan c using(idKaryawan)"
			val = ['ID', 'Judul Buku', 'Nama Anggota', 'Petugas Yang Melayani', 'Tanggal Pinjam', 'Tanggal Kembali', 'Status Kembali']

		return QueryManagement(sql, val).executeFetchAll()

	def fetchSingleItem(idInput, choiceType):
		if(choiceType == "Book"):
			sql = "SELECT * FROM tb_buku where idBuku = %s"
		elif(choiceType == "Karyawan"):
			sql = "SELECT * FROM tb_karyawan where idKaryawan = %s"
		elif(choiceType == "Anggota"):
			sql = "SELECT * FROM tb_anggota where idAnggota = %s"
		else:
			sql = "SELECT d.idTransaksi, a.judulBuku, b.namaKaryawan, c.namaAnggota, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM tb_transaksi d INNER JOIN tb_buku a using(idBuku) INNER JOIN tb_karyawan b using(idKaryawan) INNER JOIN tb_Anggota c using(idAnggota) where idTransaksi = %s"

		val = (idInput,)
		return QueryManagement(sql, val).executeFetchSingle()

while True:
	if(len(loginSession) == 0):
		print("====== Login ======")
		username = input("Masukkan username: ")
		password = input("Masukkan password: ")

		passwordHashed = hashlib.md5(password.encode('utf-8')).hexdigest()

		session = Akun.login(username, passwordHashed)

		if(session):
			for x in range(0, len(session)):
				loginSession.append(session[x])

			clear()
		else:
			print("Username atau password salah")
	else:
		print("===== Menu Utama =====")
		print("1. Manajemen Buku\n2. Manajemen Karyawan\n3. Manajemen Anggota Perpustakaan\n4. Manajemen Peminjaman\nInputkan selain angka 1 hingga 4 untuk keluar dari aplikasi")
		pilihMenuUtama = int(input("Pilihan anda: "))

		clear()

		if(pilihMenuUtama == 1):
			print("===== Sub Menu =====")
			print("1. Tambah Buku\n2. Tampilkan Buku\n3. Ubah Data Buku\n4. Hapus Data Buku")
			pilihSubMenu = int(input("Pilihan anda: "))
			
			clear()

			if(pilihSubMenu == 1):
				judulBuku = input("Masukkan judul buku: ")
				pengarang = input("Masukkan nama pengarang: ")
				penerbit = input("Masukkan nama penerbit: ")

				dataList = []
				dataList.append((judulBuku, pengarang, penerbit))

				sql = "INSERT INTO tb_buku (judulBuku, pengarang, penerbit) VALUES (%s, %s, %s)"
				val = dataList

				QueryManagement(sql, val)
				Main().executeInsert()
			elif(pilihSubMenu == 2):
				Main.fetchAllData("Book")
			elif(pilihSubMenu == 3):
				dataExist = Main.fetchAllData("Book")

				if(dataExist):
					idInput = int(input("Masukkan id buku yang ingin diubah: "))
					checkData = Main.fetchSingleItem(idInput, "Book")
					
					if(checkData):
						judulBuku = input("Masukkan judul buku yang baru: ")
						pengarang = input("Masukkan nama pengarang yang baru: ")
						penerbit = input("Masukkan nama penerbit yang baru: ")

						sql = "UPDATE tb_buku SET judulBuku = %s, pengarang = %s, penerbit = %s where idBuku = %s"
						val = (judulBuku, pengarang, penerbit, idInput)

						QueryManagement(sql, val)
						Main().executeCommit("Update")
					else:
						print(f"Tidak ditemukan data buku dengan ID {idInput}")
				else:
					print("Data buku tidak ditemukan. Silahkan untuk menginputkan beberapa data buku terlebih dahulu.")
			elif(pilihSubMenu == 4):
				dataExist = Main.fetchAllData("Book")

				if(dataExist):
					idInput = int(input("Masukkan id buku yang ingin dihapus: "))
					checkData = Main.fetchSingleItem(idInput, "Book")
					
					if(checkData):
						sql = "DELETE FROM tb_buku WHERE idBuku = %s"
						val = (idInput,)

						QueryManagement(sql, val)
						Main().executeCommit("Delete")
					else:
						print(f"Tidak ditemukan data buku dengan ID {idInput}")
				else:
					print("Data buku tidak ditemukan. Silahkan untuk menginputkan beberapa data buku terlebih dahulu.")
		elif(pilihMenuUtama == 2):
			print("===== Sub Menu =====")
			print("1. Tambah Karyawan\n2. Tampilkan Karyawan\n3. Ubah Data Karyawan\n4. Hapus Data Karyawan")
			pilihSubMenu = int(input("Pilihan anda: "))
			
			clear()

			if(pilihSubMenu == 1):
				username = input("Masukkan username karyawan: ")
				password = input("Masukkan password karyawan: ")
				namaKaryawan = input("Masukkan nama karyawan: ")
				jenisKelamin = input("Masukkan jenis kelamin (L/P): ").upper()
				umur = int(input("Masukkan umur: "))
				alamat = input("Masukkan alamat: ")
				tanggalBergabung = input("Masukkan tanggal bergabung (YYYY-MM-DD): ")

				level = "2"
				passwordHashed = hashlib.md5(password.encode('utf-8')).hexdigest()

				dataList = []
				dataList.append((username, passwordHashed, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level))

				sql = "INSERT INTO tb_karyawan (username, password, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
				val = dataList

				QueryManagement(sql, val)
				Main().executeInsert()
			elif(pilihSubMenu == 2):
				Main.fetchAllData("Karyawan")
			elif(pilihSubMenu == 3):
				dataExist = Main.fetchAllData("Karyawan")

				if(dataExist):
					idInput = int(input("Masukkan id karyawan yang ingin diubah: "))
					checkData = Main.fetchSingleItem(idInput, "Karyawan")
					
					if(checkData):
						username = input("Masukkan username karyawan yang baru: ")
						password = input("Masukkan password karyawan yang baru: ")
						namaKaryawan = input("Masukkan nama karyawan yang baru: ")
						jenisKelamin = input("Masukkan jenis kelamin yang baru (L/P): ").upper()
						umur = int(input("Masukkan umur yang baru: "))
						alamat = input("Masukkan alamat yang baru: ")
						tanggalBergabung = input("Masukkan tanggal bergabung yang baru (YYYY-MM-DD): ")

						passwordHashed = hashlib.md5(password.encode('utf-8')).hexdigest()

						sql = "UPDATE tb_karyawan SET username = %s, password = %s, namaKaryawan = %s, jenisKelamin = %s, umur = %s, alamat = %s, tanggalBergabung = %s, level = %s WHERE idKaryawan = %s"
						val = (username, passwordHashed, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level, idInput)

						QueryManagement(sql, val)
						Main().executeCommit("Update")
					else:
						print(f"Tidak ditemukan data karyawan dengan ID {idInput}")
				else:
					print("Data karyawan tidak ditemukan. Silahkan untuk menginputkan beberapa data karyawan terlebih dahulu.")
			elif(pilihSubMenu == 4):
				dataExist = Main.fetchAllData("Karyawan")

				if(dataExist):
					idInput = int(input("Masukkan id karyawan yang ingin dihapus: "))
					checkData = Main.fetchSingleItem(idInput, "Karyawan")
					
					if(checkData):
						sql = "DELETE FROM tb_karyawan WHERE idKaryawan = %s"
						val = (idInput,)

						QueryManagement(sql, val)
						Main().executeCommit("Delete")
					else:
						print(f"Tidak ditemukan data karyawan dengan ID {idInput}")
				else:
					print("Data karyawan tidak ditemukan. Silahkan untuk menginputkan beberapa data karyawan terlebih dahulu.")
		elif(pilihMenuUtama == 3):
			print("===== Sub Menu =====")
			print("1. Tambah Anggota\n2. Tampilkan Anggota\n3. Ubah Data Anggota\n4. Hapus Data Anggota")
			pilihSubMenu = int(input("Pilihan anda: "))
			
			clear()

			if(pilihSubMenu == 1):
				namaAnggota = input("Masukkan nama anggota: ")
				jenisKelamin = input("Masukkan jenis kelamin (L/P): ").lower()
				umur = int(input("Masukkan umur: "))
				alamat = input("Masukkan alamat: ")
				tanggalDaftar = datetime.datetime.today().strftime('%Y-%m-%d')
				statusAnggota = "1"

				dataList = []
				dataList.append((namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota))

				sql = "INSERT INTO tb_anggota (namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota) VALUES (%s, %s, %s, %s, %s, %s)"
				val = dataList

				QueryManagement(sql, val)
				Main().executeInsert()
			elif(pilihSubMenu == 2):
				Main.fetchAllData("Anggota")
			elif(pilihSubMenu == 3):
				dataExist = Main.fetchAllData("Anggota")

				if(dataExist):
					idInput = int(input("Masukkan id anggota yang ingin diubah: "))
					checkData = Main.fetchSingleItem(idInput, "Anggota")
					
					if(checkData):
						namaAnggota = input("Masukkan nama anggota yang baru: ")
						jenisKelamin = input("Masukkan jenis kelamin yang baru (L/P): ").lower()
						umur = int(input("Masukkan umur yang baru: "))
						alamat = input("Masukkan alamat yang baru: ")
						statusAnggota = str(input("Masukkan status anggota yang baru (1 (Aktif)/0 (Tidak Aktif): "))

						sql = "UPDATE tb_anggota SET namaAnggota = %s, jenisKelamin = %s, umur = %s, alamat = %s, statusAnggota = %s where idAnggota = %s"
						val = (namaAnggota, jenisKelamin, umur, alamat, statusAnggota, idInput)

						QueryManagement(sql, val)
						Main().executeCommit("Update")
					else:
						print(f"Tidak ditemukan data anggota dengan ID {idInput}")
				else:
					print("Data anggota tidak ditemukan. Silahkan untuk menginputkan beberapa data anggota terlebih dahulu.")
			elif(pilihSubMenu == 4):
				dataExist = Main.fetchAllData("Anggota")

				if(dataExist):
					idInput = int(input("Masukkan id anggota yang ingin dihapus: "))
					checkData = Main.fetchSingleItem(idInput, "Anggota")
					
					if(checkData):
						sql = "DELETE FROM tb_anggota WHERE idAnggota = %s"
						val = (idInput,)

						QueryManagement(sql, val)
						Main().executeCommit("Delete")
					else:
						print("Tidak ditemukan data berdasarkan hasil pencarian")
		elif(pilihMenuUtama == 4):
			print("===== Sub Menu =====")
			print("1. Tambah Data Peminjaman Buku\n2. Tampilkan Riwayat Peminjaman\n3. Pengembalian Buku\n4. Hapus Data Peminjaman")
			pilihSubMenu = int(input("Pilihan anda: "))
			clear()

			if(pilihSubMenu == 1):
				bookCheck = Main.fetchAllData("Book")
				idBuku = int(input("Masukkan ID buku yang ingin dipinjam: "))
				bookExists = Main.fetchSingleItem(idBuku, "Book")

				if(bookCheck and bookExists):
					anggotaCheck = Main.fetchAllData("Anggota")
					idAnggota = int(input("Masukkan ID anggota yang ingin meminjam: "))
					anggotaExists = Main.fetchSingleItem(idAnggota, "Anggota")

					if(anggotaCheck and anggotaExists):
						tanggalPinjam = datetime.datetime.today().strftime('%Y-%m-%d')
						initialDate = datetime.datetime.strptime(str(tanggalPinjam), '%Y-%m-%d')
						modifiedDate = initialDate + timedelta(days=3)
						tanggalKembali = datetime.datetime.strftime(modifiedDate, '%Y-%m-%d')
						statusKembali = "0"

						dataList = []
						dataList.append((idBuku, idAnggota, loginSession[0], tanggalPinjam, tanggalKembali, statusKembali))

						sql = "INSERT INTO tb_transaksi (idBuku, idAnggota, idKaryawan, tanggalPinjam, tanggalKembali, statusKembali) VALUES (%s, %s, %s, %s, %s, %s)"
						val = dataList

						QueryManagement(sql, val)
						Main().executeInsert()
					else:
						print(f"Tidak ditemukan data anggota dengan ID {idAnggota}")
				else:
					print(f"Tidak ditemukan data buku dengan ID {idBuku}")
			elif(pilihSubMenu == 2):
				Main.fetchAllData("Transaksi")
			elif(pilihSubMenu == 3):
				dataExist = Main.fetchAllData("Transaksi")

				if(dataExist):
					idInput = int(input("Masukkan ID transaksi yang bersangkutan: "))
					statusKembali = "1"
					checkData = Main.fetchSingleItem(idInput, "Transaksi")
					
					if(checkData):
						sql = "UPDATE tb_transaksi SET statusKembali = %s where idTransaksi = %s"
						val = (statusKembali, idInput)

						QueryManagement(sql, val)
						Main().executeCommit("Update")

						sql = "SELECT d.idTransaksi, a.judulBuku, b.namaAnggota, c.namaKaryawan, d.tanggalPinjam, d.tanggalKembali, d.statusKembali FROM tb_transaksi d INNER JOIN tb_buku a using(idBuku)  INNER JOIN tb_anggota b using(idAnggota) INNER JOIN tb_karyawan c using(idKaryawan) where idTransaksi = %s"
						val = (idInput,)

						QueryManagement(sql, val)
						Main().executeNota(loginSession[1])
					else:
						print(f"Tidak ditemukan data transaksi dengan ID {idInput}")
				else:
					print("Data anggota tidak ditemukan. Silahkan untuk menginputkan beberapa data anggota terlebih dahulu.")
			elif(pilihSubMenu == 4):
				dataExist = Main.fetchAllData("Anggota")

				if(dataExist):
					idInput = int(input("Masukkan id anggota yang ingin dihapus: "))
					checkData = Main.fetchSingleItem(idInput, "Anggota")
					
					if(checkData):
						sql = "DELETE FROM tb_anggota WHERE idAnggota = %s"
						val = (idInput,)

						QueryManagement(sql, val)
						Main().executeCommit("Delete")
					else:
						print(f"Tidak ditemukan data transaksi dengan ID {idInput}")
				else:
					print("Data transaksi tidak ditemukan. Silahkan untuk menginputkan beberapa data transaksi terlebih dahulu.")
			else:
				print("Pilihan tidak valid.")
		else:
			print("Selamat Tinggal")
			exit()