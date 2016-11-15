class Rectangle(object):
    
    def __init__(self, xPos, yPos, w, h, col):
        self.x = xPos
        self.y = yPos
        self.w = w
        self.h = h
        self.col = col
    
    def move(self, xSpeed):
        self.x += xSpeed
    
    def changeSize(self, dw, dh):
        self.w += dw
        self.h += dh
    
    def display(self):
        fill(self.col)
        rect(self.x, self.y, self.w, self.h) 