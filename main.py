import conn
import os
import platform
from prettytable import PrettyTable

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
			umur = input("Masukkan umur: ")
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
			idKaryawan = int(input("Masukkan id buku yang ingin diubah: "))
			result = self.fetchKaryawanSingle(idKaryawan)

			if(result):
				namaKaryawan = input("Masukkan nama karyawan yang baru: ")
				jenisKelamin = input("Masukkan jenis kelamin yang baru (L/P): ").lower()
				umur = input("Masukkan umur yang baru yang baru: ")
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

class Peminjaman:
	def executeMenu(self):
		print("===== Sub Menu =====")
		print("1. Tambah Data Peminjaman Buku\n2. Tampilkan Riwayat Peminjaman\n3. Pengembalian Buku\n4. Hapus Data Peminjaman")
		pilihSubMenu = int(input("Pilihan anda: "))
		
		clear()

		if(pilihSubMenu == 1):
			print("Under Maintenance")
		elif(pilihSubMenu == 2):
			print("Under Maintenance")
		elif(pilihSubMenu == 3):
			print("Under Maintenance")
		elif(pilihSubMenu == 4):
			print("Under Maintenance")
		else:
			print("Pilihan tidak valid")

def main():
	print("===== Menu Utama =====")
	print("1. Manajemen Buku\n2. Manajemen Karyawan\n3. Manajemen Peminjaman\n4. Manajemen Anggota Perpustakaan")
	pilihMenuUtama = int(input("Pilihan anda: "))

	clear()

	if(pilihMenuUtama == 1):
		Buku().executeMenu()
	elif(pilihMenuUtama == 2):
		Karyawan().executeMenu()
	elif(pilihMenuUtama == 3):
		Peminjaman().executeMenu()
	else:
		print("Under Maintenance")

if __name__ == "__main__":
	clear()
	main()