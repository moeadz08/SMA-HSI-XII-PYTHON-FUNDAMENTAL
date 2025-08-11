# 1.
'''
judul_buku = input('Masukkan Judul Buku: ')
perbaikan_font = judul_buku.title()
anti_sepasi = perbaikan_font.strip()
print(anti_sepasi)
'''

# 2.

email = input('Masukkan Email Anda: ')
if email.endswith((".com", ".co.id")):
    if "@" in email:
        print("Email valid")
    else:
        print("Email invalid")
else:
    print("Email invalid")

    
# 3.

'''
kalimat = "Saya tidak jago."
sensor = 'tidak'
print(kalimat.replace(sensor, "***"))
'''

# 4.
'''
nama_orgnz = input("Masukkan nama organisasi: ")

kata_kata = nama_orgnz.split()

akronim = ""
for kata in kata_kata:
    akronim += kata[0].upper()

print("Akronim:", akronim)
'''

# 5.
'''
import re

judul = input("Masukkan judul artikel: ")

judul = judul.lower() # ubah jadi lowercase

judul = judul.replace(" ", "-") # ganti spasi

# apus semua karakter selain huruf, angka, dan tanda hubung
slug = re.sub(r'[^a-z0-9\-]', '', judul)

print("Slug:", slug)
'''



























