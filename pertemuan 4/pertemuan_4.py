# 1.
'''
jam = float(input("berapa jam anda bekerja?"))
tarif = float(input('tarif anda per jam berapa?'))

print('menghitung upah...')
if jam > 40:
    jam_normal = 40
    jam_lembur = jam - 40
    total_upah = (jam_normal * tarif) + (jam_lembur * tarif * 1.5)

else:
    total_upah = jam * tarif

print("Pay:", total_upah)
'''

# 2.
'''
try:
    jam = float(input("berapa jam anda bekerja? "))
    tarif = float(input("tarif anda per jam berapa? "))

    print("menghitung upah...")
    if jam > 40:
        jam_normal = 40
        jam_lembur = jam - 40
        total_upah = (jam_normal * tarif) + (jam_lembur * tarif * 1.5)
    else:
        total_upah = jam * tarif

    print("Pay:", total_upah)

except ValueError:
    print("Error, please enter numeric input")
'''

# 3.
'''
try:
    skor = float(input("masukkin skor (antara 0.0 sampai 1.0): "))

    if skor < 0.0 or skor > 1.0:
        print("Bad score")
    else:
        if skor >= 0.9:
            grade = "A"
        elif skor >= 0.8:
            grade = "B"
        elif skor >= 0.7:
            grade = "C"
        elif skor >= 0.6:
            grade = "D"
        else:
            grade = "F"
        
        print(f"Grade anda: {grade}")

except ValueError:
    print("Error, please enter a numeric input")
'''

# 4.
'''
tinggi_cm = 70
umur = 12
didampingi_ortu = False

if tinggi_cm >= 150 and (umur >= 12 or didampingi_ortu):
    print("Boleh Masuk")
else:
    print("Tidak Boleh Masuk")
'''