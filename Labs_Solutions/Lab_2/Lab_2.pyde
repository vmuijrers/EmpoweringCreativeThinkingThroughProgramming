#Lab 2 - Valentijn Muijrers

def setup():
    rectMode(CENTER)
    size(800,600)
    
    # All global variables, the '\' denotes a new line so that we can put our code on multiple lines for clarity 
    global int_xRectPos, int_yRectPos, \
           int_xElPos, int_yElPos, \
           int_widthRect, int_heightRect, \
           difPosX, difPosY
    
    #The width and height of the rectangle
    int_widthRect  = 100
    int_heightRect = 100
    
    #The displacement of the rectangle
    ratio = float(width - int_widthRect) / (height - int_heightRect)
    difPosX = 5 * ratio
    difPosY = 5 
    
    #The initial position of the rectangle
    int_xRectPos = 50
    int_yRectPos = 50
    
    #The position of the ellipse
    int_xElPos = 100
    int_yElPos = 100

def draw():
    global int_xRectPos, int_yRectPos, \
           int_xElPos, int_yElPos, \
           int_widthRect, int_heightRect, \
           difPosX, difPosY

    #Give the background a color    
    background(51)
    
    #Exercise 2_1
    #The Moving Orange Circle
    #Add one to the x-position of the Circle
    int_xElPos = int_xElPos + 1
    
    #Exercise 2_0
    #Fill the color with orange
    fill(255,155,0)
    #Draw the circle
    ellipse(int_xElPos,int_yElPos,100,100)
    
    #Exercise 2_2
    #The Bouncing Blue Rectangle
    halfWidth  = int_widthRect  * 0.5
    halfHeight = int_heightRect * 0.5
    #Create an if-statement which checks if the rectangle reaches the bounds of the screen
    if int_xRectPos > width  - halfWidth  or int_xRectPos < halfWidth or \
       int_yRectPos > height - halfHeight or int_yRectPos < halfHeight:
           #reverse the direction of movement
           difPosX *= -1 #this is the same as difPosX = difPosX * -1
           difPosY *= -1 #this is the same as difPosY = difPosY * -1
    
    #Update the position        
    int_xRectPos = int_xRectPos + difPosX
    int_yRectPos = int_yRectPos + difPosY
    
    #Fill the color with light blue
    fill(0,155,255)
    rect(int_xRectPos,int_yRectPos,int_widthRect,int_heightRect)