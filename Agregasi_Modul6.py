class Karyawan():
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
    
    def gajian(self, honor):
        totalGaji = honor.gajiPokok + honor.tunjangan + honor.lembur
        totalGaji =  totalGaji - honor.pajak
        print(self.nama, "Mendapatkan Honor sebanyak", totalGaji)

class Honor():
    def __init__(self, gajiPokok, tunjangan, lembur, pajak):
        self.gajiPokok = gajiPokok
        self.tunjangan = tunjangan
        self.lembur = lembur
        self.pajak = pajak

def main():
    nopal = Karyawan("Naufal", "035")
    honor = Honor(10000000, 2500000, 1000000, 1500000)
    nopal.gajian(honor)
main()    