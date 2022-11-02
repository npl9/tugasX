class Bank:
    pass

class swasta(Bank):

    def __init__(self, nama):
        self.__namaBank = namaBank

    def setBank(self, namaBankBaru):
        self.__namaBank = namaBankBaru

    def getBank(self):
        return self.__namaBank

bank1 = Bank('Maybank')
print(bank1.getBank())

