def helloWorld():
    print("Hello Wawa")

class Reviewer:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
    def review(self):
        print("Reviewer " + self.nama + " bertanggung jawab di kelas " + self.kelas)