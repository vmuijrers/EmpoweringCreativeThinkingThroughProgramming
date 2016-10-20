Regels voor de toets
- studenten mogen alleen vragen stellen aan de studentassisten/begeleiders, het is niet toegestaan om te communiceren met andere studenten (ook niet via facebook/whatsapp etc.)
- studenten mogen hun aantekeningen/slides/internet erbij houden om dingen op te zoeken
- wanneer een student een vraag stelt wordt genoteerd wat voor soort vraag het is (begrip of syntax), dit wordt later meegenomen in de beoordeling

Let op: Lees de vragen eerst goed door en kijk goed naar wat er precies wordt gevraagd als output, je hoeft alleen de definitie van de gevraagde functies te geven, try-except, print en raw_input zijn niet nodig!

Toets 1:

Vraag 1: Loops
Schrijf een functie genaamd "optelsom(begingetal, eindgetal):", die een integer terug geeft, waarbij het volgende geldt:
Het begingetal is altijd kleiner dan het eindgetal (hier mag je van uit gaan).
De functie geeft de som terug van alle tussenliggende getallen, inclusief het begingetal en inclusief het eindgetal.

voorbeelden van output:  
optelsom(4,6) > 4+5+6 = 15  
optelsom(0,4) > 0+1+2+3+4 = 10  

Oplossing:  

def optelsom(begin, eind):
	result = 0
	for i in range(begin, eind+1):
		result += i
	return result


Vraag 2: Booleans
Schrijf een functie genaamd "def alarm_klok(dag, vakantie):", die een string teruggeeft, waarbij het volgende geldt:
Voor de dagen geldt: maandag =1, dinsdag =2, woensdag =3, donderdag =4, vrijdag =5, zaterdag = 6 en zondag =7
Als het weekend is (zaterdag of zondag) en we zijn op vakantie dan willen we niet op staan en zetten we het alarm op "off"
Als het weekend is (zaterdag of zondag) en we zijn niet op vakantie dan willen we op staan om "10:00"
Als het doordeweeks is (ma t/m vr) en we zijn niet op vakantie dan willen we om "7:00" op staan
Als het doordeweeks is (ma t/m vr) en we zijn wel op vakantie dan willen we om "10:00" op staan

Let op! Zorg dat je functie een waarde terug geeft, dus gebruik het keywoord 'return' en dan de tijd waarop je op wilt staan of dat de klok op "off" staat
Je hoeft niks te printen voor deze functie.

voorbeelden van output:  
alarm_klok(3,True) >>> "10:00"  
alarm_klok(3,False) >>> "7:00" 
alarm_klok(7,True) >>> "off"  
alarm_klok(6,False) >>> "10:00"  

Oplossing:  
def alarm_klok(dag, vakantie):  
	if dag <= 5 and vakantie or dag >5 not vakantie:  
		return "10:00"  
	elif dag <=5 and not vakantie:  
		return "7:00"  
	else:  
	#in alle andere gevallen (dus wanneer het weekend is en we op vakantie zijn)  
		return "off"  


Vraag 3: Modulo
Schrijf een functie genaamd "def rondom_tien(nummer):", die een boolean terug geeft, waarbij het volgende geldt:
De functie geeft True terug wanneer het nummer (deze is altijd positief) twee of minder verschilt van een tiental (tientallen zijn 0, 10, 20 etc.)
In alle andere gevallen geeft de functie False terug.

Voorbeelden van output:  
rondom_tien (12) >>> True  
rondom_tien (9) >>> True  
rondom_tien (14) >>> False  
rondom_tien (2) >>> True  

Hint: je kunt hierbij de modulo operator (%) gebruiken, welke de rest berekent wanneer twee getallen op elkaar worden gedeeld, dus 12 % 5 = 2

Oplossing:  
def rondom_tien(nummer):  
	rest = nummer % 10 # bereken eerst de restwaarde met modulo 10  
	return rest <= 2 or rest >= 8  #geef vervolgens True terug wanneer de rest kleiner of gelijk aan twee is of groter of gelijk aan 8   

Vraag 4: Strings
Schrijf een functie genaamd "def dubbele_letters(woord):", die een string teruggeeft, waarbij elke letter in de originele input wordt herhaald:

voorbeeld output:
dubbele_letters('The') >>> 'TThhee'
dubbele_letters('AAbb') >>> 'AAAAbbbb'
dubbele_letters('Hi-There') >>> 'HHii--TThheerree'

Oplossing:  
def dubbele_letters(woord):  
	result = ""  
	for i in range(0,len(woord)):  
		result += woord[i] + woord[i]  
	
	return result  

Wanneer je klaar bent met de toets kun je je resultaat in een .zip bestand opslaan (je kun alle opdrachten in 1 .py file opslaan met als naam <Voornaam><Achternaam>_Toets_1.py) en deze kun je versturen naar je practicum begeleider. Vermeld bij het onderwerp van je email het volgende: INLEVEREN: ECTTP Toets 1 <Voornaam><Achternaam> en mail deze, je mag pas gaan als er is gecontroleerd of je toets goed is aangekomen bij de docenten
