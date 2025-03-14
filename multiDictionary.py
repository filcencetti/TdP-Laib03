import dictionary as d
import richWord as rw

class MultiDictionary:
    def __init__(self):
        self.ita = d.Dictionary()
        self.eng = d.Dictionary()
        self.spa = d.Dictionary()
        self.ita.loadDictionary("resources/Italian.txt")
        self.eng.loadDictionary("resources/English.txt")
        self.spa.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language == "Italian":
            self.ita.printAll(language)
        elif language == "English":
            self.eng.printAll(language)
        elif language == "Spanish":
            self.spa.printAll(language)

    def searchWord(self, words_1, language):
        self.wrongs = []
        if language == "italian":
            self.word_list = self.ita.words
        elif language == "english":
            self.word_list = self.eng.dict
        elif language == "spanish":
            self.word_list = self.spa.dict
        for word in words_1:
            self.word_wrong = rw.RichWord(word)
            if self.word_list.__contains__(word):
                self.word_wrong.corretta = True
            if not self.word_list.__contains__(word):
                self.wrongs.append(word)
        return self.wrongs

    def searchWordLinear(self,words_1, language):
        self.wrongs = []
        if language == "italian":
            self.word_list = self.ita.words
        elif language == "english":
            self.word_list = self.eng.dict
        elif language == "spanish":
            self.word_list = self.spa.dict
        for word in words_1:
            self.word_wrong = rw.RichWord(word)
            for word_dict in self.word_list:
                if word == word_dict:
                    self.word_wrong.corretta = True
            if self.word_wrong.corretta == False:
                self.wrongs.append(word)
        return self.wrongs

    def searchWordDichotomic(self,words_1, language):
        self.wrongs = []
        if language == "italian":
            self.word_list = self.ita.words
        elif language == "english":
            self.word_list = self.eng.dict
        elif language == "spanish":
            self.word_list = self.spa.dict
        if len(self.word_list)%2 == 0 :
            half_ind = int(len(self.word_list)/2)
            mean_value = self.word_list[half_ind]
            first_half = self.word_list[:half_ind-1]
            second_half = self.word_list[half_ind+1:]
        else:
            half_ind = int(len(self.word_list)-1/ 2)
            mean_value = self.word_list[half_ind]
            first_half = self.word_list[:half_ind -1]
            second_half = self.word_list[half_ind+1:]

        for word in words_1:
            self.word_wrong = rw.RichWord(word)
            if word == mean_value:
                self.word_wrong.corretta = True
            elif word > mean_value:
                for word_dict in second_half:
                    if word == word_dict:
                        self.word_wrong.corretta = True
            elif word < mean_value:
                for word_dict in first_half:
                    if word == word_dict:
                        self.word_wrong.corretta = True
            if self.word_wrong.corretta == False:
                self.wrongs.append(word)
        return self.wrongs

    def print_wrong_words(self,wrong_words,time):
        if len(wrong_words)==0:
            print("Zero errori :-)")
        else:
            print("Using contains:")
            for word in wrong_words:
                print(word)
            print(f"Numero di parole sbagliate: {len(wrong_words)}")
            print(f"Tempo di esecuzione: {time}")
            print("------------------------------------------------")