from app.model.karyawanModel import Karyawan
from app.utility import *
import pyfiglet

def karyawanMenu():
	print(pyfiglet.figlet_format("E-LIB") + "===========================")
	print("1. Tambah Karyawan\n2. Tampilkan Karyawan\n3. Ubah Data Karyawan\n4. Hapus Data Karyawan\n5. Kembali")
	print("===========================")
	pilihSubMenu = int(input("Pilihan Menu: "))

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
		print("Berhasil menyimpan data")
		input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 2):
		Karyawan().fetchAllKaryawan()
		input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 3):
		karyawanNotEmpty = Karyawan().fetchAllKaryawan()

		if(karyawanNotEmpty):
			idInput = int(input("Masukkan id karyawan yang ingin diubah: "))

			clear()
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
				print("Berhasil mengubah data")
				input("Enter untuk melanjukan...")
			else:
				clear()
				print(f"Tidak ditemukan data karyawan dengan ID {idInput}")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 4):
		karyawanNotEmpty = Karyawan().fetchAllKaryawan()

		if(karyawanNotEmpty):
			idInput = int(input("Masukkan id karyawan yang ingin dihapus: "))

			clear()
			karyawanExists = Karyawan().fetchSingleKaryawan(idInput)
			
			if(karyawanExists):
				confirmationMsg = input(f"Apakah anda yakin ingin menghapus karyawan dengan ID {idInput}? (Y/N): ").lower()

				if(confirmationMsg == "y"):
					clear()
					Karyawan().deleteKaryawan(idInput)
					print("Berhasil menghapus data")
					input("Enter untuk melanjukan...")
				else:
					clear()
			else:
				clear()
				print(f"Tidak ditemukan data karyawan dengan ID {idInput}")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	else:
		pass