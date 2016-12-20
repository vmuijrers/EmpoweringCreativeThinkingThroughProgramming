class Score:
    def __init__(self, x,y, score1,score2):
        self.x = x
        self.y = y
        self.score1 = score1
        self.score2 = score2

    def draw(self):
        text("Score Player 1: " + str(self.score1), self.x,self.y)
        text("Score Player 2: " + str(self.score2),self.x, self.y + 50)
    
    def resetScores(self):
        self.score1 = 0
        self.score2 = 0
        
    def addScoreForPlayer1(self, score):
        self.score1 += score
        
    def addScoreForPlayer2(self, score):
        self.score2 += score
        
    def getWinner(self):
        if self.score1 > self.score2:
            return "Player 1"
        elif self.score1 < self.score2:
            return "Player 2"
        else:
            return "Nobody"
        