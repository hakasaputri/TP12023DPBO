# Saya Hakasa Putri mengerjakan TP1 DPBO 2023 C2
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan 
# kecurangan seperti yang telah dispesifikasikan. Aamiin 

# import kelas

from Dosen import Dosen
from Mahasiswa import Mahasiswa
from Manusia import Manusia
from Detail import Detail

# -------------- resyad ------------------

# Membuat objek Detail bernama resyad
resyad = Detail()
resyad.setNama("resyad")
resyad.setGender("Perempuan")
resyad.setKegiatanManusia("Minum")
resyad.setNIM("2008978")
resyad.setBuku(18)
resyad.setLaptopMahasiswa("Macbook Pro MJLQ2")
resyad.setKegiatanMahasiswa("Belajar")
resyad.setRole("Mahasiswa Biasa")
resyad.setDosenFav("Mrs.Rose")

# Menampilkan informasi tentang objek resyad
print("================================================================")
print("                     Informasi resyad")
print("================================================================")

print()
resyad.getManusia()
resyad.getMahasiswa()
resyad.getDetail()
print()
print()


# -------------- angga ------------------

# Membuat objek Detail bernama angga
angga = Detail()
angga.setNama("angga")
angga.setGender("Perempuan")
angga.setKegiatanManusia("Minum")
angga.setNIM("2008978")
angga.setBuku(18)
angga.setLaptopMahasiswa("Macbook Pro MJLQ2")
angga.setKegiatanMahasiswa("Belajar")
angga.setRole("Anggota EC")
angga.setKegiatan("Merancang proker masa depan")

# Menampilkan informasi tentang objek angga
print("================================================================")
print("                     Informasi angga")
print("================================================================")

print()
angga.getManusia()
angga.getMahasiswa()
angga.getDetail()
print()
print()


# -------------- getsbi ------------------

# Membuat objek Detail bernama getsbi
getsbi = Detail()
getsbi.setNama("getsbi")
getsbi.setGender("Perempuan")
getsbi.setKegiatanManusia("Minum")
getsbi.setNIM("2008978")
getsbi.setBuku(18)
getsbi.setLaptopMahasiswa("Macbook Pro MJLQ2")
getsbi.setKegiatanMahasiswa("Belajar")
getsbi.setRole("Anggota EC")
getsbi.setKegiatan("Belajar bahasa inggris")

# Menampilkan informasi tentang objek getsbi
print("================================================================")
print("                     Informasi getsbi")
print("================================================================")

print()
getsbi.getManusia()
getsbi.getMahasiswa()
getsbi.getDetail()
print()
print()


# -------------- pahri ------------------

# Membuat objek Detail bernama pahri
pahri = Detail()
pahri.setNama("pahri")
pahri.setGender("Perempuan")
pahri.setKegiatanManusia("Minum")
pahri.setNIM("2008978")
pahri.setBuku(18)
pahri.setLaptopMahasiswa("Macbook Pro MJLQ2")
pahri.setKegiatanMahasiswa("Belajar")
pahri.setRole("Anggota BEM")
pahri.setKegiatan("Menghadiri evaluasi")


# Menampilkan informasi tentang objek pahri
print("================================================================")
print("                     Informasi pahri")
print("================================================================")

print()
pahri.getManusia()
pahri.getMahasiswa()
pahri.getDetail()
print()
print()


# -------------- Mila ------------------

# Membuat objek Detail bernama mila
mila = Detail()
mila.setNama("Mila")
mila.setGender("Perempuan")
mila.setKegiatanManusia("Minum")
mila.setNIM("2008978")
mila.setBuku(18)
mila.setLaptopMahasiswa("Macbook Pro MJLQ2")
mila.setKegiatanMahasiswa("Belajar")
mila.setRole("Asisten Dosen")
mila.setKegiatan("Mengajari materi")


# Menampilkan informasi tentang objek mila
print("================================================================")
print("                     Informasi Mila")
print("================================================================")

print()
mila.getManusia()
mila.getMahasiswa()
mila.getDetail()
print()
print()

# -------------- Mrs. Rose ------------------

# Membuat objek Detail bernama Mrs.Rose
rose = Detail()
rose.setNama("Mrs.Rose")
rose.setGender("Perempuan")
rose.setKegiatanManusia("Tidur")
rose.setNIP("19560701 198710 1001")
rose.setSpidol(18)
rose.setLaptopDosen("Macbook Pro M2 MNEH3ID/A 8-Core")
mila.setKegiatanMahasiswa("Belajar")
rose.setRole("Dosen")
rose.setKegiatan("Memberikan tugas")


# Menampilkan informasi tentang objek Mrs.Rose
print("================================================================")
print("                     Informasi Mrs.Rose")
print("================================================================")

print()
rose.getManusia()
rose.getDosen()
rose.getDetail()
print()
print()