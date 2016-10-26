## Toets 1b ECTTP (26-10-2016):   
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
Schrijf een functie genaamd five_percent(number), die terug geeft True teruggeeft (boolean) wanneer "number" kleiner of gelijk aan 5 is of groter of gelijk aan 95 is, anders geeft de functie False terug.
number is een integer tussen de 0 en 100.  

Voorbeelden:    
five_percent(4) -> True    
five_percent(61) -> False    
five_percent(95) -> True    
 
# Vraag 2 - If-statements (4 punten)    
Schrijf een functie genaamd maxSpeed(passengers, isBig), die aangeeft hoe hard je mag varen met een boot.
Return een string waarbij het volgende geldt:
return "no passengers" wanneer het aantal passengers gelijk is aan 0
return "100 mph" wanneer de boot groot is en het aantal passengers kleiner of gelijk aan 30 (en groter dan 0).
return "50 mph" wanneer de boot groot is en het aantal passengers groter dan 30 (en groter dan 0).
return "75 mph" wanneer de boot niet groot is en het aantal passengers kleiner of gelijk aan 15 (en groter dan 0).
return "30 mph" wanneer de boot niet groot is en het aantal passengers groter dan 15 (en groter dan 0).
passengers is een integer die aangeeft hoeveel passagiers er op de boot zijn.
isBig is een boolean die aangeeft of het schip groot is (True is groot, False is niet groot)

Voorbeelden:   
maxSpeed(10, True) -> "100 mph"  
maxSpeed(0, True) -> "no passengers"  
maxSpeed(17, False) -> "30 mph"   

	
# Vraag 3 - Loops (4 punten)
Schrijf een functie genaamd lasthalfword(inputString), die gegeven een inputString met een even aantal letters, een string teruggeeft (return)
wat de tweede helft is van de inputString.  

Voorbeelden:  
halfwoord("WooHoo") -> "Woo"    
halfwoord("yaya") -> "ya"  
halfwoord("abcdef") -> "def"  
 
# Vraag 4 - Booleans  (4 punten)
Schrijf een functie genaamd warm(isRaining, isSummer, isInside), die True teruggeeft wanneer het warm is en anders False.
In de zomer is het warm, tenzij het regent.
Als het geen zomer is, is het warm als je binnen zit.
In alle andere gevallen is het niet warm.

isRaining is een boolean die aangeeft of het regent.
isSummer is een boolean die aangeeft of het zomer is.
isInside is een boolean die aangeeft of je binnen zit.

Voorbeelden:  
warm(True, False, True) -> True  
warm(False, True, False) -> True  
warm(True, True, False) -> False  
	
# Vraag 5 - Modulo (4 punten)
Schrijf een functie biggestWaste(nummer1, nummer2, nummer3), die de rest terug geeft (Integer) van de drie inputs.
De rest van een getal is het meest rechtse getal van een cijfer, dus 31 -> 1.  42 -> 2.
Hierbij zijn nummer1, nummer2 en nummer3 integers.

Voorbeelden:  
biggestWaste(31, 52 ,  76) -> 6  
biggestWaste(98, 103, 216) -> 8  
biggestWaste( 6, 14 ,  12) -> 6  

 
--Einde toets--  
   
## Inleveren toets:  
  
1. Zorg dat bovenaan je file in een comment je naam, klas en studentnummer staat  
2. Zorg dat bij elke Vraag een comment staat welke Vraag het is (dus bijvoorbeeld #Vraag 1)  
3. Sla je file op met de volgende naam: Toets_1b_ECTTP_studentnummer_voornaam_achternaam  
4. Maak van de folder met je pythonbestanden een zip met de volgende naam: Toets_1_ECTTP_studentnummer_voornaam_achternaam  
5. Mail je .zip naar valentijn.muijrers@hku.nl  

