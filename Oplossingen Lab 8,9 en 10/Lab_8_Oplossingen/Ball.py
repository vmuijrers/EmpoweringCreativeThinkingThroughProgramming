class Ball(object):
    def __init__(self, x,y,radius,xSpeed,ySpeed,rotSpeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.xSpeed =xSpeed
        self.ySpeed =ySpeed
        self.rotSpeed = rotSpeed
        self.angle = 0
        
    def update(self, ballList):
        pushMatrix()
        self.rotateMe()
        self.checkCollision(ballList)
        self.move()
        self.display()
        popMatrix()
        
    def rotateMe(self):
        #rotation, we use a matrix here, which can be manipulated using the translate and rotate function
        translate(self.x,self.y)
        self.angle += self.rotSpeed
        rotate(radians(self.angle))

    def move(self):
        #movement and keep object in screen
        if self.x < self.radius or self.x + self.radius > width:
            self.xSpeed *= -1
        if self.y < self.radius or self.y + self.radius > height:
            self.ySpeed *= -1
        self.x += self.xSpeed
        self.y += self.ySpeed
    
    def checkCollision(self,ballList):
        for i in range(0,len(ballList)):
            b = ballList[i]
            #make sure you don't collide with yourself
            if b != self:
                #check for collision based on radius (a circle collision is fine here, a box collision is also allowed)
                #box collision would be: abs(self.x - b.x) < self.w*0.5 + b.w*0.5 and abs(self.y - b.y) < self.h *0.5 + b.h*0.5
                #where w is the width of the box and h is the height of the box
                if dist(self.x,self.y,b.x,b.y) < b.radius + self.radius:
                    #determine direction away from other ball in radians
                    dir = atan2(self.y-b.y,self.x-b.x)
                    #determine speed from xSpeed and ySpeed using Pythagoras
                    speed = sqrt(self.xSpeed*self.xSpeed + self.ySpeed * self.ySpeed)
                    #calculate new speed
                    self.xSpeed = cos(dir) * speed
                    self.ySpeed = sin(dir) * speed
                    
                    #also calculate the other direction
                    otherSpeed = sqrt(b.xSpeed*b.xSpeed +b.ySpeed * b.ySpeed)
                    b.xSpeed = cos(dir - PI)*otherSpeed
                    b.ySpeed = sin(dir - PI)*otherSpeed
                    
    def display(self):
        #draw a small ball to show rotation
        ellipse(100,100,self.radius*0.25,self.radius*0.25)
        ellipse(0,0,self.radius*2,self.radius*2)
        #rect(0,0,self.radius*2,self.radius*2)
