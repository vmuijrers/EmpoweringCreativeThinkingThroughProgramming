## Toets 1 ECTTP (21-10-2016):   
De volgende regels zijn van toepassing voor de toets:  
  
- Het is niet toegestaan te communiceren met andere studenten (ook niet via skype, whatsapp etc.)  
- Het is wel toegestaan om eigen code, de slides en internet erbij te houden om dingen op te zoeken.  
- Het is mogelijk om een vraag te stellen aan de surveillanten over de toets, dit wordt geregistreerd en kan je cijfer beinvloeden.  
- Per vraag kun je 4 punten verdienen, niet-werkende onderdelen geven punten aftrek
- Je hoeft voor deze toets geen setup() en draw() functies te gebruiken! (je wordt er niet op afgerekend wanneer je dit wel doet).
- Er zijn 5 vragen, lees de vragen goed door voordat je iets opschrijft, je hoeft niks te printen (mag wel als test) tenzij dit expliciet wordt gevraagd  
- Voor deze toets krijg je 90 minuten de tijd  
  
Veel succes!  
  
# Vraag 1 - Variabelen (4 punten) 
Schrijf een functie genaamd inrange(input, laag, hoog), die terug geeft (boolean) of het input getal tussen de laag (inclusief) en hoog getallen ligt (inclusief).
input is een integer.  
laag is een integer.  
hoog is een integer.  
Je mag er vanuit gaan dat "laag" altijd lager is dan "hoog".

Voorbeeld:  
inrange(3, 1, 7) -> True  
inrange(5, 10, 12) -> False  
inrange( 16, 1, 15 -> False  
  
# Vraag 2 - If-statements (4 punten)    
Schrijf een functie genaamd party(bezoekers, obers, isZondag), die een boolean terug geeft, waarbij de functie True terug geeft wanneer er genoeg obers zijn voor het aantal bezoekers.  
Wanneer er niet genoeg obers zijn geeft de functie False terug.  
Een ober kan 8 bezoekers bedienen tenzij het zondag is, dan kan een ober maar 5 bezoekers bedienen.    
bezoekers is het aantal bezoekers op de party(integer).    
obers is het aantal obers(integer).    
isZondag geeft aan of het een zondag is (boolean).    
  
Voorbeelden:  
party(62, 5, False) -> False  
party(80, 10, True) -> False  
party(40, 20, True) -> True  
  	
# Vraag 3 - Loops (4 punten)
Schrijf een functie genaamd halfwoord(inputString), die gegeven een inputString met een even aantal letters, een string teruggeeft (return)
wat de eerste helft is van de inputString.  

Voorbeelden:  
halfwoord("WooHoo") -> "Woo"    
halfwoord("yaya") -> "ya"  
halfwoord("abcdef") -> "abc"  
 
# Vraag 4 - Booleans  (4 punten)
Schrijf een functie genaamd paraplu(isRaining, heeftRegenpak, isInside), die True teruggeeft wanneer je een paraplu nodig hebt en anders False.
Wanneer het regent heb je een paraplu nodig tenzij je binnen bent of tenzij je een regenpak hebt.

isRaining is een boolean die aangeeft of het regent.
heeftRegenpak is een boolean die aangeeft of je en regenpak aan hebt.
isInside is een boolean die aangeeft of je binnen bent.

Voorbeelden:  
paraplu(True, False, False) -> True  
paraplu(True, True, False) -> False  
paraplu(False, False, True) -> False  
paraplu(True, False, True) -> False  
	
# Vraag 5 - Modulo (4 punten)
Scrijf een functie genaamd rondaf(nummer), die een getal teruggeeft wat afgerond is op een tiental.
Hierbij geldt dat een getal groter of gelijk aan 5 wordt naarboven afgerond en kleiner dan 5 wordt naar beneden afgerond.

Voorbeelden:  
rondaf(15) -> 20  
rondaf(3) -> 0  
rondaf(7) -> 10  
  
--Einde toets--  
   
## Inleveren toets:  
  
1. Zorg dat bovenaan je file in een comment je naam, klas en studentnummer staat  
2. Zorg dat bij elke Vraag een comment staat welke Vraag het is (dus bijvoorbeeld #Vraag 1)  
3. Sla je file op met de volgende naam: Toets_1_ECTTP_<studentnummer>_<voornaam>_<achternaam>  
4. Maak van de folder met je pythonbestanden een zip met de volgende naam: Toets_1_ECTTP_<studentnummer>_<voornaam>_<achternaam>  
5. Mail je .zip naar de begeleider van de werkcolleges:  
Klas:  
A -> valentijn.muijrers@hku.nl  
B -> ton.markus@hku.nl  
C -> aaron.oostdijk@hku.nl  
D -> vincent.booman@hku.nl  
