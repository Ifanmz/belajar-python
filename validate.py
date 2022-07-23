while True:
    print("Masukkan nama anda:")
    nama = input()
    if nama.isalpha():
        print("Hallo ", nama)
        break
    print("Masukkan Nama anda dengan benar")