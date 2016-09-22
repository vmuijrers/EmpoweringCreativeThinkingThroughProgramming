
def setup():
    size(800,600)
    global i_xPos, i_yPos, i_counter, i_width, i_height, i_border 
    i_xPos = 100
    i_yPos = 100
    i_counter = 0
    i_border = 250
    i_width = 100
    i_height = 50
def draw():
    #background(51)
    global i_xPos, i_yPos, i_counter, i_border, i_width, i_height
    if i_counter < 200:
        fill(color(random(256),random(256),random(256)))
        i_xPos = random(i_border,width-i_border- i_width)
        i_yPos = random(i_border,height-i_border - i_height)
        rect(i_xPos,i_yPos, i_width ,i_height)
        i_counter += 1