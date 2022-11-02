from codecs import namereplace_errors
from http.client import NOT_ACCEPTABLE


class SecretRoom():
    def __init__(self, name):
        self.name = name
        self.id = AccessCard(8663286382, "B023")


class AccessCard():
    def __init__(self, noId, accessCode):
        self.noId = noId
        self.accessCode = accessCode
    
    def cetakKartu(self):
        print("Id Number:", self.noId, "with Access Code", self.accessCode)

def main():
    nopal = SecretRoom("Naufal")
    nopal.id.cetakKartu()

main()

