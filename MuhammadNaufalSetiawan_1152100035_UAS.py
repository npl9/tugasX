import string


class Penjual : 
    def __init__(self, nama, id):
        self.nama = nama
        self.id = id

class Pembeli :
    def __init__(self, namaBuyer, barangBelanja):
        self.namaBuyer = namaBuyer
        self.barangBelanja = barangBelanja

class Catalog :
    def __init__(self, catalog):
        self.catalog = list("ayam", "cabe", "pisang")

def main():
    rian = Penjual("Rian", "9701782")
    nopal = Pembeli("Naufal", "Ayam")
    catalog = list

main()
