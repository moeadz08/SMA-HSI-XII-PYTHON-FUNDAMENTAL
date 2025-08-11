# jenis2 operator
# 1. Operator Aritmetika: (+), (-), (*), (/), (//), (%), (**)
# 2. Operator Relasional(perbandingan): (==), (!=), (>), (<), (>=), (<=)
# 3. Operator Logika: (and), (or), (not)
# 4. Operator Assignment (Penugasan): (+=), (-=), (*=), (/=), (&=)
# 5. Urutan Operasi (Operator Precedence): Parentheses () (Kurung), Exponents ** (Pangkat)
# , Multiplication * , Division / , // , % (dikerjakan dari kiri ke kanan)
# , Addition + , Subtraction - (dikerjakan dari kiri ke kanan)
 


'''
nama= "budi"
umur=17
print ("nama saya", nama, )

# contoh ekspresi
x = 10
y = 2
result = x-y

print (x-y) # bisa ini
print (result) # bisa ini (direkomendasikan biar ga makan banyak memori)

contoh = 8

print (contoh >=8 and contoh < 0) 

print (contoh >=8 or contoh < 5) 

print (contoh >=8 and contoh > 7 and contoh < 90) 
'''


'''
# modulo
print (13 % 5) 

angka = int(input("Masukkan sebuah angka: "))# Mengecek apakah 
# angka genap atau ganjil: angka % 2 == 0 (jika True, maka genap).

if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap.")
else:
    print(f"{angka} adalah bilangan ganjil.")

# modulo adalah sisaan dari hasil pembagian
# contoh 13 % 5 = ?
# kita bagi dulu, 13 / 5 = 2,sekian
# bisa ada ", sekian" karena ada angka 3 dari 13, jadi 3 nya yang kita ambil
# Operator ini sangat berguna untuk:
# Mengulangi sesuatu dalam siklus (misalnya, memilih warna dari 3 pilihan secara berulang)
'''


'''
# normies
x = x + 1
print (x)
# antimainstream
x += 1
print (x)

a=True
print (not a)
'''



a = 5
a == 5


# Bedah Tuntas Pembagian / vs //
'''
# True Division ( / ): Selalu menghasilkan float , seperti di kalkulator.
print(10 / 5) # Output: 2.0
print(10 / 3) # Output: 3.3333333333333335
print(9.9 / 3) # Output: 3.3
print(-10 / 3) # Output: -3.3333333333333335

# Floor Division ( // ): Selalu membuang bagian desimal dan 
# membulatkan ke bawah ke bilangan bulat terdekat.
# Untuk //, selalu dibulatkan ke bawah, meskipun hasilnya negatif.
# Misalnya: -10 // 3 = -4 karena -3.33 dibulatkan ke bawah = -4, bukan -3.
print(10 // 5) # Output: 2
print(10 // 3) # Output: 3
print(9.9 // 3) # Output: 3.0
print(-10 // 3) # Output: -4 (dibulatkan ke bawah)
'''

# Menggabungkan teks dan variabel dengan koma di print() terkadang kurang fl eksibel. Ada cara yang
# lebih modern dan rapi: f-strings.
# Cukup tambahkan huruf f sebelum kutip pembuka, lalu masukkan nama variabel atau bahkan ekspresi
# di dalam kurung kurawal {} .

nama = "Udin"
umur = 18
nilai = 87.5
# Cara lama dengan koma
print("Nama:", nama, ", Umur:", umur, ", Nilai:", nilai)

# Cara modern dengan f-string
print(f"Nama: {nama}, Umur: {umur}, Nilai: {nilai}")
print(f"Tahun depan, umur {nama} akan menjadi {umur + 1} tahun.")