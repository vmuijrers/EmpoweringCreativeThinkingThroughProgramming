
 
class Cube(object):
    
    def __init__(self,x,y,w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        
    def draw(self):
        self.x += self.speed
        rect(self.x,self.y,self.w,self.h)
        if self.x + self.w> width or self.x <0:
            fill(random(255),random(255),random(255),255)
            self.speed *= -1

def setup():
    global c,c1
    size(800,600)
    background(10)
    fill(random(255),random(255),random(255),255)
    c = Cube(random(0,width),random(0,height), random(50,100), random(50,100), 10)
    c1 = Cube(random(0,width),random(0,height), random(50,100), random(50,100), 10)

def draw():
    background(10)
    c.draw()
    c1.draw()




 
    
