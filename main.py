import spellchecker
sc = spellchecker.SpellChecker()
while True:
    sc.printMenu()
    txtIn = input()
    if not txtIn.isdigit() or (int(txtIn) not in [1,2,3,4]):
        raise ValueError("Valore inserito non valido!!!")
    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")

    elif int(txtIn) == 2:
        print("Enter your sentence in English\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")

    elif int(txtIn) == 3:
        print("Introduce tu frase en Español\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")

    elif int(txtIn) == 4:
        print("Arrivederci!")
        break