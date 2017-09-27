
def setup():
    global int_rectWidth, int_rectHeight
    
    size (800,600)
    
    int_rectWidth = 100
    int_rectHeight = 50
    
def draw():
    global int_rectWidth, int_rectHeight
    background(51)
    int_amount = width / int_rectWidth
    int_amountY = height/ int_rectHeight
    #[0,1,2,3,4,5,6,7]
    #for x in range(0,int_amount):
    #    for y in range(0,int_amountY):
    #        rect(x * int_rectWidth,y * int_rectHeight,int_rectWidth,int_rectHeight)
    x =0
    while x < int_amount:
        y =0
        while y < int_amountY:
            #fill(random(0,255),random(0,255),random(0,255))
            rect(x * int_rectWidth +inc,y * int_rectHeight,int_rectWidth,int_rectHeight)
            y= y + 1
        x = x +1
    