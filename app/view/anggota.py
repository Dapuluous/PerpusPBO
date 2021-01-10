from app.model.anggotaModel import Anggota
from app.utility import *
from datetime import datetime, timedelta
import pyfiglet

def anggotaMenu():
	print(pyfiglet.figlet_format("E-LIB") + "===========================")
	print("1. Tambah Anggota\n2. Tampilkan Anggota\n3. Ubah Data Anggota\n4. Hapus Data Anggota\n5. Kembali")
	print("===========================")
	pilihSubMenu = int(input("Pilihan Menu: "))

	clear()

	if(pilihSubMenu == 1):
		data = []
		banyakData = int(input("Masukkan banyak anggota yang akan diinput: "))

		for x in range(0, banyakData):
			print(f"===== Data Anggota Ke-{x+1} =====")
			namaAnggota = input("Masukkan nama anggota: ")
			jenisKelamin = input("Masukkan jenis kelamin (L/P): ").lower()
			umur = int(input("Masukkan umur: "))
			alamat = input("Masukkan alamat: ")
			tanggalDaftar = datetime.today().strftime('%Y-%m-%d')
			statusAnggota = "1"

			data.append((namaAnggota, jenisKelamin, umur, alamat, tanggalDaftar, statusAnggota))

		clear()
		Anggota().insertAnggota(data)
		print("Berhasil menyimpan data")
		input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 2):
		Anggota().fetchAllAnggota()
		input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 3):
		anggotaNotEmpty = Anggota().fetchAllAnggota()

		if(anggotaNotEmpty):
			idInput = int(input("Masukkan id anggota yang ingin diubah: "))

			clear()
			anggotaExists = Anggota().fetchSingleAnggota(idInput)
			
			if(anggotaExists):
				namaAnggota = input("Masukkan nama anggota yang baru: ")
				jenisKelamin = input("Masukkan jenis kelamin yang baru (L/P): ").lower()
				umur = int(input("Masukkan umur yang baru: "))
				alamat = input("Masukkan alamat yang baru: ")
				statusAnggota = input("Masukkan status anggota yang baru (1 = Aktif | 0 = Tidak Aktif): ")

				data = (namaAnggota, jenisKelamin, umur, alamat, statusAnggota, idInput)

				clear()
				Anggota().updateAnggota(data)
				print("Berhasil mengubah data")
				input("Enter untuk melanjukan...")
			else:
				clear()
				print(f"Tidak ditemukan data anggota dengan ID {idInput}")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 4):
		anggotaNotEmpty = Anggota().fetchAllAnggota()

		if(anggotaNotEmpty):
			idInput = int(input("Masukkan id anggota yang ingin dihapus: "))

			clear()
			anggotaExists = Anggota().fetchSingleAnggota(idInput)
			
			if(anggotaExists):
				confirmationMsg = input(f"Apakah anda yakin ingin menghapus anggota dengan ID {idInput}? (Y/N): ").lower()

				if(confirmationMsg == "y"):
					clear()
					Anggota().deleteAnggota(idInput)
					print("Berhasil menghapus data")
					input("Enter untuk melanjukan...")
				else:
					clear()
			else:
				clear()
				print(f"Tidak ditemukan data anggota dengan ID {idInput}")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	else:
		pass