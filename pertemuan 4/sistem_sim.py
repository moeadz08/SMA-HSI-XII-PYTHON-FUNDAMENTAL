umur = int(input("berapa umur anda?"))

batas = 17

print("mengecek kelayakan...")

if umur > 100:
    print("kolot!")
elif umur >= batas:
    print("gas bikin SIM")
    print("sini main ke kantor")
elif umur < 0:
    print("ngaco lu!")
else:
    print('selamat, anda gagal')

print("pengecekan selesai")

