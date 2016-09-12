
def setup():
    size(800,600)
    textSize(40)
    global x, y, bool_myBoolean , string_myString
    bool_myBoolean = False
    x = 10
    y = 255
    string_myString = "Hoi"

def draw():
    global x, y, bool_myBoolean, string_myString
    background(51)
    x = x + 1
    y = y - 1
    if ( x > 100 ):
        bool_myBoolean = True
        
    if ( x > 200 ):
        bool_myBoolean = False
        
    if ( bool_myBoolean ):
        fill(0,255,0,y)
        rect(100,100,100,100)
        string_myString = string_myString + " Hoi"
    else:
        fill(255,0,0,y)
        
    ellipse(width/2, height/2, x,x)
    text(string_myString,100,100)
            
            