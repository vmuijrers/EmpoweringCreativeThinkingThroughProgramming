class Ball(object):
    
    def __init__(self,x,y,w,h,xSpeed,ySpeed, grav):
        self.x = x
        self.y = y 
        self.w = w
        self.h = h
        self.grav = grav
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
    def update(self):
        self.x += self.xSpeed
        self.xSpeed  *= 0.996
        
        if self.x + self.w /2> width or self.x -self.w/2<0 :
            self.xSpeed= -self.xSpeed
        
        self.y += self.ySpeed
        self.ySpeed += self.grav
        
        
        if self.y + self.h/2 > height:
            self.ySpeed =- self.ySpeed
            self.ySpeed *= 0.92
            
    def sign(self,num):
        if num > 0:
            return 1
        if num < 0:
            return -1
        return 0    
        
    def display(self):
        ellipse(self.x,self.y,self.w,self.h)
