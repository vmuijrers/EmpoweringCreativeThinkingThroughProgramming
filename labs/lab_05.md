## Lab 5: 
 
##### Naming conventions 

Put all of your homework files together into one folder, zip it and email it to your lab assistant with your name_the week.zip 

** Make the subject of the email "INLEVEREN: lab 5" **

**for example:** 
phoenixperry_02.zip


##### Due Date 

Turn each lab no later than 24 hours after the lab session. 

##### Grading Matrix 

Trait | Very Good | Good | Acceptable | Unsatisfactory	
--- |--- | --- | --- | --- |
| *Specifications* | The program produces correct results and meets all specifications. | The program works and produces the correct results and displays them correctly. It also meets most of the other specifications. | The program produces correct results but does not display them correctly. | The program is producing incorrect results.
*Readability* | The code is exceptionally well organized and very easy to follow. | The code is fairly easy to read. | The code is readable only by someone who knows what it is supposed to be doing.| The code is poorly organized and very difficult to read.|
*Delivery* | The program was delivered on time. | The program was delivered within a week of the due date. | The code was within 2 weeks of the due date. | The code was more than 2 weeks overdue but no later than 3 weeks overdue. |
*Attendance* | You attended the lab. | You attended the lab but came late or left early. | You emailed your work in ahead of time but did not attend the lab. | You did not attend and you turned your work in on time |

**After 3 weeks, you immediately get a fail for this lab. 


##Opdracht 5_1: Round Sum

Gegeven drie getallen maak een functie genaamd “def round_sum(a,b,c)” die de som van de afronding van de drie getallen berekent en terug geeft. Hierbij geldt dat een getal wordt afgerond naar zijn dichtstbijzijnde meervoud van 10. Als het meest rechtergetal van een getal kleiner dan 5 is, dan wordt er omlaag afgerond naar tienvouden en alshet rechtergetal 5 of groter is, dan wordt er omhoog afgerond naar tienvouden. Dus 15 wordt afgerond naar 20 en 32 wordt afgerond naar 30.  Om herhaling van code te voorkomen, schrijf een hulpfunctie genaamd “def round10(num):” en roep deze 3 keer aan. Zorg dat er geen print-aanroepen voorkomen binnen je functies, gebruik deze alleen om het resultaat te printen.

Voorbeeld van outputs:

round_sum(16,17,18)   –>  output: 60

round_sum(22,39,55) –>  output: 120

 

##Opdracht 5_2: Scrambled Eggs

Gegeven twee woorden, schrijf een functie genaamd “def scramble(word1, word2):” die de worden door elkaar husselt door om en om een letter van elk woord te pakken en daarmee een nieuw woord te vormen. Wanneer de twee woorden ongelijk zijn kun je ‘0’ (nul) gebruiken als opvulling.

Voorbeeld van outputs:

scramble(‘scrambled’, ‘eggs’) –> output: secgrgasm0b0l0e0d0

scramble(‘kipje’,’kaasje’) –> output:  kkiapajsej0e

hints:

om de lengte van een woord op te vragen kun je len() gebruiken dus len(‘kipje’)  geeft 5 terug

om een bepaalde letter op te vragen van een woord kun je (net als bij een tuple) de index gebruiken dus:

woord = ‘kipje’

woord[0] –> ‘k’

woord[4] –> ‘e’

woord[5] –> Error!

#bonus:

zorg dat het gescramblede woord niet eindigt op een ‘0’

##Opdracht 5_3: Unscrambled Eggs

Gegeven een gescrambled woord van Opdracht 5_2, schrijf een functie “def unscramble(word):” ,wat het woord weer opdeelt in twee woorden en een tuple terug geeft met deze twee woorden als elementen erin.

Voorbeeld van outputs:

unscramble(‘kkiapajsej0e’)  –> output: (‘kipje’,’kaasje’)

unscramble(‘uengsgcsr0a0m0b0l0e0d0’)  –> output: (‘unscrambled’,’eggs’)

hint: in deze opdracht kun je de modulo operator (%) gebruiken om te testen of iets even of oneven is

 

Mail je resultaten naar je lab begeleiders, zorg dat je alles als losse .py files zipt.

Voor vragen of onduidelijkheden, mail naar valentijn.muijrers@hku.nl

#Voor Extra oefeningen kijk op:
Codingbat.com/Python
