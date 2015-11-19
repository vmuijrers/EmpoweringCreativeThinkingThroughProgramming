from Ball import Ball

def setup():
    size(800,600)
    rectMode(CENTER)
    ellipseMode(CENTER)
    global b1, gravity, ballList, startX,startY
    startX =0
    startY = 0
    gravity = 0.3
    ballList = []
    b1 = Ball(100,100,100,100,20, 0, gravity)
    ballList.append(b1)
    
def draw():
    global startX, startY, isPressed
    background(100)
    
    for i in range(0,len(ballList)):
        ballList[i].update()
        ballList[i].display()

    if mousePressed:
        line(startX,startY,mouseX,mouseY)
    
def mousePressed():
    global startX,startY
    startX = mouseX
    startY = mouseY
    
def mouseReleased():
    global startX,startY
    b1 = Ball(startX,startY,100,100,sign(mouseX - startX) * 15, sign(mouseY - startY)*5, gravity)
    ballList.append(b1)

def sign(num):
    if num > 0 :
        return 1
    if num < 0:
        return  -1
    return 0
