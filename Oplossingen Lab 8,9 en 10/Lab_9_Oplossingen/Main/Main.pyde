from hoverTab import Hover

def setup():
    size(800,600)
    global keysPressed, hoverList
    keysPressed = {'a':False,'w':False,'s':False,'d':False,LEFT:False,UP:False,DOWN:False,RIGHT:False }
    hoverList = []
    h1 = Hover(100,100,0,0,50,5,0.1)
    h2 = Hover(500,300,0,0,50,5,0.1)
    hoverList.append(h1)
    hoverList.append(h2)
def draw():
    background(0)
    if keysPressed['a']:
        hoverList[0].moveLeft()
    if keysPressed['w']:
        hoverList[0].moveUp()
    if keysPressed['s']:    
        hoverList[0].moveDown()
    if keysPressed['d']:
        hoverList[0].moveRight()
    if keysPressed[LEFT]:
        hoverList[1].moveLeft()
    if keysPressed[RIGHT]:
        hoverList[1].moveRight()
    if keysPressed[UP]:
        hoverList[1].moveUp()
    if keysPressed[DOWN]:
        hoverList[1].moveDown() 

    for i in hoverList:
        i.updateSpeed()
        i.moveSelected()
        i.display()


def keyPressed():
    
    keysPressed[key] = True
    keysPressed[keyCode] = True
   
def keyReleased():
    
    keysPressed[key] = False
    keysPressed[keyCode] = False

def mouseClicked():
    if mouseButton == LEFT:
        for i in hoverList:
            i.setTargetPos(mouseX,mouseY)
            i.checkSelected()

def mouseDragged():
    if mouseButton == RIGHT:
        for i in hoverList:
            i.moveSelected()

def mousePressed():
    if mouseButton == RIGHT:
        for i in hoverList:
            i.setTargetPos(mouseX,mouseY)   
