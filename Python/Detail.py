
# Saya Hakasa Putri mengerjakan TP1 DPBO 2023 C2
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 

from Mahasiswa import Mahasiswa
from Dosen import Dosen

class Detail(Mahasiswa, Dosen):

    def __init__(self): #Constructor

        self.Kegiatan = ""
        self.Angggota = ""
        self.DosenFav = ""

    # metode getter dan setter
    def getDosenFav(self):
        return self.DosenFav
    
    def setDosenFav(self, DosenFav):
        self.DosenFav = DosenFav

    def getKegiatan(self):
        return self.Kegiatan
    
    def setKegiatan(self, Kegiatan):
        self.Kegiatan = Kegiatan
    
    def getRole(self):
        return self.Role
    
    def setRole(self, Role):
        self.Role = Role

    def penjelasan(self):
        if(self.getRole() == "Asisten Dosen"):
            print("dan merupakan asdos yang sedang " + self.getKegiatan() + " kepada mahasiswa")
        elif(self.getRole() == "Dosen"):
            print("dan merupakan dosen yang sedang " + self.getKegiatan() + " kepada mahasiswa")
        elif(self.getRole() == "Mahasiswa Biasa"):
            print("dan dosen favoritnya adalah " + self.getDosenFav())
        elif(self.getRole() == "Anggota BEM"):
            print("dan merupakan anggota BEM yang sedang " + self.getKegiatan() + " BEM")
        elif(self.getRole() == "Anggota EC"):
            print("dan merupakan anggota EC yang sedang " + self.getKegiatan())
            print("juga sedang mempersiapkan diri menjadi ketua")

    
    # tampilkan informasi class BEM
    def getDetail(self):
        
        print("Role           : " + self.getRole())
        print("----------------------------------------------------------------")
        self.penjelasan()
        print("----------------------------------------------------------------")
        print()