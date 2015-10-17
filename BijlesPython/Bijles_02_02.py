__author__ = 'Student'

#opdracht 4_1 uit de lessen:
#het berekenen van het aantal wielen

#met += of -= of /= of *= kan je:
#voorbeeld += 1
#maar is hetzelfde als
#voorbeeld = voorbeeld + 1

def Wheels(cars, tris, bikes):
    totaalAantalWielen = 0
    #gebruik van +=
    totaalAantalWielen += cars * 4
    totaalAantalWielen += tris * 3
    totaalAantalWielen += bikes * 2
    #vervolgens returnen!, niet uitprinten
    return totaalAantalWielen

#parameters binnen een functie en die je invult wanneer je de functie aanroept
#hoeven niet hetzelfde te heten. (voor jezelf ook makkelijker)
autos = int(raw_input("Hoeveel autos heb je?"))
driewielen = int(raw_input("Hoeveel driewielers heb je?"))
fietsen = int(raw_input("Hoeveel fietsen heb je?"))

#dus vervolgens de gevraagde antwoorden doorvoeren in Wheels()
wielenInMijnGarage = Wheels(autos, driewielen, fietsen)
#om te testen:
#Wheels() returned een getal (int), maar print verwacht hier een string
print "Ik heb " + str(wielenInMijnGarage) + " wielen in mijn garage."
