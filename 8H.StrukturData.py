# Struktur Data:
# Data structures (struktur data) adalah acrauntuk menyimpan data mengorganisir data dalam program 
# sejauh ini kita sudah belajar menyimpan satu nilai dalam satu variabel 
# Sekarang ktia akan belajar cara menyimpan banyak nilai sekaligus 

# List
# List adalah kumpulan data yang bisa menyimpan banyak nilai dalam satu variable 
# List ditulis dengan menggunakan kurung siku

# Manipulasi List
# Mengakses List, sama seperti string, list menggunakan index yang dimulai dari 0
# Mengubah elemen list, bisa menggunakan index dan ubah seperti mengubah variabel 
# Menambah Elemen ke list, bisa menggunakan method append(data) untuk menambahkan diakhir, dan insert(index, data) untuk menambahkan data setelah index 
# Menghapus elemen dari list, bisa menggunakan method remove(index), atau method pop() untuk menghapus elemen terakhir 
# Untuk menghitung panjang list, kita bisa menggunakan function len(list)
# List juga bisa digabungkan dengan list lain seperti string menggunakan operator + (tambah)
# List juga sama seperti string, bisa di iterasi menggunakan for loop
nama_nama:list[str] = []

# Untuk memasukan nilai ke dalam list
nama_nama.append("Faiz")
nama_nama.append("Hannan")
nama_nama.append("Hakim")

for nama in nama_nama:
    print(nama)

# untuk menghapus suatu nilai di dalam list
nama_nama.remove("Hannan")

for nama in nama_nama:
    print(nama)

# Untuk menghapus data paling belakang dan mengembalikan nya
nama_paling_belakang = nama_nama.pop()

print(nama_paling_belakang)


for nama in nama_nama:
    print(nama)

if "Faiz" in nama_nama :
    print("Ada Faiz")


# Tuple 
# Tuple mirip dengan list, tetapi tidak bisa diubah setelah dibuat, Tuple ditulis dengan kurung biasa 
# Untuk membuat tuple, kita bisa buat langsung menggunakan kurung, misal(satu, dua, tiga), kita bisa buat data bebas berapapun yang kita mau 
# Untuk mengakses data di tuple, sama seperti di list dan string, kita bisa menggunakan index dengan kurung kotak 
# Tuple tidak bisa diubah setelah dibuat, jadi tidak ada oeprasi untuk mengubah atau menghapus data di tuple 
# Untuk mengetahui panjang tuple, kita bisa gunakan function len(tuple) sama seperti  di list, kita juga bisa melakukan iterasi di tuple 

point: tuple[int] = (10, 11, 12)
print(point[0]) 
print(point[1])

for angka in point :
    print("Ini angka di tuple", angka)

if 11 in point :
    print("ada kok")

# Dictionary
# Dictionary menyimpan data dalam pasangan key-value (kunci-nilai). Dictionary ditulis dengan kurung kurawal {}
# Untuk membuat data dictionary, kita perlu menentukan key dan juga valuenya 
# Key di dictionary bisa tipe data seperti string, integer, float, boolean, namun biasanay kebanyakan orang menggunakan string untuk key nya 
# Untuk mengakses dan mengubah value di dictionary, kita bisa gunakan key dengan kurung kotak, seperti di list 
# Untuk menghapus value di dictionary, kita bisa gunakan kata kunci dengan delete sama seperti di list 
# Untuk mengetahui panjang dictionary, kita bisa gunakan len(dictionary)
# Dictionary juga bisa di iterasi menggunakan perulangan for sama seperti list, akan mengembalikan key dan value nya 

siswa = {
    "Nama": "Faiz",
    "Nilai" : 100,
    "Kelas": "203"
}

print(siswa)

del(siswa["Kelas"]) # Untuk menghapus

for key, nilai in siswa.items():
    print("Key: ", key)
    print("Value: ", nilai)


# Set
# Set adalah kumpulan data yang tidak berurutan dan tidak memiliki elemen duplikat
# Set ditulis dengan kurung kurawal {} atau fungsi set
# Untuk menambah data ke set, kita bisa gunakan method add(value)
# Untuk menghapus data di set, kita bisa gunakan method remove(value)
# Karena data di set tidak duplicate dan tidak berurutan, maka tidak bisa diakses menggunakan index 
# Untuk mengakses data di set, biasanya menggnakan for

buah = {"Apel", "Jeruk", "Pisang"}
print(buah)

buah.add("Mangga")
print(buah)

buah.remove("Pisang")
print(buah)

for i in buah:
    print(i)


# python 8H.StrukturData.py

