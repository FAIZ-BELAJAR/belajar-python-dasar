# Apa itu String:
# String adalaj tipe data untuk menyimpan teks atau kumpulan karakter. string ditulis dengan menggunakan tanda kutip, baik kutip tunggal (') atau kutp ganda (")
# Untuk menggabungkan strng ktia bisa menggunakan tanda + (tambah)
# Dan tipe data string tidak bisa digabungkan dengan tipe data lain seperti integer, float atau boolean, kita harus konversi dulu tipe data lain menjadi tipe data string 

nama_awal = "Faiz"
nama_tengah = "Hannan"

nama_lengkap = nama_awal + " " + nama_tengah
print(nama_lengkap)

# Gunakan len() untuk mengetahui panjang string 
print(len(nama_lengkap))

# Mengakses Karakter dalam string (indexing)
# Setiap karakter dalam string memiliki posisi (index) yang dimulai dari 0 
# Untuk mengakses tiap karakter di string, kita bisa gunakan kurung kotak dan didalm kurung kotak tersebut disebutkan posisi index nya 
# Kita juga bisa menggunakan posisi index negatif jika ingin mulai dari karakter paling belakang 

nama = "Python"
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])
print(nama[4])
print(nama[5])
print("=============================================")
print(nama[-1])
print(nama[-2])
print(nama[-3])
print(nama[-4])
print(nama[-5])
print(nama[-6])

# String Slicing 
# String slicing digunakan utnuk mengambil sebagian dari string 
# Kita bisa menggunakan kurung kotak dimana di dalam kurung kotak, terdapat 2 posisi index dipisahkan oleh :(titik dua), itu menunjukan posisi awal dan akhir karakter yang ingin kita ambil 
# Jika kita tidak sebutkan posisi index di awalm berarti akan menggunakan default nilai( nilai bawaan) yakni dengan 0
# Dan jika tidak menyebutkan posisi index di akhir, berarti akan menggunakan nilai default(nilai bawaan) dengan posisi index terakhir

print(nama[0:3])
print(nama[2:5])

# String Methods
# Tipe data string memiliki method (fungsi yang menempel pada tipe data), ada banyak sekali method yang bisa digunakan, seperti 
# upper() untuk mengubah semua karakter string menjadi huruf besar semua 
# lower() untuk mengubah semua karakter string menjadi huruf kecil semua 
# title() untuk mengubah setiap awal karakter di kata menjadi huruf besar 
# capitalize() untu mengubah awal karakter menjadi huruf besar 
# strip() untuk menghilangkan karakter kosong seperti spasi
# replace(dari, menjadi) untuk mengganti bagian tertentu dalam string 
# count(text) untuk menghitung berapa kali text muncul di dalam string 
# find(text) untuk mencari posisi text muncul

# String Interpolation 
# String iterpolation adalah cara modern untuk menggabungkan variable dengan teks
# ini lebih mudah dibaca dan lebih efisien daripada concatenaiton menggunakan +
# f-strings adalah cara terbaaru dan paling direkomendasikan untk string interpolation di python, yaitu dengan menambah huruf f, di awal ketika membuat string 
# Selanjutnya di dalam nilai string, kita bisa menggunakan kurung kurawal untuk mengakses variable lain yang ingin dimasukan atau digabungkan dengan string nya 

nama: str = "Faiz Hannan Hakim"
umur: int = 19
kota: str = "Jakarta"

profil = f"Halo, nama saya {nama} umur saya saat ini: {str(umur)}, dan saya tinggal di kota {kota.upper()}"
print(profil)
# python 4D.StringDanManipulasinya.py

