## Lab 9: 
 
##### Grading Matrix 

Trait | Very Good | Good | Acceptable | Unsatisfactory	
--- |--- | --- | --- | --- |
| *Specifications* | The program produces correct results and meets all specifications. | The program works and produces the correct results and displays them correctly. It also meets most of the other specifications. | The program produces correct results but does not display them correctly. | The program is producing incorrect results.
*Readability* | The code is exceptionally well organized and very easy to follow. | The code is fairly easy to read. | The code is readable only by someone who knows what it is supposed to be doing.| The code is poorly organized and very difficult to read.|

## Blocker Ball!  
## Basic  

Add the Ball-class from the previous lab to your project, add a new parameter called playerNumber and color. 
Make sure at least two ball objects are instantiated during the setup and give them the correct arguments, one for player 1 (Red) and one for player 2 (Blue).
Set the PlayerNumbers accordingly.
Make sure the different colours are shown for each ball and put the balls in a list.  
Make sure you only use the list to control the balls and do not use separate variables for each ball.  
  
## Advanced  

Make a class called Blocker which has the following attributes: xPos, yPos, radius.  
Add the methods display(self) and collide(self, ball) to the Blocker class.
Make it so that when you click the left mouse button, a circular blocker is placed in the scene on the mouse position, also add each blocker object to a list (this is a separate list from the balls).
Implement the collide-function, hint: use the distance-function for the positions of the ball and the blocker to check if the two circles are close enough to collide.
If there is a collision between a ball and a blocker, reverse the speed of the ball.

Hint: Create a double for-loop in the draw of the main tab, one for the balls and the second one for the blockers. check for each ball and each blocker if there is a collision.

## Expert  

Make a third class called Score and instantiate exactly one object of this class. 
The score class keeps score for both players (think of which attributes and methods this class will need).  
Create a Score object and make sure that if a Red ball hits a blocker, Player 1 gets a point and if a Blue ball hits a blocker, Player 2 gets a point.
Show the scores on screen.  
Hint: To add a score, add an extra parameter to the collide-function the blocker class and give the score object to the function. From within the collide function, it is now possible to add a score to the score object if there is a collision.


## INLEVEREN

## Put all of your code into a single sketch and zip your projectfolder, submit it online in the tool (http://www.elvishasleftthebuilding.nl/geni/)

Zipname:
ECTTP_homework_achternaam_voornaam_labnr.zip 
(voorbeeld: ECTTP_homework_muijrers_valentijn_7.zip )

