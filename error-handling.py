# python contoh_salah_sintaksis.py  
#  File "contoh_salah_sintaksis.py", line 2
#    if True print('salah sintaksis')

# while True print('Hello world')
#  File "<stdin>", line 1
#    while True print('Hello world')

# angka = 2
# print(angka)
# Traceback (most recent call last):

# bukan_angka = '1'
# print(bukan_angka + 2)

# z = 0
# try:
#   x = 1 / z
#   print(x)
# except ZeroDivisionError:
#   print('tidak bisa membagi angka dengan nilai nol')

d = {'ratarata': '10.0'}
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except ValueError:
    print('nilai tidak sesuai')
