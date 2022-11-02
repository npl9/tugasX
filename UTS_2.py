class dosen:
    def nama_dosen (self, nama, mata_kuliah):
        self.nama = nama
        self.mata_kuliah = mata_kuliah

class Mahasiswa:
    def nama_mahasiswa (self, nama, nrp):
        self.nama = nama 
        self.nrp = nrp

class mataKuliah:
        jumlah_tugas = 0

mahasiswa = Mahasiswa('Muhammad Naufal Setiawan','1152100035')
print(mahasiswa.mahasiswa)
print(mahasiswa.jumlah_tugas)
