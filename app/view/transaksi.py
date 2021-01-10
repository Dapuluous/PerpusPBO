from app.model.bukuModel import Buku
from app.model.anggotaModel import Anggota
from app.model.transaksiModel import Transaksi
from app.utility import *
from datetime import datetime, timedelta
import pyfiglet

def transaksiMenu(idUser, namaUser):
	print(pyfiglet.figlet_format("E-LIB") + "===========================")
	print("1. Tambah Data Peminjaman Buku\n2. Tampilkan Riwayat Peminjaman\n3. Pengembalian Buku\n4. Hapus Data Peminjaman\n5. Kembali")
	print("===========================")
	pilihSubMenu = int(input("Pilihan Menu: "))

	clear()

	if(pilihSubMenu == 1):
		bukuNotEmpty = Buku().fetchAllBuku()

		if(bukuNotEmpty):
			idBuku = int(input("Masukkan ID buku yang ingin dipinjam: "))
			
			clear()
			bukuExists = Buku().fetchSingleBuku(idBuku)
			clear()

			if(bukuExists):
				anggotaNotEmpty = Anggota().fetchAllAnggota()
				idAnggota = int(input("Masukkan ID anggota yang ingin meminjam: "))
				
				clear()
				anggotaExists = Anggota().fetchSingleAnggota(idAnggota)

				if(anggotaExists):
					tanggalPinjam = datetime.today().strftime('%Y-%m-%d')
					initialDate = datetime.strptime(str(tanggalPinjam), '%Y-%m-%d')
					modifiedDate = initialDate + timedelta(days=3)
					tanggalKembali = datetime.strftime(modifiedDate, '%Y-%m-%d')
					statusKembali = "0"

					data = []
					data.append((idBuku, idAnggota, idUser, tanggalPinjam, tanggalKembali, statusKembali))

					clear()
					Transaksi().insertTransaksi(data)
					print("Berhasil menyimpan data")
					input("Enter untuk melanjukan...")
				else:
					clear()
					print(f"Tidak ditemukan data anggota dengan ID {idAnggota}")
					input("Enter untuk melanjukan...")
			else:
				clear()
				print(f"Tidak ditemukan data buku dengan ID {idBuku}")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 2):
		Transaksi().fetchAllTransaksi()
		input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 3):
		transaksiNotEmpty = Transaksi().fetchAllTransaksi()

		if(transaksiNotEmpty):
			idInput = int(input("Masukkan ID transaksi yang bersangkutan: "))

			clear()
			transaksiExists = Transaksi().fetchSingleTransaksi(idInput)
			
			if(transaksiExists[6] == "1"):
				clear()
				print(f"Maaf, buku dengan ID {idInput} telah dikembalikan.")
				input("Enter untuk melanjukan...")
			elif(transaksiExists):
				statusKembali = "1"
				data = (statusKembali, idInput)

				confirmationMsg = input(f"Apakah anda yakin ingin memproses transaksi dengan ID {idInput}? (Y/N): ").lower()
				
				if(confirmationMsg == "y"):
					Transaksi().updateTransaksi(data)
					clear()
					Transaksi().printNota(idInput, namaUser)
					input("Enter untuk melanjukan...")
				else:
					clear()
			else:
				clear()
				print(f"Tidak ditemukan data transaksi dengan ID {idInput}")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	elif(pilihSubMenu == 4):
		transaksiNotEmpty = Transaksi().fetchAllTransaksi()

		if(transaksiNotEmpty):
			idInput = int(input("Masukkan id transaksi yang ingin dihapus: "))

			clear()
			transaksiExists = Transaksi().fetchSingleTransaksi(idInput)
			
			if(transaksiExists):
				confirmationMsg = input(f"Apakah anda yakin ingin menghapus transaksi dengan ID {idInput}? (Y/N): ").lower()

				if(confirmationMsg == "y"):
					clear()
					Transaksi().deleteTransaksi(idInput)
					print("Berhasil menghapus data")
					input("Enter untuk melanjukan...")
				else:
					clear()
			else:
				clear()
				print(f"Tidak ditemukan data transaksi dengan ID {idInput}")
				input("Enter untuk melanjukan...")
		else:
			input("Enter untuk melanjukan...")
	else:
		pass