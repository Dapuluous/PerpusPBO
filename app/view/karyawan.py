from app.model.karyawanModel import Karyawan
from app.utility import *

def karyawanMenu():
	print("===== Sub Menu =====")
	print("1. Tambah Karyawan\n2. Tampilkan Karyawan\n3. Ubah Data Karyawan\n4. Hapus Data Karyawan")
	pilihSubMenu = int(input("Pilihan anda: "))

	clear()

	if(pilihSubMenu == 1):
		data = []	
		banyakData = int(input("Masukkan banyak karyawan yang akan diinput: "))
		
		for x in range(0, banyakData):
			print(f"===== Data Karyawan Ke-{x+1} =====")
			username = input("Masukkan username karyawan: ")
			password = input("Masukkan password karyawan: ")
			namaKaryawan = input("Masukkan nama karyawan: ")
			jenisKelamin = input("Masukkan jenis kelamin (L/P): ").upper()
			umur = int(input("Masukkan umur: "))
			alamat = input("Masukkan alamat: ")
			tanggalBergabung = input("Masukkan tanggal bergabung (YYYY-MM-DD): ")
			level = input("Masukkan level (1 = Admin | 2 = User): ")
			hashedPassword = hashmd5(password)

			data.append((username, hashedPassword, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, level))

		clear()
		Karyawan().insertKaryawan(data)
	elif(pilihSubMenu == 2):
		Karyawan().fetchAllKaryawan()
	elif(pilihSubMenu == 3):
		karyawanNotEmpty = Karyawan().fetchAllKaryawan()

		if(karyawanNotEmpty):
			idInput = int(input("Masukkan id karyawan yang ingin diubah: "))
			karyawanExists = Karyawan().fetchSingleKaryawan(idInput)
			
			if(karyawanExists):
				username = input("Masukkan username karyawan yang baru: ")
				password = input("Masukkan password karyawan yang baru: ")
				namaKaryawan = input("Masukkan nama karyawan yang baru: ")
				jenisKelamin = input("Masukkan jenis kelamin yang baru (L/P): ").upper()
				umur = int(input("Masukkan umur yang baru: "))
				alamat = input("Masukkan alamat yang baru: ")
				tanggalBergabung = input("Masukkan tanggal bergabung yang baru (YYYY-MM-DD): ")
				level = input("Masukkan level yang baru (1 = Admin | 2 = User): ")
				hashedPassword = hashmd5(password)

				data = (username, hashedPassword, namaKaryawan, jenisKelamin, umur, alamat, tanggalBergabung, idInput)

				clear()
				Karyawan().updateKaryawan(data)
			else:
				clear()
				print(f"Tidak ditemukan data karyawan dengan ID {idInput}")
		else:
			pass
	elif(pilihSubMenu == 4):
		karyawanNotEmpty = Karyawan().fetchAllKaryawan()

		if(karyawanNotEmpty):
			idInput = int(input("Masukkan id buku yang ingin dihapus: "))
			karyawanExists = Karyawan().fetchSingleKaryawan(idInput)
			
			if(karyawanExists):
				clear()
				Karyawan().deleteKaryawan(idInput)
			else:
				clear()
				print(f"Tidak ditemukan data karyawan dengan ID {idInput}")
		else:
			pass
	else:
		pass