class Score(object):
    def __init__(self,score):
        self.score = score
    def addScore(self):
        self.score += 1000
    def display(self):
        text(self.score,width/2,40)
