mahasiswa = ["Ifan","Rahma"]

mahasiswa.append("Zaenudin")

for nama in mahasiswa:
    print("nama: ", nama)

for huruf in 'Dicoding':  # Contoh pertama
    print('Huruf: ', huruf)

# flowers = ['mawar', 'melati', 'anggrek']
# for flower in flowers:  # Contoh kedua
#     print('Flower: {}'.format(flower))

flowers = ['mawar', 'melati', 'anggrek']
for index in range(len(flowers)):
    print('Flowers: {}'.format(flowers[index]))

for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()

for huruf in 'Dico ding':
    if huruf == 'd':
        break
    print('Huruf saat ini: {}'.format(huruf))

for i in range (0,10):
    for j in range (0,10):
        if j>i:
            print()
            break
        else:
            print("*",end="")

print('\n================================================================')

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

items = [1,2,3,4,5,6,7,8]

for item in items:
    if (item == 1):
        #ditemukan!
        print("item ditemukkan, item tersebut bernilai: ", item)
        break
else:
    #Item tidak ditemukan
    print("item tidak ditemukan")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break