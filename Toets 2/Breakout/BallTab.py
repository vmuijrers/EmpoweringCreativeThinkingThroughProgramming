class Ball:
    def __init__(self, x,y,radius,xSpeed,ySpeed, col):
        self.x = x
        self.y = y
        self.radius = radius
        self.xs = xSpeed
        self.ys = ySpeed
        self.lastPaddleHit = 0
        self.col = col
 
            
    def update(self):
        #TODO: Update the x and y position of the ball by adding their xSpeed and ySpeed to it
        self.x += self.xs
        self.y += self.ys 
        #TODO: Make sure the ball cannot leave the screen by reversing it's speed if it hits the side of the screen
        if(self.x + self.radius > width or self.x - self.radius < 0):
          self.xs *= -1  
        if(self.y + self.radius > height or self.y - self.radius <0 ):
          self.ys *= -1       
            
    def draw(self):
        fill(self.col)
        ellipse(self.x,self.y,self.radius*2,self.radius*2)
        fill(255)
    
    def checkCollisionWithBlock(self, block):
        difX = abs(block.x - self.x)
        difY = abs(block.y - self.y)
        
        if(difX > block.w/2 + self.radius or difY > block.h/2+self.radius):
            return False
        
        res = (difX <= block.w/2 or difY <= block.h/2 or sq(difX - block.w/2) + sq(difY - block.h/2) < sq(self.radius))   
        
        
        if(res):   
           if(self.x >= block.x + block.w/2 +self.xs or self.x <= block.x - block.w/2 -self.xs):
                self.xs *= -1
                self.x += self.xs  
           if(self.y >= block.y + block.h/2 +self.ys or self.y <= block.y - block.h/2 -self.ys):
                self.ys *= -1
                self.y += self.ys
           return True
        return False  
      
    def pointInCircle(self,x,y):
        return dist(self.x,self.y,x,y) < self.radius