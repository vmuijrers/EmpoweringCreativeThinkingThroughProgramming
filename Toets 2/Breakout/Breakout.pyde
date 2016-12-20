from PaddleTab import Paddle 
from BallTab import Ball
from BlockTab import Block
from ScoreTab import Score

def setup():
    size(800,600)
    background(10)
    rectMode(CENTER)
    global ballList, paddleList, blockList, score, allKeys
    allKeys = {'a':False, 'd':False, 'j':False, 'l': False } 
    ResetGame()
    textSize(32)
    
def draw():
    global blockList, score, paddleList
    background(10)
    
    if(len(blockList) == 0):
        #Game Over!
        winner = score.getWinner()
        text(winner + " wins!\nScore Player 1: "+str(score.score1)+"\nScore Player 2: "+str(score.score2)+"\nPress Enter to Restart!",width/2-50,height/2, 400, 300)
        return  
        
    
    #Check Collision with paddle
    
    for j in range(0,len(ballList)):
        bal = ballList[j]
        #Update the Ball's position by calling the update() function of the ball and draw it on screen
        bal.update()
        bal.draw()
        
        #Check for collision between ball en paddle
        for k in range(0,len(paddleList)):
            paddle = paddleList[k]
            # if there is collision add a score
            if(bal.checkCollisionWithBlock(paddle)):
                bal.lastPaddleHit = k
                bal.col = paddleList[k].col
                if k == 0:
                    score.addScoreForPlayer1(10)
                elif k==1:
                    score.addScoreForPlayer2(10) 
        
        #Draw the blocks which are left in the list
        for i in range(0,len(blockList)):
            if(bal.checkCollisionWithBlock(blockList[i])):
                blockList[i].hasCollided = True
                
                if bal.lastPaddleHit == 0:
                    score.addScoreForPlayer1(10)
                else:
                    score.addScoreForPlayer2(10)
      
    #Remove all blocks which are in Collision
    blockList = [block for block in blockList if not block.hasCollided]
    
    #Draw all blocks
    for i in range(0,len(blockList)):   
        blockList[i].draw()
     
    #Handle the keypresses and update paddles accordingly
    if allKeys['a']:
        paddleList[0].update(-1)
    if allKeys['d']:
        paddleList[0].update(1)
    if allKeys['j']:
        paddleList[1].update(-1)
    if allKeys['l']:
        paddleList[1].update(1)
    
    #Draw the paddles on screen by calling their draw() functions
    for i in range(0,len(paddleList)):
        paddleList[i].draw()  
    
    #Show the score
    score.draw()
    


def keyPressed():
    global allKeys
    #If a key is pressed and it is in our dictionary, set it to False
    if key in allKeys:
        allKeys[key] = True

#TODO: Define the keyReleased() function and implement it in such a way that when the ENTER key is pressed, the ResetGame() function is called
def keyReleased():
   
   #If a key is released and it is in our dictionary, set it to False
   global allKeys
   if key in allKeys:
        allKeys[key] = False
    
   if(key == ENTER):
        ResetGame()
        
def ResetGame():
    global ballList, paddleList, blockList, score

    score = Score(10,40,0,0)
    score.resetScores()
    
    blockList = []
    numBlocks = 21
    for i in range(0,numBlocks):
        block_w = 100
        block_h = 50
        block_x = 100 + (i % 7) * block_w + 10 
        block_y = 100 + (i / 7) * block_h + 20 
        blockList.append(Block(block_x,block_y,block_w,block_h))
    
    paddleList = []
    numPlayers = 2
    for i in range(0,numPlayers):
        pad_w = 100
        pad_h = 50
        pad_x = width/2 - 100 + i * 150
        pad_y = height - pad_h/2
        pad_speed = 10
        paddle = Paddle(pad_x,pad_y,pad_w,pad_h,pad_speed, color(random(0,255),random(0,255),random(0,255)))
        paddleList.append(paddle)
    
    ballList = []
    numBalls = 3
    for i in range(0,numBalls):
        bal_x = width/2 -100 + i * 50
        bal_y = height -100
        bal_radius = 25
        bal_Xspeed = 5
        bal_Yspeed = 5
        bal = Ball(bal_x,bal_y,bal_radius,bal_Xspeed,bal_Yspeed, color(255))
        ballList.append(bal)
    
    


 