# not return value
def cetak( param1 ):
   print(param1)

cetak("Wawa")

# return value
def kali(angka1, angka2):
    # Kalikan kedua parameter
    hasil = angka1 * angka2
    print('Dicetak dari dalam fungsi: {}'.format(hasil))
    return hasil
 
# Panggil fungsi kali
keluaran = kali(10, 20);
print('Dicetak sebagai kembalian: {}'.format(keluaran))

def ubah(list_saya):
    list_saya.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(list_saya))
 
# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))

print("================================================================")
def ubah(list_saya):
    "Deklarasi Variabel list_saya berikut hanya dikenali (berlaku) di dalam fungsi ubah"
    list_saya = [1, 2, 3, 4] 
    print ('Nilai di dalam fungsi: {}'.format(list_saya))
 
# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))


print("===============================")
def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))
 
 
# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i':7, 'j':8})

# Anonymous functoin
kali = lambda nilai1, nilai2: nilai1 * nilai2
print ("Hasil : ", kali( 11, 21 ))
print ("Hasil : ", kali( 2, 2 ))