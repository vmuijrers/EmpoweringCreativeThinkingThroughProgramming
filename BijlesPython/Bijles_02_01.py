__author__ = 'Student'

#functie: def
#vervolgens de naam die je later gaat aanroepen
#afsluiten met ():
#let op de tabjes
def TestFunctie():
    print "test"

#aanroepen van de functie:
TestFunctie()

#functie met 1 parameter genaamd 'text'
#binnen de tabjes van de functie kan een parameter gebruik worden
# daar buiten niet
def FunctieMetParameter(eenparameter):
    print eenparameter

#2 dezelfde functies met andere parameters
FunctieMetParameter("wat ik hier type")
FunctieMetParameter("is iets anders dan hierboven")
#kan ook iets anders zijn als text:
FunctieMetParameter(6)

#een functie kan meerdere parameters hebben:
def AndereFunctieMetParameters(a,b,c):
    print a
    print b
    print c


#voorbeeld van een functie die iets terugstuurt (return)
def PlakBeerVoorWoord(woord):
    nieuwWoord = "beer"+woord
    return nieuwWoord

#bij een return, veranderd de functienaam in alles achter de return
print PlakBeerVoorWoord("appelsap")
print PlakBeerVoorWoord("beer")
print PlakBeerVoorWoord("weer")

def PlakWoordVoorWoord(woord1, woord2):
    nieuwWoord = woord1 + woord2
    return nieuwWoord


print PlakWoordVoorWoord("grote ", "beer")
print PlakWoordVoorWoord("beer ", "Tom")
print PlakWoordVoorWoord("katje ", "Paul")
#een gereturnde variable zou je kunnen opslaan voor later gebruik
naam = PlakWoordVoorWoord("Dit is ", "een nieuwe zin.")
print naam

#max() is bijvoorbeeld een ingebouwde functie van Python

#voorbeeld waarbij een functie weer in een ifstatement gebruikt wordt
def IsGetalVijf(getal):
    if(getal == 5):
        return True
    else:
        return False

getal = 5
if(IsGetalVijf(getal)):
    print "Dit is een vijf."
else:
    print "Dit is een geen vijf."
#einde van vorig genoemd voorbeeld

#een voorbeeld opdracht over returns en functies in de volgende file