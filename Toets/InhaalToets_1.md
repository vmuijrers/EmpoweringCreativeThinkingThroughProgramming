## InhaalToets 1 ECTTP (16-11-2016):   
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
Schrijf een functie genaamd DifferenceMinMax(number1, number2, number3), die een integer terug geeft die aangeeft wat het verschil is tussen het grootste en het kleinste getal.  

Voorbeelden:    
DifferenceMinMax(6, 2,  5) -> 4    
DifferenceMinMax(38,16, 50) -> 34    
DifferenceMinMax(3, 78, 101) -> 98    
 
# Vraag 2 - If-statements (4 punten)
Twee dieven overvallen een bank, maar worden aangehouden en verhoord.  
Dief 1 kan Dief 2 verraden om een lagere celstraf te krijgen, tenzij de andere dief dat ook doet.  
Schrijf een functie genaamd Prisoner(Dief_1, Dief_2), die een integer terug geeft, die aangeeft hoeveel jaar celstraf Dief 1 krijgt.    
De celstraf wordt op de volgende manier bepaald:  
Als Dief 1 Dief 2 beschuldigt en Dief 2 beschuldigt niemand, dan moet de functie 3 teruggeven (3 jaar celstraf voor Dief 1)  
Als Dief 1 Dief 2 beschuldigt en Dief 2 beschuldigt Dief 1, dan moet de functie 5 teruggeven (5 jaar celstraf voor beide dieven)  
Als Dief 1 niemand beschuldigt en Dief 2 beschuldigt niemand, dan moet de functie 2 teruggeven (2 jaar celstraf voor beide dieven)  
Als Dief 1 niemand beschuldigt en Dief 2 beschuldigt Dief 1, dan moet de functie 7 teruggeven (7 jaar celstraf voor Dief 1)  

Hierbij geldt dat:  
Dief_1 is een Boolean die aangeeft of Dief_1 de andere dief beschuldigd 
Dief_2 is een Boolean die aangeeft of Dief_2 de andere dief beschuldigd

Voorbeelden:   
Prisoner(True, True) -> 5  
Prisoner(True, False) -> 3 
Prisoner(False, False) -> 2  
Prisoner(False, True) -> 7   

	
# Vraag 3 - Loops (4 punten)  
Schrijf een functie genaamd Awesome(inputString), die gegeven een inputString, een string teruggeeft (return) waarbij elke letter "a" die voorkomt in het woord wordt vervangen door het woord "Awesome".  
    
Voorbeelden:  
Awesome("WooHoo") -> "WooHoo"    
Awesome("yaya") -> "yAwesomeyAwesome"  
Awesome("abcdef") -> "Awesomebcdef"  
 
# Vraag 4 - Booleans  (4 punten)  
Schrijf een functie genaamd Cola(isWeekend, isTired, isEvening), die True teruggeeft wanneer het een goed idee is om cola te drinken en anders False.  
Als je moe bent is het een goed idee om cola te drinken tenzij het avond is.
Als het weekend is, is het altijd een goed idee om cola te drinken. 
In alle andere gevallen is het geen goed idee om cola te drinken.

isWeekend is een boolean die aangeeft of het weekend is.  
isTired is een boolean die aangeeft of je moe bent.  
isEvening is een boolean die aangeeft of het avond is.  

Voorbeelden:  
Cola(True, False, True) -> True  
Cola(False, True, False) -> True  
Cola(True, True, False) -> True  
Cola(False, False, True) -> False 
	
# Vraag 5 - Modulo (4 punten)  
Schrijf een functie genaamd EvenModulo(number, mod), die een boolean terug geeft, wanneer de rest van de modulo die je over houdt, even is. 
Dus EvenModulo (18, 4) -> 18 modolo 4 geeft 2, 2 is even dus return True.   
Hierbij is number een integer.  
Hierbij is mod een integer die de modulo waarde representeert.  

Voorbeelden:  
EvenModulo(18, 4) ->  True  
EvenModulo(105, 5) -> True  
EvenModulo( 21, 5) -> False  

 
--Einde toets--  
   
## Inleveren toets:  
  
1. Zorg dat bovenaan je file in een comment je naam, klas en studentnummer staat  
2. Zorg dat bij elke Vraag een comment staat welke Vraag het is (dus bijvoorbeeld #Vraag 1)  
3. Sla je file op met de volgende naam: InhaalToets_1_ECTTP_studentnummer_voornaam_achternaam  
4. Maak van de folder met je pythonbestanden een zip met de volgende naam: InhaalToets_1_ECTTP_studentnummer_voornaam_achternaam  
5. Mail je .zip naar valentijn.muijrers@hku.nl  

