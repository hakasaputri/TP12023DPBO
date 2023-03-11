
# Saya Hakasa Putri mengerjakan TP1 DPBO 2023 C2
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 


class Manusia:

    #Constructor
    def __init__(self): 
        # Inisialisasi atribut Nama, Gender, dan KegiatanManusia
        self.Nama = ""
        self.Gender = ""
        self.KegiatanManusia = ""

    # setter getter untuk atribut Nama
    def getNama(self):
        return self.Nama

    def setNama(self, Nama):
        self.Nama = Nama

    # setter getter untuk atribut Gender
    def getGender(self):
        return self.Gender

    def setGender(self, Gender):
        self.Gender = Gender

    # setter getter untuk atribut KegiatanManusia
    def getKegiatanManusia(self):
        return self.KegiatanManusia

    def setKegiatanManusia(self, KegiatanManusia):
        self.KegiatanManusia = KegiatanManusia

    # method untuk menampilkan informasi kegiatan manusia
    def KegiatanManusiaManusia(self):
        print("Seorang manusia yang bernama " + self.getNama() + " sedang " + self.getKegiatanManusia() + ".")

    # method untuk menampilkan informasi lengkap manusia
    def getManusia(self):
        print("Nama           : " + self.getNama())
        print("Gender         : " + self.getGender())
        print("----------------------------------------------------------------")
        self.KegiatanManusiaManusia()
        print("----------------------------------------------------------------")
        print()
