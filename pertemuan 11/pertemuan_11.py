# 1.
# hai_cuy = input('masukkan nama file: ')

# with open('puisi.txt') as hai_cuy:

# an kok gabisa
'''
nama_file = "puisi.txt"

try:
    with open(nama_file, 'r') as file:
        print("Daftar Siswa (dibaca dengan 'with open'):")
        for baris in file:  # Harus diindentasikan ke dalam blok 'with'
            print(f"- {baris.strip().upper()}")

except FileNotFoundError:
    print(f"Error: File '{nama_file}' invalid.")
'''

# 2.
# mbox-short.txt
'''
nama_file = input("Masukkan nama file: ")

try:
    with open(nama_file, 'r') as file:
        total = 0
        count = 0

        for baris in file:
            if baris.startswith("X-DSPAM-Confidence:"):
                angka_str = baris[len("X-DSPAM-Confidence:"):].strip()
                angka_float = float(angka_str)
                total += angka_float
                count += 1

        if count > 0:
            rata_rata = total / count # rerata
            print(f"Rata-rata X-DSPAM-Confidence: {rata_rata}")
        else:
            print("Tidak ada baris yang cocok.")

except FileNotFoundError:
    print(f"Error: File '{nama_file}' tidak ditemukan.")
'''
# 3.
'''
nama_file = input("Masukkan nama file: ")

if nama_file.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, 'r') as file:
            print("Daftar Siswa (dibaca dengan 'with open'):")
            for baris in file:
                print(f"- {baris.strip().upper()}")

    except FileNotFoundError:
        print(f"Error: File '{nama_file}' invalid.")
'''











