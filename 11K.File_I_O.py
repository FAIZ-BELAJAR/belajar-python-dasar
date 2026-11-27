#  File I/O
# File I/O (Input / Output) adalah kemampuan program untuk membaca data dari file dan menulis data ke file 
# Dengan file I/O, kita bisa:
# Menyimpan data secara permanen
# Membaca data yang sudah disimpan
# Membuat laporan dalam bentuk file 
# Memproses data dari file ke eksternal
# Backup dan restore data aplikasi 

# Membuka File dan Menutup File 
# Untuk membuka file, kita bisa menggunakan function open(file, mode)
# Setelah selesai membuka file, jangan lupa tutup menggunakan method close() pada variablenya
# Saat membuka file, kita harus tentukan mode nya
# Ada 4 mode yakni
# r -> Read(baca) = digunakan untuk membaca file yang sudah ada 
# w -> Write(tulis) = digunakan untuk menulis file baru atau menimpa file lama 
# a -> Append(tambah) = digunakan untuk menambah data di akhir file yang sudah ada 
# x -> Create(buat) = digunakan untuk membuat file baru, error jika sudah ada

# ==========================================
# PRAKTIK FILE I/O PYTHON (1 CODEBASE)
# Mode: w (Write), r (Read), a (Append), x (Create)
# ==========================================

def mode_write(nama_file):
    """Mode 'w': membuat file baru atau menimpa isi file lama."""
    file = open(nama_file, "w", encoding="utf-8")
    file.write("=== CATATAN HARIAN ===\n")
    file.write("1. Menyimpan data secara permanen\n")
    file.write("2. Membuat laporan dalam bentuk file\n")
    file.close()
    print(f"[MODE 'w'] File '{nama_file}' berhasil ditulis.")


def mode_read(nama_file):
    """Mode 'r': membaca isi file yang sudah ada."""
    try:
        file = open(nama_file, "r", encoding="utf-8")
        isi = file.read()
        file.close()
        print(f"\n[MODE 'r'] Isi dari '{nama_file}':")
        print("-" * 35)
        print(isi, end="")
        print("-" * 35)
    except FileNotFoundError:
        print(f"[MODE 'r'] Error: File '{nama_file}' belum ditemukan.")


def mode_append(nama_file):
    """Mode 'a': menambah data di akhir file tanpa menghapus isi lama."""
    file = open(nama_file, "a", encoding="utf-8")
    file.write("3. Backup dan restore data aplikasi\n")
    file.close()
    print(f"[MODE 'a'] Data baru berhasil ditambahkan ke '{nama_file}'.")


def mode_create(nama_file):
    """Mode 'x': membuat file baru, error jika file sudah ada."""
    try:
        file = open(nama_file, "x", encoding="utf-8")
        file.write("File baru dibuat menggunakan mode 'x'.\n")
        file.close()
        print(f"[MODE 'x'] File '{nama_file}' berhasil dibuat.")
    except FileExistsError:
        print(f"[MODE 'x'] Gagal: File '{nama_file}' sudah ada!")


file_utama = "catatan_modul.txt"
file_eksklusif = "laporan_eksklusif.txt"

# 1. Buat & tulis file baru (mode 'w')
mode_write(file_utama)

# 2. Tambah data di akhir file (mode 'a')
mode_append(file_utama)

# 3. Baca hasil akhir file (mode 'r')
mode_read(file_utama)

# 4. Uji mode 'x' (pertama akan berhasil, kedua kali akan memunculkan pesan sudah ada)
mode_create(file_eksklusif)
mode_create(file_eksklusif)

# python 11k.File_I_O.py