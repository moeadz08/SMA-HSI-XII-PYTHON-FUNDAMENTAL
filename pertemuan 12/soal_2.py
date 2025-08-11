# Nama file untuk menyimpan daftar tugas
NAMA_FILE_TUGAS = "sumber.txt"
# --- BAGIAN MEMBACA ---
print("--- Daftar Tugas Saat Ini ---")
try:
    with open(NAMA_FILE_TUGAS, 'r') as file:
 # Baca semua baris ke dalam sebuah list
     daftar_tugas = file.readlines()
    if not daftar_tugas:
         print("(Tidak ada tugas)")
    else:
 # Cetak tugas yang sudah ada
         for i, tugas in enumerate(daftar_tugas, 1):
            print(f"{i}. {tugas.strip()}")
except FileNotFoundError:
     print("(File tugas belum ada, akan dibuat baru)")
     daftar_tugas = []
print("-" * 25)

# --- BAGIAN MENAMBAH TUGAS BARU ---
tugas_baru = input("Masukkan tugas baru (atau biarkan kosong untuk selesai): ")
if tugas_baru:  # Jika pengguna memasukkan sesuatu
    # Tambahkan tugas baru ke list di memori, jangan lupa newline!
    daftar_tugas.append(tugas_baru + '\n')
    
    # --- BAGIAN MENULIS KEMBALI ---
    # Buka file dengan mode 'w' untuk menimpa seluruh isinya
    with open(NAMA_FILE_TUGAS, 'w') as file:
        file.writelines(daftar_tugas)

    print("Tugas baru berhasil disimpan!")
else:
    print("Tidak ada tugas baru yang ditambahkan.")

# --- BAGIAN MENYALIN KE FILE LAIN ---
NAMA_FILE_SALINAN = "salinan.txt"

try:
    with open(NAMA_FILE_TUGAS, 'r') as sumber_file:
        isi = sumber_file.read()

    with open(NAMA_FILE_SALINAN, 'w') as salinan_file:
        salinan_file.write(isi)

    print(f"Isi file berhasil disalin ke '{NAMA_FILE_SALINAN}'")

except FileNotFoundError:
    print(f"File sumber '{NAMA_FILE_TUGAS}' tidak ditemukan. Tidak bisa menyalin.")
