from app.model.anggotaModel import Anggota
from app.utility import *
from datetime import datetime, timedelta

def anggotaMenu():
	print("===== Sub Menu =====")
	print("1. Tambah Anggota\n2. Tampilkan Anggota\n3. Ubah Data Anggota\n4. Hapus Data Anggota")
	pilihSubMenu = int(input("Pilihan anda: "))

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
	elif(pilihSubMenu == 2):
		Anggota().fetchAllAnggota()
	elif(pilihSubMenu == 3):
		anggotaNotEmpty = Anggota().fetchAllAnggota()

		if(anggotaNotEmpty):
			idInput = int(input("Masukkan id anggota yang ingin diubah: "))
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
			else:
				clear()
				print(f"Tidak ditemukan data anggota dengan ID {idInput}")
		else:
			pass
	elif(pilihSubMenu == 4):
		anggotaNotEmpty = Anggota().fetchAllAnggota()

		if(anggotaNotEmpty):
			idInput = int(input("Masukkan id anggota yang ingin dihapus: "))
			anggotaExists = Anggota().fetchSingleAnggota(idInput)
			
			if(anggotaExists):
				clear()
				Anggota().deleteAnggota(idInput)
			else:
				clear()
				print(f"Tidak ditemukan data anggota dengan ID {idInput}")
		else:
			pass
	else:
		pass