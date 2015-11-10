from myCarClass import Car

def setup():
    size(800,600)
    global carList
    carList = []
    for i in range(0,200):
        w = random(50,100)
        h = random(50,100)
        x = random(0,width -w)
        y = random(0,height -h)
        col = color(random(0,255),random(0,255),random(0,255))
        xSpeed = random(-3,3)
        ySpeed = random(-3,3)
        c = Car(col,x,y,w,h, xSpeed, ySpeed )
        carList.append(c)
def draw():
    background(0)
    for i in range(0,200):
        carList[i].accelerate()
        carList[i].move()
        carList[i].display()
