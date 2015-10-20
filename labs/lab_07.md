## Lab 7: 
 
##### Naming conventions 

Put all of your homework files together into one folder, zip it and email it to your lab assistant with your name_the week.zip 

** Make the subject of the email "INLEVEREN: lab 7" **

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

Download Processing 2.2.1 from processing.org
## You need only one processing project for this lab, each exercise extends the previous exercises!

#7_1: Don't be Square!

In Processing:
First create a new project, and save your project and name it "mySquareProject", your main tab will now have the same name. (You will only need 2 tabs in your project)  
Then create a class named "Square(object)" in a new tab named "MySquareTab", which has the following attributes: x (x-position),y (y-position), w (width), h (height), col (color). 
Also give the Square class the method "def display", this is where you draw the square to the screen.
If you created your class in a separate file, use "from MySquareTab import Square" in your main sketch, to access the Square class.
Make sure you create one instance of the Square class in your main sketch file by calling "Square(xPos,yPos,width,height, col)"
Hint: you can create a color as follows: color(value,value,value) in order red, green, blue with values between 0 and 255. So c = color(255,100,125) and then Square(100,200,100,100,c) (this is an example).

#7_2: Random Squares!

In the same project, create a list of 200 squares in "mySquareProject" by creating 200 Square objects which you created in 7_1 with different x and y positions and widths and heights and colors (you may need a for-loop to do this).
Hint: to get different values for every square you can use the random(0, maxRange) function to get a random value between 0 and maxRange.

#Bonus: 7_3: Marching Squares!

Now add a method to your Square class named "move()", which makes the squares move and bounce against the sides of the screen so that they stay in the view. (You may need some extra attributes like "xSpeed" and "ySpeed" for this to work.
You can ask for the width of the whole level by simply saying "width" without quotes and "height" for the height of the level.
We have to check for a square if their x and y position are still inside the level and if not reverse their speed values.
If all works well, you have now created a screensaver!

#When you are done, zip your processing project in  a .zip and send it to your practicum tutor