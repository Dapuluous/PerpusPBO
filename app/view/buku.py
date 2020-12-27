from app.model.bukuModel import Buku
from app.utility import *

def bukuMenu():
	print("Silahkan pilih menu: ")
	print("1. Tambah Buku\n2. Tampilkan Buku\n3. Ubah Buku\n4. Hapus Buku")
	pilihSubMenu = int(input("Pilih Menu: "))

	clear()

	if(pilihSubMenu == 1):
		data = []
		banyakData = int(input("Masukkan banyak buku yang akan diinput: "))

		for x in range(0, banyakData):
			print(f"===== Data Buku Ke-{x+1} =====")
			judulBuku = input("Masukkan judul buku: ")
			pengarang = input("Masukkan nama pengarang: ")
			penerbit = input("Masukkan nama penerbit: ")
			tahunTerbit = input("Masukkan tahun terbit: ")
			jumlahHalaman = input("Masukkan jumlah halaman: ")

			data.append((judulBuku, pengarang, penerbit, tahunTerbit, jumlahHalaman))

		clear()
		Buku().insertBuku(data)
	elif(pilihSubMenu == 2):
		Buku().fetchAllBuku()
	elif(pilihSubMenu == 3):
		bukuNotEmpty = Buku().fetchAllBuku()

		if(bukuNotEmpty):
			idInput = int(input("Masukkan id buku yang ingin diubah: "))
			bukuExists = Buku().fetchSingleBuku(idInput)

			if(bukuExists):
				judulBuku = input("Masukkan judul buku yang baru: ")
				pengarang = input("Masukkan nama pengarang yang baru: ")
				penerbit = input("Masukkan nama penerbit yang baru: ")
				tahunTerbit = input("Masukkan tahun terbit yang baru: ")
				jumlahHalaman = input("Masukkan jumlah halaman yang baru: ")

				data = (judulBuku, pengarang, penerbit, tahunTerbit, jumlahHalaman, idInput)

				clear()
				Buku().updateBuku(data)
			else:
				clear()
				print(f"Data buku dengan ID {idInput} tidak ditemukan.")
		else:
			pass
	elif(pilihSubMenu == 4):
		bukuNotEmpty = Buku().fetchAllBuku()

		if(bukuNotEmpty):
			idInput = int(input("Masukkan id buku yang ingin dihapus: "))
			bukuExists = Buku().fetchSingleBuku(idInput)

			if(bukuExists):
				clear()
				Buku().deleteBuku(idInput)
			else:
				clear()
				print(f"Data buku dengan ID {idInput} tidak ditemukan.")
		else:
			pass
	else:
		pass
