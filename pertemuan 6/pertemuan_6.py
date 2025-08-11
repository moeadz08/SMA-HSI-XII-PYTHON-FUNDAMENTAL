# 1.
'''
def buat_email(nama_pengguna, domain="coding.com"):
    email = f"{nama_pengguna}@{domain}"
    return email.lower()

print(buat_email("Budi"))      
print(buat_email("Ani", "belajar.id"))  
'''

# 2. 
'''
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan} dengan berat {berat_kg} kg.")
    print(f"Express: {express}")
    print(f"Asuransi: {asuransi}")

# Pemanggilan fungsi:
kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)
'''

# 3.
# Mengembalikan Banyak Nilai Buatlah sebuah fungsi bernama analisis_daftar yang
# menerima satu parameter berupa daftar angka (misal: [10, 20, 30, 40, 50]). Fungsi ini harus
# mengembalikan TIGA nilai:
# . Jumlah total semua angka dalam daftar.
# . Jumlah elemen dalam daftar.
# . Nilai rata-rata. Petunjuk: Gunakan fungsi bawaan sum() dan len(). Panggil fungsi tersebut dan
# "unpack" hasilnya ke dalam tiga variabel terpisah, lalu cetak.
'''
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka) # 'sum' untuk ngitung jumlah total
    jumlah = len(daftar_angka)           
    rata_rata = total / jumlah          
    return total, jumlah, rata_rata      

data = [10, 20, 30, 40, 50] # bebas angkanya, ini ngikut contoh
total, jumlah, rata_rata = analisis_daftar(data)  # hasil unpacking

print("Total:", total)
print("Jumlah elemen:", jumlah)
print("Rata-rata:", round(rata_rata, 2))  # diibulatkan ke 2 angka desimal
'''

# 4.
'''
def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka untuk menghitung total, jumlah elemen, dan rata-rata.

    Args:
        daftar_angka (list of numbers): Daftar yang berisi angka-angka (int atau float).

    Returns:
        tuple: Mengembalikan tiga nilai:
            - total (number): Jumlah total dari seluruh angka dalam daftar.
            - jumlah (int): Jumlah elemen dalam daftar.
            - rata_rata (float): Nilai rata-rata dari angka-angka dalam daftar.
    """
    total = sum(daftar_angka)
    jumlah = len(daftar_angka)
    rata_rata = total / jumlah
    return total, jumlah, rata_rata

# Contoh pemanggilan
data = [10, 20, 30, 40, 50]
total, jumlah, rata_rata = analisis_daftar(data)
print("Total:", total)
print("Jumlah elemen:", jumlah)
print("Rata-rata:", rata_rata)

# Menampilkan dokumentasi fungsi
help(analisis_daftar)
'''

# 5.
'''
# def get_luas_lingkaran(radius):
#  return 3.14159 * (radius ** 2)

# lambda untuk ngitung luas lingkaran
luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)  # 3.14159 * (radius ** 2) adalah rumus luas lingkaran: π × r²

print(luas_lingkaran_lambda(7)) # 7 = jari2nya
'''



