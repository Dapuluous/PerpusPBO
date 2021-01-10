from app.model.bukuModel import Buku
from app.utility import *
import pyfiglet

def bukuMenu():
	print(pyfiglet.figlet_format("E-LIB") + "===========================")
	print("1. Tambah Buku\n2. Tampilkan Buku\n3. Ubah Buku\n4. Hapus Buku\n5. Kembali")
	print("===========================")
	pilihSubMenu = int(input("Pilih Menu: "))

	clear()

	if(pilihSubMenu == 1):
		data = []
		banyakData = int(input("Masukkan banyak buku yang akan diinput: "))

		clear()

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
		print("Berhasil menyimpan data")
		input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 2):
		Buku().fetchAllBuku()
		input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 3):
		bukuNotEmpty = Buku().fetchAllBuku()

		if(bukuNotEmpty):
			idInput = int(input("Masukkan id buku yang ingin diubah: "))

			clear()
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
				print("Berhasil mengubah data")
				input("Enter untuk melanjukan...")
			else:
				clear()
				print(f"Data buku dengan ID {idInput} tidak ditemukan.")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 4):
		bukuNotEmpty = Buku().fetchAllBuku()

		if(bukuNotEmpty):
			idInput = int(input("Masukkan id buku yang ingin dihapus: "))

			clear()
			bukuExists = Buku().fetchSingleBuku(idInput)

			if(bukuExists):
				confirmationMsg = input(f"Apakah anda yakin ingin menghapus buku dengan ID {idInput}? (Y/N): ").lower()

				if(confirmationMsg == "y"):
					clear()
					Buku().deleteBuku(idInput)
					print("Berhasil menghapus data")
					input("Enter untuk melanjukan...")
				else:
					clear()
			else:
				clear()
				print(f"Data buku dengan ID {idInput} tidak ditemukan.")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	else:
		pass
