# Apa itu Kontrol Alur Program?
# kontrol alur program adalah cara untuk mengatur jalan nya program berdasarkan kondisi tertentu 
# dengan kontrol alur, program bisa mengambil keputusan dan melakukan tindakan yang berbeda tergentung pada situasi 

# Pernyataan If 
# Pernyataan if digunakan untuk menjalankan kode hanya jika kondisi tertentu bernilai true 
# Setelah if, harus ada titik dua
# Kode yang akan dijalankan jika kondisi true harus diindentasi (diberi spasi di awal)
# jika kita ingin melakukan pengkondisian pada nilai sebaliknya kita bisamenggunakan else 
# Atau jika kita ingin melakukan pengkondisian berbeda sesuai kita selain pada if, kita bisa gunakan elif
true = "Kocak"
if true == True:
    print("benar")
elif true == "Kocak":
    print("lah gajelas")
else :
    print("salah")

# Pernyataan Match Case 
# match case adalah fitur alternatif yang lebih bersih untuk kemungkinan kondisi yang banyak, jauh lebih efisien dan bersih ketimbang menggunakan elif yang banyak

hari: str = str(input("Masukan nama hari: ")).lower()
match hari :
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari biasa")
    case "sabtu" | "minggu": 
        print("Hari Libur")
    case _:
        print("Nama hari tidak valid")

# Conditional Express (Ternary Operator)
# Conditional expression memungkinkan kita menulis kondisi sederhana dalam satu baris
berhasil: str = str(input("berhasil atau tidak?")).lower()
keadaan = "Berhasil cok" if berhasil == "berhasil" else "Gagal blayy"

print(keadaan)

# python 6F.AlurProgram.py