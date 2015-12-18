class Ball(object):
    
    def __init__(self,x,y,radius,xSpeed,ySpeed,speed):
        self.x =x
        self.y =y
        self.radius =radius
        self.speed =0
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.dir =45
        self.speed = speed
    
    def move(self):
#         self.xSpeed = cos(radians(self.dir)) * self.speed
#         self.ySpeed = sin(radians(self.dir)) * self.speed
        self.x += self.xSpeed
        self.y += self.ySpeed
        if(self.y < self.radius or self.y> height -self.radius):
#             self.dir =  360 - self.dir 
              self.ySpeed *=-1
        if (self.x +self.radius > width or self.x < self.radius):
#             self.dir =  360 - self.dir
            self.xSpeed *= -1 
            return True
        return False
        
    def checkCollisionBall(self,ball):
        if (self != ball):
            if dist(self.x,self.y,ball.x,ball.y) < self.radius +ball.radius:
                txSpeed = self.xSpeed
                tySpeed = self.ySpeed
                self.xSpeed = ball.xSpeed
                self.ySpeed = -ball.ySpeed
                ball.xSpeed = txSpeed
                ball.ySpeed = -tySpeed
        
    def checkCollision(self, paddle):
        
        #Check eerst of er collision is, daarna van welke kant
        
        dx = abs(self.x-paddle.x)
        dy = abs(self.y-paddle.y)
        if dx <= self.radius + paddle.w/2 and dy <= self.radius + paddle.h/2:
            
            #Check collision voor een hoek
            ddir = degrees(atan2(paddle.y-self.y,paddle.x-self.x))
            ddir += 180
            if(ddir >=40 and ddir<=50 or ddir >=130 and ddir <=140 or ddir >=220 and ddir <=230 or ddir >=310 and ddir <=320):
#                 self.dir += 180
                self.xSpeed *=-1
                self.ySpeed *=-1
            else:
                #Collision van links of rechts
                if self.x <= paddle.x-paddle.w/2 or self.x >= paddle.x+paddle.w/2 :
                    self.xSpeed *=-1
#                     self.dir = (360 -self.dir)  + 180
                else:
                    #Collision van onder of boven
#                     self.dir = (360 -self.dir)
                    self.ySpeed *=-1

        
    def display(self):
        ellipse(self.x,self.y,self.radius*2,self.radius*2)
        
