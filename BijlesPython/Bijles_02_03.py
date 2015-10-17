__author__ = 'Student'
#lab 5 opdracht 2: (the infamous) Scrambled Eggs
#samenvatting: het gebruiken van een array binnen een forloop in een functie

#onze pseudocode om te beginnen:
#een nieuwe functie die def Scramble heet met 2 parameters (woord1 en woord2)
    #een nieuwe variable maken voor het gescramble woord
    #een for loop maken om om-en-om letters toe te voegen
    #return het gescramble woord
#einde pseudocode

#deze functie staat boven Scramble(), want Python ;-;
def GeefLetterOfNul(woord, positie):
    #wanneer de positie die we willen checken, groter is dan het woord lang is
    if positie >= len(woord):
        return "0"
    else:
        #anders de letter op positie terug sturen
        return woord[positie]

#bovenstaande pseudocode uitgewerkt:
def Scramble(word1, word2):
    #wederom eerst aanmaken en vertellen dat hij een lege string is
    scrambledword = ""
    #kijken welk woord het langste is:
    lettersInLangsteWoord = max(len(word1), len(word2))
    #voor for loops, koop een premium account of kijk in bijles #1
    for letter in range(0, lettersInLangsteWoord):
        #letter op plek nr 0 pakken uit word1, en vervolgens toevoegen
        scrambledword += GeefLetterOfNul(word1, letter)
        #omdat we willen ritsen:
        scrambledword += GeefLetterOfNul(word2, letter)

    #het returnen van het nieuwe woord, note: het tabje staat binnen de functie, maar buiten de forloop
    return scrambledword

#print kipje[234]
geschudWoord = Scramble("kipje", "autogarage")
print geschudWoord
