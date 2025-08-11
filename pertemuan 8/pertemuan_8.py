# 1.
# Iterasi dan range() Gunakan for loop dan fungsi range() untuk mencetak semua bilangan
# kelipatan 7 dari 0 hingga 70 (inklusif).
'''
print('angka2 kelipatan 7')
for apaaja in range(7, 76, 7):
    print(apaaja)
'''

# 2.

# Latihan 2: Pola Akumulator dengan String Buat program yang memiliki sebuah string: kalimat =
# "Python". Gunakan for loop untuk membangun string baru yang merupakan kebalikan dari string
# tersebut.
# Petunjuk: Inisialisasi string kosong kalimat_terbalik = "". Di dalam loop, tambahkan setiap
# huruf ke depan kalimat_terbalik (kalimat_terbalik = huruf + kalimat_terbalik).
# Output yang diharapkan: "nohtyP"
'''
kalimat_terbalik = "Python"

for huruf in reversed(kalimat_terbalik):
    print(f"Karakter saat ini: {huruf}")
'''

'''
kalimat = "Python"
kalimat_terbalik = "" # untuk nyimpen hasil dari proses membalik kalimat.

for huruf in kalimat: # untuk baca kalimat (dari kiri ke kanan)
    kalimat_terbalik = huruf + kalimat_terbalik # untuk ngebalik huruf

print(kalimat_terbalik)
'''

# 3.
'''
jumlah = 0 

for angka in range(1, 51): # untuk ngehasilin angka dari 1-50, kenapa 51? karena range(diantara)
    if angka % 3 == 0 and angka % 5 == 0: # kenapa pake and? karena disuruhnya
        #(habis dibagi 3 DAN habis dibagi 5, bukan ATAU)
        print(angka)  # nampilin angka yg habis dibagi 3 dan 5
        jumlah += 1   # triggerr

print(f"\ntotal angka yang habis dibagi 3 dan 5 dari 1 sampe 50: {jumlah}")
'''

# 4.
'''
for i in range(5, 0, -1):  # loop dari 5 ke 1 (mundur), kenapa -1? jawabannya sama kek yg diatas
    for j in range(i):     # cetak * sebanyak i kali
        print("*", end="") # tetep di baris yang sama
    print()  # Pindah ke baris baru setelah satu baris selesai
'''

# 5.

# faktorial
# 1! = 1
# 2! = 2 * 1 = 2
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040
# 8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320
# 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 362880
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800 

while True:
    user_input = input("masukkan bilangan bulat positif: ")

    if user_input.lower() == "selesai":
        print("Program selesai. Terima kasih!")
        break

    angka = int(user_input)

    hasil_faktorial = 1

    # ngitung faktorial dengan for loop
    for i in range(1, angka + 1):
        hasil_faktorial *= i  # Sama seperti hasil_faktorial = hasil_faktorial * i

    print(f"Faktorial dari {angka} adalah {hasil_faktorial}")











