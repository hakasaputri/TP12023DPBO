# Saya Hakasa Putri mengerjakan TP1 DPBO 2023 C2
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 

from Manusia import Manusia

class Mahasiswa(Manusia):

    # constructor
    def __init__(self): 

        self.NIM = ""
        self.Buku = 0
        self.LaptopMahasiswa = ""
        self.KegiatanMahasiswa = ""

    # setter getter
    def getNIM(self):
        return self.NIM

    def setNIM(self, NIM):
        self.NIM = NIM

    def getBuku(self):
        return self.Buku

    def setBuku(self, Buku):
        self.Buku = Buku

    def getLaptopMahasiswa(self):
        return self.LaptopMahasiswa

    def setLaptopMahasiswa(self, LaptopMahasiswa):
        self.LaptopMahasiswa = LaptopMahasiswa

    def getKegiatanMahasiswa(self):
        return self.KegiatanMahasiswa

    def setKegiatanMahasiswa(self, KegiatanMahasiswa):
        self.KegiatanMahasiswa = KegiatanMahasiswa

    # Metode Belajar yang menampilkan aktivitas belajar mahasiswa
    def Belajar(self):
        print("Dia merupakan seorang mahasiswa yang sedang " + self.getKegiatanMahasiswa())

    # Metode getMahasiswa yang menampilkan informasi kelas Mahasiswa
    def getMahasiswa(self):
        
        print("NIM            : " + self.getNIM())
        print("Jumlah Buku    : " + str(self.getBuku()) + " buku")
        print("Laptop         : " + self.getLaptopMahasiswa())
        print("----------------------------------------------------------------")
        self.Belajar()
        print("----------------------------------------------------------------")
        print()
