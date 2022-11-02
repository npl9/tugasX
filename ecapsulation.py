#Encapsulatiot(Hak Akses)
#public,private,protected

class Ayah:
    _silsilah = 'gledek'

class Anak(Ayah):
    def __init___(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    def cetakSilsilah(self):
        print('silsilah anak adalah: ', self.__silsilah)
    
    def setNama(self, namaBaru):
        self.__nama = namaBaru

    def getNama(self):
        return self.__nama

    @classmethod
    def cetakClassMethod(cls):
        print('ini adalah class method')

anak1 = Anak('budi', 12)

Anak.cetakClassMethod()
