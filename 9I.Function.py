# Function 
# Funtion (fungsi) adalah blok kode yang dapat digunakan berulang ulang
# Funciton membantu kita menulis kode yang lebih terorganisir, mudah dibaca, dan mudah dipelihara 
# Dengan function kita tidak perlu menulis kode yang sama berkali kali 

# Membuat Function 
# Function dibuat menggunakan kata kunci def 
# Lalu diikuti dengan nama function dan adiakhiri dengan kurung buka dan nutup 
# Biasanya nama function dibuat seperti nama variable, snake_case dan huruf kecil semua 
# Isi function harus terdapat spasi untuk menandakan bahwa itu adalah isi dari function nya 
# Untuk memanggil function, kita bisa langsung panggil nama function nya diikuti dengan kurung buka dan kurug tutup

# Local Variable 
# Saat kita membuat variable di dalam function, maka variable tersebut bersifat local di function it, artinya tidak bisa digunakan di luar function

def nama_function():
    print("Ini dari function baru yang kita buat")

nama_function()
nama_function()

# Function dengan parameter 
# Parameter memungkinkan kita mengirim data ke function 
# Caranya kita bisa tambahkan nama parameter diantara kurung buka dan kurung tutup di function 
# Jika kita inginn menambahkan lebih dari satu parameter, kita bisa gunakan karakter koma sebagai pemisah parameter tersebut 
# Saat memanggil function nya, maka kita wajib mengisi data pada parameter function nya 

def sapa_nama(nama: str):
    print("Halo", nama)
    print("Senang bertemu anda", nama)

sapa_nama("Faiz")

# Function dengan return value 
# Saat membuat function, mungkin kita ingin function tersebut melakukan suatu kegiatan dan hasil kegiatan ingin kita dapatkan 
# Function bisa mengembalikan nilai dari kegiatan yang dilakukan di dalam function 
# Function bisa mengambalikan nilai menggunakan kata kunci return 
# Setelah kata kunci return, diikuti dengan nilai yang akan dikembalikan di function tersebut 

def hitung_luas_lingkaran(radius: float)-> float:
    return radius * 3.14159 * radius

print("Hasil luas lingkaran adalah: ", hitung_luas_lingkaran(21))

# Default Parameter 
# Saat kita menambahkan parameter di function, maka kita wajib mengisi nilai pada parameter tersebut ketika memanggil function nya 
# Namun, kita juga bisa menambahkan default parameter nya, yaitu nilai awal untuk parameter tersebut
# Hal ini menjadikan jika kita tidak mengisi nilai pada parameter tersebut, maka parameter tersebut akan menggunakan nilai awal
# Posisi default paraemeter, tidak boleh di depan parameter biasa, harus di belakang parameter biasa 
# Untuk membuat default parameter, cukup tambahkan = (sama dengan) diikuti dengan nilai nya 
# Default argument boleh lebih dari satu namun tetap dibelakang parameter biasa 

def sapa(nama:str, sapaan:str = "Kamu") -> str:
    return "Hai " + sapaan  + " alias " + nama


print(sapa("Faiz", "Bob"))

# Keyword Argument 
# Argument adalah nilai yang kita kirim ke parameter function ketika kita memanggil function 
# Saat memanggil function, posisi argument harus sama dengan posisi parameter di function 
# Namun, jika kita ingin mengubah posisi argument, sehingga posisinya tidak harus sama dengan posisi parameter, maka kita harus menyebutkan nama parameter nya saat memanggil function 
# Fitur ini disebut Keyword Argument 
# Saat menggunakan Keyword Argument, kita juga bisa mengkombinasikan dengan Argument Biasa

def perkenalan(nama: str, umur: int, kota: str):
    print("Nama: ", nama)
    print("Umur: ", umur, "Tahun" )
    print("Asal: ", kota)
    print("---")

# Postional arguments 
perkenalan("Faiz", 19, "Jakarta")

# Keyword Arguments
perkenalan(umur = 19, kota = "Bekasi", nama= "Jeki")

# Parameter Dinamis 
# Python juga mendukung parameter dinamis 
# Kita bisa menambahkan tanda * sebelum nama parameter untuk memberi tahu bahwa itu adalah parameter dinamis berupa List 
# Atau kita bisa gunakan tanda ** sebelum nama parameter untuk memberi tahu bahwa itu adalah parameter berupa Dictionary
diksionari = {
    "Nama": "Kocak",
    "Makanan": "Ayam"
}

def cetak_diksionari(**datanyo):
    for key, value in datanya.items():
        print(f"{key}: {value}")

cetak_diksionari(diksionari)
# python 9I.Function.py