class Dictionary:
    def __init__(self):
        self.words = []

    def loadDictionary(self,path):
        file = open(path,"r",encoding="utf-8")
        for line in file.readlines():
            self.words.append(line.strip())

    def printAll(self,language):
        print(f"Il dizionario {language} contiene:")
        for word in self.words:
            print(word)

    @property
    def dict(self):
        return self.words