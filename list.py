# list type 

# declaration
nama = ["Ifan", "Rahma"]

print(nama)

a = [1, 2.2, 'python']

print(a)

x = [5,10,15,20,25,30,35,40]
print(x[5]) # mengambil data dari index ke 5
print(x[-1]) # mengambil data dari index terakhir
print(x[3:5]) # mengambil data dari index 3 sampai sebelum index 5
print(x[:5]) # mengambil data dari index 0 sampai index sebelum 5
print(x[-3:]) # mengambil data dari 3 index terakhir
print(x[1:7:2]) # mengambil data dari index 1 sampe index sebelum 7 dengan step pengambilan data 2

print("================================================================")

x1 = [1,2,3]
x1[2] = 7

# menambahkan data pada list
x1.append(8)

# menghapus nilai pada spesifik index tertentu
del x1[-1]

print(x1)

# slicing pada string

hello = "Hello world"
print(hello[4])
print(hello[6:11])
print(hello)
hello = "Halo dunia"
print(hello)
print("================================================================")
# tuple list 
t = (5,'program', 1+3j)
print(t[1])
print(t[0:3])
print(t)
print("================================================================")
# set list 
a = {1,2,2,3,3,3}
print(a)
print("================================================================")
#Dictionary
d = {1:'value','key':2}
print(d[1])
print(d['key'])
print("================================================================")
# conversion
print(float(5))
print(int(10.6))
print(int(-10.6))
print(float('2.5'))
print(str(25))
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
print(dict([[1,2],[3,4]]))

print("================================================================")
contohList = [1,2,3,4,5,6,7,8,9]
print(len(contohList), "min: ", min(contohList), "max: ", max(contohList), "count: ",contohList.count(3))

contohList2 = ["a", "b", "c"]

mergeList = contohList + contohList2

print(mergeList, "replikasi contohList2: ", contohList2 * 2)

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)