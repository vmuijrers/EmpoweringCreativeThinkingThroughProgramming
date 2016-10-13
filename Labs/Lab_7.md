## Lab 7: 
 

##### Grading Matrix 

Trait | Very Good | Good | Acceptable | Unsatisfactory	
--- |--- | --- | --- | --- |
| *Specifications* | The program produces correct results and meets all specifications. | The program works and produces the correct results and displays them correctly. It also meets most of the other specifications. | The program produces correct results but does not display them correctly. | The program is producing incorrect results.
*Readability* | The code is exceptionally well organized and very easy to follow. | The code is fairly easy to read. | The code is readable only by someone who knows what it is supposed to be doing.| The code is poorly organized and very difficult to read.|
*Delivery* |The program was delivered on time. | |  |  The Code was not delivered on time (within one week)


##Exercise 7_0 

Gegeven drie getallen maak een functie genaamd “def round_sum(a,b,c)” die een integer terug geeft waarbij de som van de afronding van de drie getallen worden berekend.  
Hierbij geldt dat een getal wordt afgerond naar zijn dichtstbijzijnde meervoud van 10.  
Als het meest rechtergetal van een getal kleiner dan 5 is, dan wordt er omlaag afgerond naar tienvouden en alshet rechtergetal 5 of groter is, dan wordt er omhoog afgerond naar tienvouden.  
Dus 15 wordt afgerond naar 20 en 32 wordt afgerond naar 30.  
Om herhaling van code te voorkomen, schrijf een hulpfunctie genaamd “def round10(num):” en roep deze 3 keer aan.  
Zorg dat er geen print-aanroepen voorkomen binnen je functies, gebruik deze alleen om het resultaat te printen.

Voorbeeld van outputs:
round_sum(16,17,18)   –>  60
round_sum(22,39,55) –>  120

##Opdracht 7_1: Scrambled Eggs

Gegeven twee woorden, schrijf een functie genaamd “def scramble(word1, word2):” die de worden door elkaar husselt door om en om een letter van elk woord te pakken en daarmee een nieuw woord te vormen.  
Wanneer de twee woorden ongelijk zijn kun je ‘0’ (nul) gebruiken als opvulling.
Zorg dat het gescramblede woord niet eindigt op een ‘0’.

Voorbeeld van outputs:  
scramble(‘scrambled’, ‘eggs’) –> secgrgasm0b0l0e0d  
scramble(‘kipje’,’kaasje’) –> kkiapajsej0e  

hints:
Om de lengte van een woord op te vragen kun je len() gebruiken dus len(‘kipje’)  geeft 5 terug
Om een bepaalde letter op te vragen van een woord kun je (net als bij een tuple) de index gebruiken dus:

Example:   
woord = ‘kipje’  
woord[0] –> ‘k’  
woord[4] –> ‘e’  
woord[5] –> Error!  

##Opdracht 7_2: Unscrambled Eggs

Gegeven een gescrambled woord van Opdracht 7_1, schrijf een functie “def unscramble(word):” ,wat het woord weer opdeelt in twee woorden en een tuple terug geeft met deze twee woorden (als string) als elementen erin.

Voorbeeld van outputs:  
unscramble(‘kkiapajsej0e’)  –> (‘kipje’,’kaasje’)  
unscramble(‘uengsgcsr0a0m0b0l0e0d0’)  –> (‘unscrambled’,’eggs’)  
  
hint: in deze opdracht kun je de modulo operator (%) gebruiken om te testen of iets even of oneven is
 
##INLEVEREN

##Put all of your code into a single sketch and zip your projectfolder, attach the .zip to an email to your lab teacher with the following naming conventions: 

Zipname:
yourname_studentnumber_lab_#.zip 
(voorbeeld: valentijnmuijrers_1337_Lab_04d.zip)

Email name:
INLEVEREN: ECTTP_Lab_#_Voornaam_Achternaam_StudentNummer
(voorbeeld: INLEVEREN: ECTTP_Lab_1_Valentijn_Muijrers_1337)

##DO NOT SEND A RAR, THE MAIL CLIENT WILL NOT ACCEPT THIS

##Due Date 

Turn each lab in before the next lab (one week later). 
