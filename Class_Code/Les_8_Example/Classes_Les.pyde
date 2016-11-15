from RectangleTab import Rectangle

def setup():
    size(800,600)
    global myRectangle, myRectangle1, myRectangleList
    myRectangleList = []
    
    for i in range(0,300):
        xPos = random(0,width)
        yPos = random(0,height)
        w = random(50,100)
        h = random(50,100)
        col = color(random(255),random(255),random(255))
        myRectangleList.append(Rectangle(xPos,yPos,w,h, col))
    

def draw():
    
    global myRectangle, myRectangle1,myRectangleList
    background(0)
    for i in range(0,len(myRectangleList)):
        myRectangleList[i].changeSize(random(-10,10),random(-10,10))
        myRectangleList[i].display()