#TODO: Implement the Block Class with the init and draw function. A block has the following parameters: x, y, w, h and hasCollided with inital value at False.
class Block:
    def __init__(self, x,y, pad_w,pad_h):
        self.x = x
        self.y = y
        self.w = pad_w
        self.h = pad_h
        self.hasCollided = False

    def draw(self):
        rect(self.x,self.y,self.w,self.h)
        
        
