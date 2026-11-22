# Perulangan:
# Perulangan (loop) adalah cara untuk menjalankan kode yang sama berulang kali.
# Dengan perulangan, kita bisa menghemat waktu dan membuat kode lebih efisien daripada menulis kode yang sama berkali kali

# For loop
# For Loop digunakan untuk mengulang kode sejumlah tertentu atau mengitersi melalui sekumpulan data 
# For Loop biasanya menggunakan function range() untuk membuat urutan angka untuk perulangan nya

# mencetak angka 0 smpai 4
for i in range(5):
    print("Perulangan ke: " + str(i))

# mencetak angka 1 smpai 5
for i in range(1, 6):
    print("Perulangan ke: " + str(i))

# mencetak hitung mundur
for i in range(5, 0, -1):
    print("Perulangan ke: " + str(i))

# For Loop dengan String 
# For loop juga bisa digunakan untuk mengiterasi setiap karakter dalam string

nama = "Faiz Hannan Hakim"
def cetak_nama(nama: str): 
    for n in nama:
        if (n == " "):
            continue
        print(n)

cetak_nama(nama)

# While Loop
# While Loop mengulang kode salam kondisi tertentu masih true
ulang = True 
angka = 0
while (ulang):
    print(angka)
    angka += 1
    if (angka == 21):
        ulang = False
# python 7G.Perulangan.py