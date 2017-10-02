#Lab_4_Valentijn_Muijrers


def setup():
    textSize(48)
    size(800,600)
    global i_x, i_y, i_w, i_h, f_score_t,f_t, i_score, i_score_start, i_score_end, \
           i_newX, i_oldX, i_oldY, i_newY, \
           i_newWidth, i_oldWidth, i_newHeight, i_oldHeight, d_t
    i_w = random(50,200)
    i_h = random(50,200)
    i_x = random(0,width  -i_w)
    i_y = random(0,height -i_h)
    i_oldX = i_x
    i_oldY = i_y
    i_newX = i_x
    i_newY = i_y
    f_t = 1
    f_score_t = 0
    i_score = 0
    i_score_start = i_score
    i_score_end = i_score
    i_newWidth = i_w
    i_oldWidth = i_w
    i_oldHeight = i_h
    i_newHeight = i_h
    d_t = 1.0/60.0
    
def draw():
    global i_x, i_y, i_w, i_h, f_score_t,f_t, i_score, i_score_start, i_score_end, \
           i_newX, i_oldX, i_oldY, i_newY, \
           i_newWidth, i_oldWidth, i_newHeight, i_oldHeight, d_t
    background(51)
    fill(255,255,255)
    
    #Exercise 4_2
    f_t = min( 1, f_t + d_t)
    f_score_t = min( 1, f_score_t + d_t)
    i_score = lerp(i_score_start, i_score_end, f_t)
    i_x = lerp(i_oldX, i_newX, f_t)
    i_y = lerp(i_oldY, i_newY, f_t)
    i_w = lerp(i_oldWidth, i_newWidth, f_t)
    i_h = lerp(i_oldHeight, i_newHeight, f_t)
    rect(i_x, i_y, i_w, i_h)
    
    #Exercise 4_0
    fill(0,255,0)
    text("Score: "+ str(int(i_score)),10,50)


def mousePressed():
    global i_x, i_y, i_w, i_h, f_score_t,f_t, i_score, i_score_start, i_score_end, \
           i_newX, i_oldX, i_oldY, i_newY, \
           i_newWidth, i_oldWidth, i_newHeight, i_oldHeight, d_t
    
    #Exercise 4_1
    if mouseX >= i_x and mouseX <= i_x + i_w and mouseY >= i_y and mouseY <= i_y + i_h and f_t == 1:
        i_score_end += 20
        i_newX = random(0,width  -i_w)
        i_newY = random(0,height -i_h)
        i_oldX = i_x 
        i_oldY = i_y
        i_oldHeight = i_h
        i_newHeight = random(50,200)
        i_oldWidth = i_w
        i_newWidth = random(50,200)
        f_t = 0 
    else:
        i_score_end += 10
    f_score_t = 0    
    i_score_start = i_score
    