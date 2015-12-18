from BallTab import Ball
from PaddleTab import Paddle
from Score import Score


def setup():
    rectMode(CENTER)
    ellipseMode(CENTER)
    textSize(40)
    size(800,600)
    global paddleList, ballList, keysPressed, score
    paddleList = []
    ballList = []
    numBalls = 2
    for i in range(0,numBalls):
        if i == 0:
            xSpeed = 4
        else:
            xSpeed = -4
        b = Ball(width/2,100+i*100,40,xSpeed,2,xSpeed)
        ballList.append(b)
    p1 = Paddle(50,height/2,50,100,3)
    p2 = Paddle(width-50,height/2,50,100,3)
    paddleList.append(p1)
    paddleList.append(p2)
    score = Score(0,0)
    keysPressed = {'a':False,'w':False,'s':False,'d':False,LEFT:False,UP:False,DOWN:False,RIGHT:False }

def draw():
    global paddleList, ballList, keysPressed, score
    background(0)
    #move ball
    for i in range(0,len(ballList)):
        bal = ballList[i]
        for j in paddleList:
            bal.checkCollision(j)
        for k in range(i,len(ballList)):
            bal.checkCollisionBall(ballList[k])
        
        if(bal.move()):
            if bal.x > width-bal.radius:
                score.addScore(1)
            if bal.x <bal.radius:
                score.addScore(2)
        bal.display()
    
    #paddles
    yDir =0
    if keysPressed['w']:
        yDir = -1
    if keysPressed['s']:    
        yDir = 1
    paddleList[0].move(yDir)
    
    yDir =0
    if keysPressed[UP]:
        yDir = -1
    if keysPressed[DOWN]:
        yDir = 1
    paddleList[1].move(yDir)
    
    for i in paddleList:
        i.display()    
     
    #score
    if score.score1 >= 5000 or score.score2 >= 5000:
        reset()      
    score.display()
    
def reset():
    global ballList,score
    for i in range(0,len(ballList)):
        ballList[i].x = width/2
        ballList[i].y = height/2 + i * 50   
    score.reset()
    
def keyPressed():
    global keysPressed
    if keyPressed:
        keysPressed[key] = True
        keysPressed[keyCode] = True
        
def keyReleased():
    global keysPressed
    if keyPressed:
        keysPressed[key] = False
        keysPressed[keyCode] = False
