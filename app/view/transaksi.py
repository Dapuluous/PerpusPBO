from app.model.bukuModel import Buku
from app.model.anggotaModel import Anggota
from app.model.transaksiModel import Transaksi
from app.utility import *
from datetime import datetime, timedelta

def transaksiMenu(idUser, namaUser):
	print("===== Sub Menu =====")
	print("1. Tambah Data Peminjaman Buku\n2. Tampilkan Riwayat Peminjaman\n3. Pengembalian Buku\n4. Hapus Data Peminjaman")
	pilihSubMenu = int(input("Pilihan anda: "))

	clear()

	if(pilihSubMenu == 1):
		bukuNotEmpty = Buku().fetchAllBuku()

		if(bukuNotEmpty):
			idBuku = int(input("Masukkan ID buku yang ingin dipinjam: "))
		
			bukuExists = Buku().fetchSingleBuku(idBuku)

			if(bukuExists):
				anggotaNotEmpty = Anggota().fetchAllAnggota()
				idAnggota = int(input("Masukkan ID anggota yang ingin meminjam: "))
				
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
				else:
					clear()
					print(f"Tidak ditemukan data anggota dengan ID {idAnggota}")
			else:
				clear()
				print(f"Tidak ditemukan data buku dengan ID {idBuku}")
		else:
			pass
	elif(pilihSubMenu == 2):
		Transaksi().fetchAllTransaksi()
	elif(pilihSubMenu == 3):
		transaksiNotEmpty = Transaksi().fetchAllTransaksi()

		if(transaksiNotEmpty):
			idInput = int(input("Masukkan ID transaksi yang bersangkutan: "))
			transaksiExists = Transaksi().fetchSingleTransaksi(idInput)
			
			if(transaksiExists[6] == "1"):
				clear()
				print(f"Maaf, buku dengan ID {idInput} telah dikembalikan.")
			elif(transaksiExists):
				statusKembali = "1"
				data = (statusKembali, idInput)
				
				clear()
				Transaksi().updateTransaksi(data)
				Transaksi().printNota(idInput, namaUser)
			else:
				print(f"Tidak ditemukan data transaksi dengan ID {idInput}")
		else:
			pass
	elif(pilihSubMenu == 4):
		transaksiNotEmpty = Transaksi().fetchAllTransaksi()

		if(transaksiNotEmpty):
			idInput = int(input("Masukkan id transaksi yang ingin dihapus: "))
			transaksiExists = Transaksi().fetchSingleTransaksi(idInput)
			
			if(transaksiExists):
				clear()
				Transaksi().deleteTransaksi(idInput)
			else:
				clear()
				print(f"Tidak ditemukan data transaksi dengan ID {idInput}")
		else:
			pass
	else:
		pass