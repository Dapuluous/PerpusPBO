from app.config.dbManager import *
from app.model.userModel import User
from app.utility import *
from app.view.buku import bukuMenu
from app.view.karyawan import karyawanMenu
from app.view.anggota import anggotaMenu
from app.view.transaksi import transaksiMenu

class App:
	__loginSession = []

	def setCredential(self):
		checkDBConnection = Database()

		if(len(self.__loginSession) == 0):
			print("====== Login ======")
			username = input("Masukkan username: ")
			password = input("Masukkan password: ")
			hashedPassword = utility.hashmd5(password)

			loginStatus = User().setLogin(username, hashedPassword)

			utility.clear()
			
			if(loginStatus):
				for x in range(0, len(loginStatus)):
					self.__loginSession.append(loginStatus[x])

				print(f"Login sukses! Selamat datang {loginStatus[1]}!")
			else:
				print("Username atau Password salah.")
		else:
			pass

	def mainMenu(self):
		print("===== Menu Utama =====")
		print("1. Manajemen Buku\n2. Manajemen Karyawan\n3. Manajemen Anggota Perpustakaan\n4. Manajemen Peminjaman\n5. Logout\nInputkan selain 1 hingga 5 untuk keluar dari aplikasi")
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
		else:
			pass

	def run(self):
		while True:
			try:
				if(self.__loginSession):
					self.mainMenu()
				else:
					self.setCredential()
			except:
				utility.clear()
				print("Selamat tinggal!")
				exit()


		
