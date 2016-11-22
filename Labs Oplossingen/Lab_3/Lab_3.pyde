
def setup():
    size(800, 600)
    rectMode(CENTER)
    global i_xPos,i_yPos, i_moveSpeed , i_normalRectSize, bool_spacePressed, i_counter, i_rectSize
    i_xPos = 100
    i_yPos = 100
    i_moveSpeed = 3
    i_normalRectSize = 100
    i_counter = 0
    i_rectSize = 100
    bool_spacePressed = False
def draw():
    global i_xPos,i_yPos, i_moveSpeed, i_normalRectSize, bool_spacePressed, i_counter, i_rectSize
    background(51)
    
    #Exercise 3_2
    if bool_spacePressed:
        i_counter+= 1
        if i_counter >= 60:
            bool_spacePressed = False
        i_rectSize = min(i_normalRectSize*2,i_rectSize +2)
    else:
        i_rectSize = max(i_normalRectSize,i_rectSize -2)
    
    #Exercise 3_1
    if i_xPos <= width/2:
        if i_yPos <= height/2:
            #Left Top
            if bool_spacePressed:
                fill(255,0,255) #magenta
            else: 
                fill(0,0,255) #blue
        else:
            #Left Bottom
            if bool_spacePressed:
                fill(255,0,0) #red
            else:
                fill(255,100,0) #orange
    else:
        if i_yPos <= height/2:
            #Right Top
            if bool_spacePressed:
                fill(255,255,255) #white
            else:
                fill(255,255,0) #yellow
        else:
            #Right Bottom
            if bool_spacePressed:
                fill(0,255,255) #cyan
            else:
                fill(0,255,0) #green
    
    rect(i_xPos,i_yPos, i_rectSize * 2, i_rectSize)
    
    
def keyPressed():
    #Exercies 3_0
    global i_xPos,i_yPos, i_moveSpeed, bool_spacePressed, i_counter
    if key == 'a':
        i_xPos -= i_moveSpeed
    if key == 'd':
        i_xPos += i_moveSpeed
    if key == 'w':
        i_yPos -= i_moveSpeed
    if key == 's':
        i_yPos += i_moveSpeed
    if key == ' ':
        bool_spacePressed = True
        i_counter = 0