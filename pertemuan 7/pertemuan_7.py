# 1.
'''
x = 10

while x >= 0:
    print(x)

    x -= 1
print('Blastoff!')
'''

# 2.

# angka_rahasia = 7
# while True:
#     angka_rahasia = int(input('>'))
#     if (angka_rahasia == '7'):
#         print('Selamat, tebakan Anda benar!')
#     else:
#         print('coba lagi!')
#         break
'''
angka_rahasia = 7
while True:
    angka_tebakan = int(input('>'))
    if (angka_tebakan == 7):
        print('Selamat, tebakan Anda benar!')
        break
    else:
        print('Salah, coba lagi!')

print('\nTerimakasih sudah bermain!')
'''

# 3.
'''
total = 0 # buat ngitung jumlah total semua angka
count = 0 # buat ngitung berapakali user nginput angka yang valid

while True: # program minta input dari
    data_input = input(": ") # user tanpa batas sampai user ngetik "done"

    if data_input.lower() == 'done': # kalo user ngetik "done" (dalam huruf kecil/besar),
        break  # program bakal keluar dari loop while (looping)
    # ".lower()" bikin program jadi lebih ramah pengguna, gak peduli mereka ngetik:
    # done, DONE, DoNe, bodoamat sama besarkecilnya huruf
    try:
        angka = float(data_input) # convert ke float biar hanya masukkin angka, baik desimal maupun integer
        total += angka # jika berhasil, angka itu ditambahkan ke total
        count += 1 
    except ValueError: # kalo user masukkin selain angka, bakal error dan 
        continue # bisa pake ini, bisa enggak (yang penting bukan break)
        print("Invalid fren") # menampilkan "Invalid fren"
         # biar lanjut ke bawah dan berentiin looping, kalo nulisnya break malah langsung end

if count > 0:
    rata_rata = total / count # jika ada angka minimal 1
    print(f"\nTotal: {total}") # akan ngitung total
    print(f"Jumlah angka: {count}") # jumlah angka
    print(f"Rata-rata: {rata_rata}") # rata-rata
else:
    print("Itu bukan angka Pak!") # kalo ga valid
'''









