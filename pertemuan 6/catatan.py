# lambda
# Definisi Fungsi
# 'parameter1' dan 'parameter2' adalah placeholder (variabel lokal)
def nama_fungsi(parameter1, parameter2):
 # 1. Menerima input melalui parameter.
 # 2. Melakukan serangkaian proses di 'body' fungsi.
 hasil_proses = parameter1 + parameter2
 # 3. Mengembalikan output menggunakan 'return'.
 return hasil_proses
# Pemanggilan Fungsi
# 1. Memberikan nilai nyata (argumen) ke fungsi.
# 2. Menangkap nilai kembaliannya dalam sebuah variabel.
hasil_akhir = nama_fungsi(10, 5) # 10 dan 5 adalah argumen
print(hasil_akhir) # Output: 15

# kenapa bisa jadi 15?
# Kamu memanggil fungsi 'nama_fungsi' dengan 'parameter1 = 10' dan 'parameter2 = 5'
# Maka di dalam fungsi, 'hasil_proses = 10 + 5 = 15'
# Nilai 15 ini dikembalikan oleh fungsi (return hasil_proses) dan disimpan ke variabel 'hasil_akhir'

