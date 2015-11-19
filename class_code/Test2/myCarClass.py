class Car(object):
    
    def __init__(self,  kleur, x, y,w,h, xSpeed, ySpeed ):
        self.col = kleur
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.w = w
        self.h = h
        
    def display(self):
        stroke(0,0,0,0)
        fill(self.col)
        rect(self.x,self.y, self.w,self.h)
    
    def move(self):
        if self.x > width -self.w or self.x < 0:
            self.xSpeed = -self.xSpeed
        if self.y > height -self.h or self.y < 0:
            self.ySpeed = -self.ySpeed
        self.x += self.xSpeed
        self.y += self.ySpeed
    
    def accelerate(self):
        self.xSpeed += random(-0.1,0.1)
        self.ySpeed += random(-0.1,0.1)
