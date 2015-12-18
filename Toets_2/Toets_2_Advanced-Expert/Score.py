class Score(object):
    
    def __init__(self,score1,score2):
        self.score1 = score1
        self.score2 = score2
    
    def addScore(self,player):
        if player == 1:
            self.score1 += 1000
        else:
            self.score2 += 1000
   
    def reset(self):
        self.score1= 0
        self.score2 = 0
        
    def display(self):
        text(self.score1,width/4,40)
        text(self.score2,3* width/4,40)
