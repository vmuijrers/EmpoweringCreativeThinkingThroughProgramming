from Ball import Ball
from Car import Car
def setup():
    size(800,600)
    global ballList, numBalls, car
    ellipseMode(CENTER);
    car = Car(100,100,50,100,5,5,5)
    ballList = []
    numBalls = 4
    rectMode(CENTER)
    for i in range(0,numBalls):
        radius = random(50,75)
        xPos = random(radius,width-radius)
        yPos = random(radius,height-radius)
        xSpeed = random(-3,3)
        ySpeed = random(-3,3)
        rotSpeed = random(-5,5)
        b = Ball(xPos,yPos,radius,xSpeed,ySpeed,rotSpeed)
        ballList.append(b)
def draw():
    background(0)
    for i in range(0,numBalls):
        ballList[i].update(ballList)
    
    if keyPressed:
        yMovement = 0
        xMovement = 0
        if keyCode == UP or key == 'w':
            yMovement = -1
        if keyCode == DOWN or key == 's':
            yMovement = 1
        if keyCode == LEFT or key == 'a':
            xMovement = -1
        if keyCode == RIGHT or key == 'd':
            xMovement = 1
        car.move(xMovement,yMovement)
    car.display()
    

    
