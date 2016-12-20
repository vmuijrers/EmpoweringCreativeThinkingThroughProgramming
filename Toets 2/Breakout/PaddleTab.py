class Paddle:
    #TODO: Implement the __init__ function for the paddle with variables: x, y, w (width), h(height) and moveSpeed
    def __init__(self, x,y, pad_w,pad_h,moveSpeed, col):
        self.x = x
        self.y = y
        self.w = pad_w
        self.h = pad_h
        self.moveSpeed = moveSpeed
        self.col = col
    
    def update(self,difX):
        #TODO: make sure the paddle moves to the left over the x-axis with its moveSpeed if the difX value is -1 and to the right over the x-axis with its moveSpeed if the difX value is 1, otherwise do nothing
        self.x += difX * self.moveSpeed
        #TODO: Make sure the paddle can not go out of the screen by limiting it's self.x position
        if(self.x + self.w/2 > width):
            self.x = width - self.w/2
        if(self.x - self.w/2 < 0):
            self.x = self.w/2
    def draw(self):
        fill(self.col)
        rect(self.x,self.y,self.w,self.h)
        fill(255)
        