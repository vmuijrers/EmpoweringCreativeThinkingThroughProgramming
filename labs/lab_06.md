## Lab 6: 
 
##### Naming conventions 

Put all of your homework files together into one folder, zip it and email it to your lab assistant with your name_the week.zip 

** Make the subject of the email "INLEVEREN: lab 6" **

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


#6_1: Reversed Range
Write a function named "def reversedRange(list,start,end)" which takes a list, a start and an end index (excluding) and returns a list which gives the part of the inputlist in that range, but reversed.
hint: use the splice operator [start : end : step] to get a part of a list, so list[0:3:1] gives us the first three elements of a list

print reversedRange([1,5,6,7,10,8],2,4) >>> output: [7,6]
print reversedRange([1,5,6,7],0,3) >>> output: [6,5,1]

#6_2: Colored Lists
Given a list of colors (note: a color is a tuple with three values: red, green and blue ranging from 0 to 255), write a function 'RedList(list)' which returns an integer which tells us how many instances of red occur in the list (a red instance is a tuple where the red value (first element) is 255, the other two values can be anything).


print RedList([ (255,0,0), (200,100,100) , (255,100,35) , (233,0,0)] ) >>> output: 2
print RedList([ (105,0,0), (200,100,100) , (255,100,0)  , (233,0,0)] ) >>> output: 1
print RedList([ (255,0,0), (200,100,30)  , (255,100,25) , (255,0,10)]) >>> output: 3

hint: om een element van een list op te vragen kun je list[i] gebruiken waarbij i, verwijst naar de index (het eerste element van een list heeft index 0). Om een waarde van een tuple in een list op te vragen kun je list[i][j] gebruiken waarbij i verwijst naar het i'de element in de list en j naar het j'de element in de tuple.

#6_3: Smelly Dwarfs and rich Orcs
Download the file Dwarfs.txt and put in your projectfolder next to your .py files.
Then use the command "textFile = open('Dwarfs.txt','r')", to save the content of the file to the variable named 'textFile'
Next use the command "textFile.read()" and save the result in a variabel called "textWords", this is a string containing all the words of the text.
You can now print your textWords variable to see the story.
The story is written on a scroll in the empire of the Dwarfs, a jealous orc thinks he is smart and wants to replace all occurrences of the word 'dwarf' with the word 'orc', can you help him?
Write a function "def ReplaceDwarf(text, newRaceName):", which takes two string-parameters, write the code to replace all occurrences of the word 'dwarf' with the given 'newRaceName' word. 

Return the resulting string and print your new story outside the function with the call 'print ReplaceDwarf(textWords, 'Orc')'

hint: you can use the function text.replace(oldWord,newWord) to replace an occurrence of a word with another word
