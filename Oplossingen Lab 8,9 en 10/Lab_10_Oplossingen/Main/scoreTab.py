
class Score(object):
    
    def __init__(self,player1,player2):
        self.p1Score = player1
        self.targetScore1 = self.p1Score
        self.p2Score = player2 
        self.targetScore2 = self.p2Score
        self.t1= 0
        self.t2 =0
        self.start1 =0
        self.start2 =0
    
    def AddScore(self,score,player):
        if player == 1:
            self.start1 = self.p1Score
            self.targetScore1 += score
            self.t1 = 0
        if player == 2:
            self.start2 = self.p2Score
            self.targetScore2 += score
            self.t2 =0
        
    def display(self):
        if self.t1<1:
            self.t1+=0.01
        if self.t2 <1:
            self.t2+=0.01
        
        self.p1Score = lerp(self.start1,self.targetScore1,self.t1)
        self.p2Score = lerp(self.start2,self.targetScore2,self.t2)
        
        textSize(40)
        text("Score Player 1: " +str(self.p1Score), 100,40)
        text("Score Player 2: " +str(self.p2Score), 100,80)
    
    def checkReset(self):
        return self.p1Score >= 5000 or self.p2Score >= 5000
            
    def Reset(self):
        self.targetScore1 = 0
        self.targetScore2 = 0

