
from scoreTab import Score
def setup():
    global score
    size ( 800,600)
    score = Score(0,0)
    

def draw():
    global score
    background(0)

    score.display()
    if(score.checkReset()):
        score.Reset()

def keyPressed():
    if key == 'a':
        score.AddScore(1000,1)
    if key == 'l':
        score.AddScore(1000,2)
