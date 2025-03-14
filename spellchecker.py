import time
import multiDictionary as md

class SpellChecker:
    def __init__(self):
        self.m = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        sentence_by_words = []
        txtIn = replaceChars(txtIn)
        for i in txtIn.split(" "):
            sentence_by_words.append(i.lower())
        start_time = time.time()
        wrong_words = self.m.searchWord(sentence_by_words, language)
        end_time = time.time()
        start_time1 = time.time()
        wrong_words1 = self.m.searchWordLinear(sentence_by_words, language)
        end_time1 = time.time()
        start_time2 = time.time()
        wrong_words2 = self.m.searchWordDichotomic(sentence_by_words, language)
        end_time2 = time.time()
        print("Ricerca semplice:")
        self.m.print_wrong_words(wrong_words,end_time - start_time)
        print("Ricerca lineare:")
        self.m.print_wrong_words(wrong_words1,end_time1 - start_time1)
        print("Ricerca dicotomica:")
        self.m.print_wrong_words(wrong_words2, end_time2 - start_time2)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

def replaceChars(text):
    import string
    characters = string.punctuation
    for c in characters:
        text = text.replace(c, "")
    text = text.lower()
    return text