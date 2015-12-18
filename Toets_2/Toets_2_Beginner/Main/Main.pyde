from Ball import Ball
from PaddleTab import Paddle
from Score import Score

def setup():
    size (800,600)
    textSize(50)
    rectMode(CENTER)
    ellipseMode(CENTER)
    global ball,paddle,score
    x = 100
    y = 100
    radius = 50
    xSpeed = 3
    ySpeed = 3
    ball = Ball(x,y,radius,xSpeed,ySpeed)
    paddle = Paddle(width-radius,height/2,50,100,3)
    score = Score(0)

def draw():
    global ball, paddle, score
    background (0)
    ball.move()
    if ball.x > width-ball.radius:
        score.addScore()
    ball.display()
    if keyPressed:
        if key == 'w':
            paddle.move(-1)
        if key == 's':
            paddle.move(1)
    paddle.display()
    score.display()
    
