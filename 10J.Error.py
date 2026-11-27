# Error 
# Error adalah kesalahan yang terjadi saat program berjalan 
# Ketika error terjadi, program akan berhenti dan menampilkan pesan error 

# SyntaxError
# Kesalahn sintaks
# Diakibatkan kesalahan penulisan kode 

# ----------- print("Halo" #Lupa tutup

# NameError 
# Variable Tidak ditemukan 
# Diakibatkan memanggil variable yang tidak pernah di deklarasikan 

# ----------- print(x) #padahal x tidak pernah ada

# TypeError
# Kesalahan tipe data
# Diakibatkan kesalahan operasi antar tipe data dll

# ----------- angka = int("Kocak lu") #int tidak boleh berisi huruf

# IndexError
# Mengakses index di list atau tuple yang tidak pernak ada

namas: list[str] = ["Saya", "Anjay"]

# ----------- print(namas[2]) #index urutan ke 2 tidak pernah ada

# KeyError
# Key tidak valid
# Diakibatkan kesalahan dalam memanggil key di dictionary

identitas: dict[str: str] = {
    "Nama": "Faiz"
}

# ----------- print(identitas["Umur"]) #key umur tidak pernah ada

# ZeroDivisionError
# Pembagian dengan nol
# Diakibatkan membagi bilangan dengan nol

# ----------- print(100/0) #membagi 100 dengan 0

# Penanganan error 
# Secara default ketika terjadi error python akan otomatis mengentikan jalan nya program 
# Bagaimana untuk menangani error agar program kita tidak berhenti?
# Penanganan error memungkinkan program unuk menangani error dengan baik tanpa berhenti secaratiba tiba 

# Try-Except 
# try-except digunakan untuk menangani error yang mungkin terjadi

identitas: dict[str: str] = {
    "Nama": "Faiz"
}

try:
    print(identitas["Umur"]) #key umur tidak pernah ada
except:
    print("Terjadi key error")


print("Program tak berhenti")

# Menangani Error Spesifik 
# Saat menangani error, mungkin kita ingin melakukan hal yang berbeda untuk jenis error yang berbeda 
# Kita bisa menyebutkan tipe errornya setelah kata kunci except, sehingga jika terjadi error jenis tersebut, maka bagian except tersebut yang akan dieksekusi 
# Kita bisa menambahkan lebih dari satu except

try:
    print(identitas["Umur"]) #key umur tidak pernah ada

except KeyError:
    print("Terjadi key Error")
except ZeroDivisionError:
    print("Terjadi pembagian dengan nol")
except:
    print("Terjadi error yang lain")

# Try-Except-Else
# try-except juga memiliki bagian else seperti pada if dan for dan while 
# Bagian else dijalankan jika tidak ada error pada try-except
# Jika terjadi error, bagian else tidak akan dijalankan

try:
    print(identitas["Nama"]) #key umur tidak pernah ada

except KeyError:
    print("Terjadi key Error")
except ZeroDivisionError:
    print("Terjadi pembagian dengan nol")
except:
    print("Terjadi error yang lain")
else:
    print("Gaada error kok")

# Try-Except-Finally
# else di try-except hanya akan dijalankan ketika tidak ada error 
# Bagaimana jika kita ingin melakukan sesuatu, baik itu jika terjadi error ataupun tidak?
# Kita bisa menggunakan finally
# Finally selalu dijalankan, baik ada error atau tidak 


try:
    print(identitas["Nama"]) #key umur tidak pernah ada

except KeyError:
    print("Terjadi key Error")
except ZeroDivisionError:
    print("Terjadi pembagian dengan nol")
except:
    print("Terjadi error yang lain")
else:
    print("Gaada error kok")
finally:
    print("Error maupun gak Error finally ini bakal di eksekusi yahah")



# python 10J.Error.py