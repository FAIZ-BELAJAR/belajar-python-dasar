# Operator :
# Operator adalah simbol yang digunakan untuk melakukan operasi pada avriable dan nilai, python memiliki beberapa jenis operator yang bisa kita gunakan untuk memanipulasi data 
# Operator aritmatika digunakan untuk melakukan operasi matematika 
# Operator dasar, seperti +(tambah), -(kurang), *(kali), /(bagi)
# Operator pembagian bulat dan modulo, seperti // (pembagian bulat), % (modulo || sisa pembagian)
# Operator pangkat, seperti **(pangkat)

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

# Operator Assignment
# Operator assignment digunakan untuk memberikan nilai pada variabel, seperti yang sudah pernah kita bahas, menggunakan tanda = (sama dengan)
# Compound Assinment, yaitu operator yang menggabungkan operasi aritmatika dengan assinment 

masukan_pada_variabel_ini = 10
masukan_pada_variabel_ini += 20
print(masukan_pada_variabel_ini)

# Operator Perbandingan 
# Operator Perbandingan digunakan untuk membandingkan dua nilai, hasil dari operasi ini adalah true atau false 
# == sama dengan
# > lebih besar dari 
# < lebih kecil dari 
# >= lebih besar sama dengan 
# <= lebih kecil sama dengan 
# != tidak sama dengan 

nama1 = "alice"
nama2 = "bob"
nama3 = "alice"

print(nama1 == nama3)
print(20 > 10)
print(30< 40)
print(nama3 >= "alice")
print(nama2 <= "bob")
print(nama1 != nama2)

# Operator Logika 
# Operator Logika digunakan untuk menggabungkan atau memodifikasi nilai boolean 
# and (dan), menghasilkan true jika kedua kondisi true
# or (atau), menghasilkan true jika salah satu kondisi true
# not (tidak), membalik nilai boolean

benar_atau_salah = True and True
print(benar_atau_salah)
benar_atau_salah = True or False 
print(benar_atau_salah)
benar_atau_salah = False
print(not benar_atau_salah)

# Operator String 
# Operator khusus yang dapat bekerja untuk string 
# Concatenation (+), menambah satu string dengan string lain nya 
# Repetition (*), mengulang string sejumlah angka
# Membership (in), mengecek apakah text ada dalam string 

string1 = "Penjaga satu"
string2 = "Penjaga dua"

print(string1 + string2)
print(string1 * 3)
print("Penjaga" in string1 and "Penjaga" in string2)

# Prioritas Operator 
# Operator memiliki urutan prioritas (precedence). Operator dengan prioritas lebih tinggi akan dieksekusi terlebih dulu
# Urutan Prioritas (dari tinggi ke rendah)
# ** (pangkat)
# *, /, //, % (perkalian, pembagian, pembagian bulat, modulo)
# +, - (penjumlahan, pengurangan)
# ==, !=, <, >, <= >= (operator perbandingan)
# not (logika not)
# and (logika and)
# or (logika or)

# python 5E.Operator.py