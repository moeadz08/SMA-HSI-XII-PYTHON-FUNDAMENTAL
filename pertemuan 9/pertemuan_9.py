# 1.
# Ahli Indexing Diberikan string s = "Belajar Python itu Menyenangkan". Tulis kode untuk
# mengambil dan mencetak:
# Karakter pertama (B)
# Karakter terakhir (n) menggunakan indexing negatif.
# Karakter spasi pertama (di indeks 7).
'''
s = "Belajar Python itu Menyenangkan"

karakter_pertama = s [0]
print(f"Index ke 0 adalah: '{karakter_pertama}'")


karakter_terakhir = s [-1]
print(f"Index terakhir adalah: '{karakter_terakhir}'")


karakter_kedelapan = s [7]
print(f"Index ke 7 adalah: '{karakter_kedelapan}'")
'''

# 2.
# Master Slicing Masih menggunakan string s = "Belajar Python itu Menyenangkan".
# Tulis kode slicing untuk mendapatkan dan mencetak substring berikut:
# "Python"
# "Menyenangkan"
# "Belajar
'''
s = "Belajar Python itu Menyenangkan"

karakter_8_sampe_15 = s [8:14]
print(f"Indeks ke 7 sampe 14: '{karakter_8_sampe_15}'")


karakter_12_akhir = s [-12:]
print(f"Indeks ke 12 karakter akhir: '{karakter_12_akhir}'")


karakter_1_sampe_6 = s [0:7]
print(f"Indeks ke 0 sampe 7: '{karakter_1_sampe_6}'")
'''

# 3.

# Membalik Kata Buatlah sebuah program yang:
# Meminta pengguna memasukkan sebuah kata.
# Menggunakan slicing untuk membalik kata tersebut.
# Mencetak kata yang sudah dibalik.
# Menggunakan if untuk mengecek apakah kata tersebut adalah palindrom (kata yang sama jika
# dibaca dari depan maupun belakang, contoh: "kasur rusak"). Cetak pesan yang sesuai.
'''
while True:
    kata = input("masukkan kata: ")

    if kata.upper() == "DONE":
        print("Program selesai. Terima kasih!")
        break

    kata_terbalik = kata[::-1] # slicing    

    print(f"Kata yang dibalik: {kata_terbalik}")

# mengecek apakah palindrom
    if kata.lower() == kata_terbalik.lower():
        print("Ini adalah palindrom!")

    else:
        print("Ini bukan palindrom.")
'''

# 4.

# Kode Rahasia Buatlah sebuah program yang mengambil "kode rahasia" dari sebuah kalimat
# panjang. Aturannya adalah: ambil setiap karakter ketiga dari kalimat tersebut. Gunakan slicing dengan step
# untuk mengekstrak dan mencetak kode rahasia dari kalimat:
# "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
'''
karakter = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
lompat_3kali = karakter[::3]
print(lompat_3kali)
'''

# 5.

# Memperbaiki Nama Diberikan sebuah nama yang salah ketik: nama_salah = "dUDI
# sANTOSO". Kamu belum belajar string methods seperti .title() atau .upper(). Gunakan hanya
# indexing, slicing, dan penggabungan string (+) untuk memperbaiki nama tersebut menjadi "Budi
# Santoso". Cetak hasilnya.
'''
nama_salah = "dUDI sANTOSO"
nama_benar = "Budi Santoso"
nama_benar = 'B' + 'u' + 'd' + 'i' ' ' 'S' + 'a' + 'n' + 't' + 'o' + 's' + 'o'
print ("nama baru:", nama_benar)
'''



















