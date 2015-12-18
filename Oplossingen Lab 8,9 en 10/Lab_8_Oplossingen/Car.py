class Car(object):
    def __init__(self, x,y,w,h,xSpeed,ySpeed,rotSpeed):
        self.x = x
        self.y = y
        self.w = w
        self.h =h
        self.xSpeed =xSpeed
        self.ySpeed =ySpeed
        self.rotSpeed = rotSpeed
        self.angle = 0
        
    def update(self):
        pushMatrix()
        self.move()
        self.display()
        popMatrix()
        

    def move(self, xDir,yDir):
        #movement and keep object in screen
        self.x += self.xSpeed * xDir
        self.y += self.ySpeed * yDir
    
        if self.x < self.w:
            self.x = self.w
        if self.x + self.w > width:
            self.x = width -self.w
        if self.y < self.h:
            self.y = self.h
        if self.y + self.h > height:
            self.y = height -self.h
        

    def display(self):
        #draw a small ball to show rotation
        rect(self.x,self.y,self.w,self.h)
    
