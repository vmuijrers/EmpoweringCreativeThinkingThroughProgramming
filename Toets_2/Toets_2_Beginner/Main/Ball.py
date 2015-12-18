class Ball(object):
    def __init__(self,x,y,radius,xSpeed,ySpeed):
        self.x =x
        self.y =y
        self.radius = radius
        self.ySpeed =ySpeed
        self.xSpeed =xSpeed
    
    def move(self):
        if self.x > width- self.radius or self.x < self.radius:
            self.xSpeed *= -1
        if self.y > height- self.radius or self.y < self.radius:
            self.ySpeed *= -1
        self.x += self.xSpeed
        self.y += self.ySpeed


    def display(self):
        ellipse(self.x,self.y,self.radius*2,self.radius*2)
