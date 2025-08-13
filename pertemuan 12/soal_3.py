import os

# Meminta pengguna memasukkan nama file
nama_file = input("Masukkan nama file yang ingin dihapus: ")

# Mengecek apakah file tersebut ada
if os.path.exists(nama_file):
    # Minta konfirmasi dari pengguna
    konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ").lower()
    
    if konfirmasi == 'y':
        os.remove(nama_file)
        print(f"File '{nama_file}' berhasil dihapus.")
    elif konfirmasi=='n':
        os.remove(nama_file)
        print(f'nggak jadi diapus? kocak!')
    else:
        print("Penghapusan dibatalkan.")
else:
    print(f"File '{nama_file}' tidak ditemukan.")