
# Saya Hakasa Putri mengerjakan TP1 DPBO 2023 C2
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 


from Manusia import Manusia

class Dosen(Manusia):

   # constructor class Dosen
    def __init__(self): 

        # inisialisasi atribut milik class Dosen
        self.NIP = ""
        self.Spidol = 0
        self.LaptopDosen = ""


    # setter getter untuk atribut milik class Dosen
    def getNIP(self):
        return self.NIP

    def setNIP(self, NIP):
        self.NIP = NIP

    def getSpidol(self):
        return self.Spidol

    def setSpidol(self, Spidol):
        self.Spidol = Spidol

    def getLaptopDosen(self):
        return self.LaptopDosen

    def setLaptopDosen(self, LaptopDosen):
        self.LaptopDosen = LaptopDosen

    # method khusus class Dosen
    def MemberiNilai(self):
        print("Dia merupakan dosen yang sedang memberi nilai kepada mahasiswa")

    # method untuk menampilkan informasi milik class Dosen
    def getDosen(self):
        
        print("NIP            : " + self.getNIP())
        print("Jumlah Spidol  : " + str(self.getSpidol()) + " buah")
        print("Laptop         : " + self.getLaptopDosen())
        print("----------------------------------------------------------------")
        self.MemberiNilai()
        print("----------------------------------------------------------------")
        print()
