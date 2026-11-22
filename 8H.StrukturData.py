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

# python 8H.StrukturData.py

