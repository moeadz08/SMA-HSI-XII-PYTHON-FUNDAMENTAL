# 1.
'''
def salam_pembuka():
    print("==============================")
    print("Selamat Datang di Program Saya!")
    print("==============================")
salam_pembuka()
'''

# 2.
'''
def info_cuaca(kota, cuaca):
    print(f"Cuaca di kota {kota} hari ini {cuaca}.")   
info_cuaca("Jakarta", "berawan")
info_cuaca("Bandung", "hujan")
info_cuaca("Cirebon", "cerah")
'''

# 3.
'''
def kubik(angka):
    return angka ** 3

hasil_kubik = kubik(4)
print(hasil_kubik)
'''

# 4.
'''
def hitung_diskon(harga_awal, persen_diskon):
    jumlah_diskon = harga_awal * (persen_diskon / 100)
    harga_akhir = harga_awal - jumlah_diskon
    return harga_akhir

try:
    harga = float(input("Masukkan harga barang: "))
    diskon = float(input("Masukkan persentase diskon (%): "))

    harga_setelah_diskon = hitung_diskon(harga, diskon)
    print(f"Harga akhir setelah diskon: Rp {harga_setelah_diskon:.2f}")
except ValueError:
    print("Error: Masukkan angka yang valid.")
'''

# 5.
'''
celcius = 37  # misalnya suhu tubuh normal
fahrenheit = ((9/5) * celcius) + 32
print('suhu adalah dalam fahrenheit adalah',fahrenheit, "Fahrenheit")

# Fungsi untuk mengubah Fahrenheit ke Celsius
def fahrenheit_ke_celcius(temp_f):
    return (temp_f - 32) * 5 / 9

hasil = fahrenheit_ke_celcius(98.6)

print(f"98.6°F sama dengan {hasil:.2f}°C")
'''



