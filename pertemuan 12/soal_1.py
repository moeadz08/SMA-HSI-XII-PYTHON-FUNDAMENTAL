# nama_file = "log_kegiatan.txt"

# user = input('Masukkan kegiatan: ')
# with open(user, 'a') as file:
#  print(f"\nMenambahkan item baru ke '{nama_file}'...")

#  file.write(user)
# #  file.write("5. Telur (1 lusin)\n")
#  print("Berhasil menambahkan item baru.")
# print(f"File '{nama_file}' telah ditutup.")

# change directory
"cd '.\pertemuan 12\'"

nama_file = "log_kegiatan.txt"

with open(nama_file, 'a') as file:  # pakai nama_file, bukan user
    print(f"\nMenambahkan item baru ke '{nama_file}'...")
    while True:
        user = input('Masukkan kegiatan: ')
        if user.strip() == "":
            break
        file.write(user + "\n")  # tulis setiap input ke file
        print("Berhasil menambahkan item baru.")

print(f"File '{nama_file}' telah diubka.")



