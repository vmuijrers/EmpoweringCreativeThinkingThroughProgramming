class Hover(object):
    def __init__(self,x,y,xSpeed,ySpeed,radius, maxSpeed,accel):
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed       
        self.radius = radius
        self.maxSpeed= maxSpeed
        self.accel = accel
        self.selected = False;
        self.targetX = self.x
        self.targetY = self.y
        
    def moveLeft(self):
        if self.x > self.radius:
            self.xSpeed = max(self.xSpeed - self.accel, -self.maxSpeed)
    def moveRight(self):
        if self.x < width- self.radius:
            self.xSpeed = min(self.xSpeed + self.accel, self.maxSpeed)    
    def moveUp(self):
        if self.y > self.radius:
            self.ySpeed = max(self.ySpeed - self.accel, -self.maxSpeed)
    def moveDown(self):
        if self.y < height- self.radius:
            self.ySpeed = min(self.ySpeed + self.accel, self.maxSpeed)
    
    def updateSpeed(self):
        #create friction
        if not keyPressed:
            self.xSpeed *= 0.99
            self.ySpeed *= 0.99
        
        
        self.x += self.xSpeed
        if self.x < self.radius or self.x > width- self.radius:
            self.xSpeed *=-1
            
        
        self.y += self.ySpeed
        if self.y< self.radius or self.y > height-self.radius:
            self.ySpeed *= -1
        
        
    def checkSelected(self):
        self.selected = False
        if dist(self.x,self.y,mouseX,mouseY) < self.radius:
            self.selected = True
        
    def moveSelected(self):
        if self.selected:
            self.x = lerp(self.x,self.targetX,0.02)
            self.y = lerp(self.y,self.targetY,0.02)
    
    def setTargetPos(self,targetX,targetY):
        self.targetX = targetX
        self.targetY = targetY
    
    def display(self):
        noStroke()
        fill(255)
        ellipse(self.x,self.y,self.radius*2,self.radius*2)
        if self.selected:
            noFill()
            stroke(0,255,0)
            ellipse(self.x,self.y,self.radius*2 +50,self.radius*2 + 50)
    
    def sign(self,num):
        if num > 0 :
            return 1
        if num < 0:
            return -1
        return 0
