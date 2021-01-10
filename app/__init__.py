from app.config.dbManager import *
from app.model.userModel import User
from app.utility import *
from app.view.buku import bukuMenu
from app.view.karyawan import karyawanMenu
from app.view.anggota import anggotaMenu
from app.view.transaksi import transaksiMenu
import pyfiglet

class App:
	# Variabel private untuk menyimpan sesi login
	__loginSession = []

	# Fungsi untuk login
	def setCredential(self):
		utility.clear()

		# Jika array __loginSession kosong
		if(len(self.__loginSession) == 0):
			print(pyfiglet.figlet_format("E-LIB") + "===========================")

			username = input("Masukkan username: ")
			password = input("Masukkan password: ")
			hashedPassword = utility.hashmd5(password)

			loginStatus = User().setLogin(username, hashedPassword)

			utility.clear()
			
			# Jika login Berhasil
			if(loginStatus):
				for x in range(0, len(loginStatus)):
					self.__loginSession.append(loginStatus[x])

				print(f"Login sukses! Selamat datang {loginStatus[1]}!")
				input("Enter untuk melanjutkan...")
			else:
				print("Username atau Password salah.")
				input("Enter untuk melanjutkan...")
		else:
			pass

	# Fungsi untuk menampilkan menu
	def mainMenu(self):
		utility.clear()
		print(pyfiglet.figlet_format("E-LIB") + "===========================")
		print("1. Manajemen Buku\n2. Manajemen Karyawan\n3. Manajemen Anggota\n4. Manajemen Peminjaman\n5. Logout\n6. Exit")
		print("===========================")
		pilihMenuUtama = int(input("Pilihan anda: "))
		
		utility.clear()

		if(pilihMenuUtama == 1):
			try:
				bukuMenu()
			except:
				utility.clear()
				App().run()
		elif(pilihMenuUtama == 2):
			try:
				if(self.__loginSession[2] == "1"):
					karyawanMenu()
				else:
					print("Anda tidak punya hak untuk mengakses menu ini.")
					input("Enter untuk melanjutkan...")
			except:
				utility.clear()
				App().run()
		elif(pilihMenuUtama == 3):
			try:
				anggotaMenu()
			except:
				utility.clear()
				App().run()
		elif(pilihMenuUtama == 4):
			try:
				transaksiMenu(self.__loginSession[0], self.__loginSession[1])
			except:
				utility.clear()
				App().run()
		elif(pilihMenuUtama == 5):
			self.__loginSession = []
		
			utility.clear()
			print("Berhasil logout.")
		elif(pilihMenuUtama == 6):
			utility.clear()
			print("Selamat Tinggal")
			exit()
		else:
			pass

	def run(self):
		checkDBConnection = Database()

		if(checkDBConnection):
			while True:
				try:
					if(self.__loginSession):
						self.mainMenu()
					else:
						self.setCredential()
				except:
					utility.clear()
					print("Selamat Tinggal")
					exit()
			else:
				pass
		else:
			pass


		
