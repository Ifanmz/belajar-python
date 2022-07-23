# learning string
s = '''Ini adalah string
yang memiliki baris pertama
dan selanjutnya baris kedua'''

sumString = "2" + "3"

print(sumString, type(sumString))

print(s, type(s))

kata = 'dicoding'
kata = kata.upper()
print(kata)
kata = kata.lower()
print(kata)
print('Dicoding    '.rstrip(), "right space")
print('    Dicoding'.lstrip(), "left space")
print('    Dicoding    '.strip(), "right and left space")
kata = 'DicodingDicodingCodeCode'
print(kata.strip("Dicoding"))
print('Dicoding Indonesia'.startswith('Dicoding'))
print('Dicoding Indonesia'.endswith('Indonesia'))
print(' '.join(['Dicoding', 'Indonesia', '!']))
print('Lorem ipsum dolor sit amet'.split())
exampleString = "Hallo Wawa"
print(exampleString.replace("Wawa", "Rahma"))
string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 2))

kata = "Bebas"
print(kata.islower())
print('DICODING'.upper().lower().isupper())
print("dicoding".isalpha())
print("dicoding123".isalnum())
print('Dicoding'.center(20,'!'))
print('Jum\'at \\ rabu')