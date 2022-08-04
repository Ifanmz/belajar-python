# flow control

kelerengku = 0
if kelerengku:
    print("Cetak ini jika benar")
    print(kelerengku)
else:
    print("Cetak ini jika tidak benar")

# nilai = int(input("Masukkan nilai tugas Anda : "))
# if nilai>80:
#    print("Selamat! Anda mendapat nilai A")
#    print("Pertahankan!")
# elif nilai>70:
#    print("Hore! Anda mendapat nilai B")
#    print("Tingkatkan!")
# elif nilai>60:
#    print("Hmm.. Anda mendapat nilai C")
#    print("Ayo semangat!")
# else:
#    print("Waduh, Anda mendapat nilai D")
#    print("Yuk belajar lebih giat lagi!")

# ternary
kondisi = True
print(2 if kondisi else 1/0)

hasil = None
pesan = hasil or "Tidak ada data"
print(pesan)