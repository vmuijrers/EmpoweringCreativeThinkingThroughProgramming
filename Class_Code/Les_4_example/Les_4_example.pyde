

def setup():
    size(800,600)
    global i_xPos, i_yPos, i_width, i_startValue, i_endValue, f_t
    i_xPos = 100
    i_yPos = 100
    i_width = 100
    i_startValue =0
    i_endValue = width/2
    f_t=0

def draw():
    background(51)
    global i_xPos, i_yPos, i_width, i_startValue, i_endValue, f_t
    f_t += 0.01
    i_xPos =  lerp(i_startValue,i_endValue,f_t)
    #i_xPos = random(0, width-i_width)
    #i_yPos = random(0, height)
    rect(i_xPos,i_yPos,i_width,50)