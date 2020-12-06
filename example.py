# import conn

# ===== Create Data =====
# sql = "INSERT INTO tb_buku VALUES (%s, %s, %s)"
# val = ("2", "Nama Buku2", "Dapoo3")
# conn.mycursor.execute(sql, val)

# conn.mydb.commit()

# print(conn.mycursor.rowcount, "Data berhasil disimpan")

# ===== Create Data (Input) =====
# judulBuku = input("Masukkan nama buku: ")
# pengarang = input("Masukkan nama pengarang: ")

# sql = "INSERT INTO tb_buku (judulBuku, pengarang) VALUES (%s, %s)"
# val = (judulBuku, pengarang)
# conn.mycursor.execute(sql, val)

# conn.mydb.commit()

# print(conn.mycursor.rowcount, "data berhasil disimpan")

# ===== Create Data (Multiple) =====
# sql = "INSERT INTO tb_buku (judulBuku, pengarang) VALUES (%s, %s)"
# val = [
# 	("Nama BukuA", "Dapoo3"),
# 	("Nama asd", "Dapoo3"),
# 	("Nama fdhbfd", "AS"),
# 	("Nama e32", "Dafsdfpoo3"),
# 	("Nama asd", "Daposfdso3")
# ]
# conn.mycursor.executemany(sql, val)

# conn.mydb.commit()

# print(conn.mycursor.rowcount, "data berhasil disimpan")

# ===== Create Data (Multiple Input) =====
# dataList = []
# banyakBuku = int(input("Masukkan banyak buku yang akan disimpan: "))

# for x in range(0, banyakBuku):
# 	print(f"===== Data ke {x+1} =====")
# 	judulBuku = input("Masukkan nama buku: ")
# 	pengarang = input("Masukkan nama pengarang: ")

# 	dataList.append((judulBuku, pengarang))

# sql = "INSERT INTO tb_buku (judulBuku, pengarang) VALUES (%s, %s)"
# val = dataList

# conn.mycursor.executemany(sql, val)

# conn.mydb.commit()

# print(conn.mycursor.rowcount, "data berhasil disimpan")

# ===== Read Data =====
# conn.mycursor.execute("SELECT * FROM tb_buku")

# result = conn.mycursor.fetchall()

# for x in result:
# 	print(x)

# ===== Read Data (Single Input) =====
# inputData = int(input("Masukkan id buku yang ingin dicari: "))
# whereData = (inputData,)

# sql = "SELECT * FROM tb_buku where idBuku = %s"

# conn.mycursor.execute(sql, whereData)
# result = conn.mycursor.fetchone()

# for x in result:
# 	print(x)

# ===== Delete Data (Single) =====
# conn.mycursor.execute("SELECT * FROM tb_buku")

# result = conn.mycursor.fetchall()

# for x in result:
# 	txt = (f"===== ID Buku: {x[0]} =====\n" +
# 	f"Nama Buku: {x[1]}\n" +
# 	f"Pengarang: {x[2]}")
# 	print(txt)

# inputData = int(input("Masukkan id buku yang ingin dihapus: "))
# whereData = (inputData,)

# sql = "DELETE FROM tb_buku WHERE idBuku = %s"

# conn.mycursor.execute(sql, whereData)

# conn.mydb.commit()

# print(conn.mycursor.rowcount, "data dihapus")

# ===== Update Data (Input) =====
# conn.mycursor.execute("SELECT * FROM tb_buku")

# result = conn.mycursor.fetchall()

# for x in result:
# 	txt = (f"===== ID Buku: {x[0]} =====\n" +
# 	f"Nama Buku: {x[1]}\n" +
# 	f"Pengarang: {x[2]}")
# 	print(txt)

# idBuku = int(input("Masukkan id buku yang ingin diubah: "))
# judulBuku = input("Masukkan nama buku yang baru: ")
# pengarang = input("Masukkan nama pengarang yang baru: ")

# sql = "UPDATE tb_buku SET judulBuku = %s, pengarang = %s where idBuku = %s"
# whereData = (judulBuku, pengarang, idBuku)

# conn.mycursor.execute(sql, whereData)

# conn.mydb.commit()
# print(conn.mycursor.rowcount, "data berhasil diubah") 