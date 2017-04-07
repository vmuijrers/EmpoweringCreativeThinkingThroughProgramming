## Toets 2 ECTTP Herkansing (07-04-2017):    
De volgende regels zijn van toepassing voor de toets:  
  
- Het is niet toegestaan te communiceren met andere studenten (ook niet via skype, whatsapp etc.)   
- Het is wel toegestaan om eigen code, de slides en internet erbij te houden om dingen op te zoeken.   
- Het is mogelijk om een vraag te stellen aan de surveillanten over de toets, dit wordt geregistreerd en kan je cijfer beinvloeden.   
- Er zijn 3 niveau's, hoe verder je komt, hoe meer punten je kunt scoren; elk nivo vereist ten minste het voorgaande niveau om behaald te worden. 
- Voor deze toets krijg je 90 minuten de tijd   
  
Veel succes!  

##Dodge Pong  
Maak het spel Dodge Pong. Het spel Dodge Pong werkt als volgt: Twee spelers besturen een paddle (blok) net als bij normaal pong, echter kunnen de spelers alleen over de x-as bewegen en niet over de y-as (de Paddles zitten boven en onder in het scherm).    
Er vliegen meerdere ballen door het veld welke moeten worden ontweken door de spelers. Beide spelers hebben 5 levens. Wanneer een paddle wordt geraakt door een bal, gaat er een leven af van de betreffende speler.   
Een speler zonder levens is af. De speler die overblijft wint. Het spel kan dan opnieuw gestart worden.   
Het is toegestaan zelf invulling te geven aan art/toevoegingen te doen en hulpfuncties te schrijven.   

##Basic (V)  
Om het Basic niveau te halen, moet je ten minste de volgende dingen werkend hebben: 
- Een Paddle Class die bestuurbaar is door de speler, deze heeft ten minste de volgende eigenschappen: xPos, yPos, w (width), h (height) en moveSpeed 
- Een Ball Class waarbij tenminste een bal tegen de muren kan kaatsen en in het scherm blijft, deze heeft ten minste de volgende eigenschappen: xPos, yPos, radius, xSpeed en ySpeed 
- Een Score Class, deze heeft ten minste de volgende eigenschappen: hitPointsPlayer1, hitPointsPlayer2 
- Maak tenminste twee Paddle objecten aan (middenboven en middenonder in het scherm) en drie Ball objecten, maak tevens een Score object aan 
- Zorg ervoor dat elke speler een paddle kan besturen met ofwel de pijltjestoetsen (Links, Rechts) of met de A en D (Links, Rechts) 
- Zorg ervoor dat de Ballen bewegen en tegen de muren kaatsen en dus binnen het speelveld blijven 
- Zorg ervoor dat de Score het huidige aantal levens van de spelers laat zien op het scherm 

##Advanced (G)   
Om het Advanced niveau te halen, moet je tenminste de volgende dingen werkend hebben: 
- Gebruik van lijsten voor de Ballen (ten minste 3 ballen) 
- Zorg ervoor dat elke 200 frames, er een nieuwe bal in het spel komt 

##Expert (ZG)  
Om het Expert niveau te halen, moet je ten minste de volgende dingen werkend hebben:
- Voeg Collision toe tussen de ballen en de paddles (gebruik hiervoor de voorbeeld code om Collision te checken tussen een Ball en een Paddle, je kunt deze code toevoegen aan de Ball class) 
- Update de hitPoints van de spelers wanneer er een collision plaats vindt tussen bal en paddle 
- Zorg ervoor dat wanneer een speler geen levens meer heeft, het spel gereset wordt (dit betekent dat de Paddles naar hun oorspronkelijke positie gaan, het aantal ballen weer terug wordt gezet op 3 en de score gereset wordt) 

--Einde toets--  
   
## Inleveren toets:  
  
1. Zorg dat bovenaan je file in een comment je naam, klas en studentnummer staat  
2. Sla je file op met de volgende naam: Toets_2_Herkansing_ECTTP_studentnummer_voornaam_achternaam  
3. Maak van de folder met je pythonbestanden een zip met de volgende naam: Toets_2_Herkansing_ECTTP_studentnummer_voornaam_achternaam  
4. Mail je .zip naar valentijn.muijrers@hku.nl  

