class Paddle(object):
    
    def __init__(self,x,y,w,h,ySpeed):
        self.x =x
        self.y =y
        self.w =w
        self.h =h
        self.ySpeed =ySpeed
    
    def move(self, yDir):
        
        if((self.y > self.h/2 and yDir == -1) or (self.y< height -self.h/2 and yDir == 1)):
            self.y += yDir * self.ySpeed

    def display(self):
        rect(self.x,self.y,self.w,self.h)
        
