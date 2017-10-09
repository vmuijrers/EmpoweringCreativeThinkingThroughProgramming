#Lab 5 Valentijn Muijrers
def setup():
    global rectSize
    size(800,800)
    rectSize = 100
    #5_0
    for i in range(1,101):
        if i % 3 == 0 and i% 5==0:
            print 'HighFive'
        elif i % 3 == 0:
            print 'High'
        elif i % 5 == 0:
            print 'Five'
        else:
            print i
def draw():
    background(51)
    global rectSize
    num = int(width/float(rectSize))
    num2 = int(height/float(rectSize))
    #5_1
    for i in range (0,num):
        for j in range(0,num2):
            fill(255,255,255)
            if i%2 == j%2:
                fill(0,0,0)
            rect(i*rectSize,j*rectSize,rectSize,rectSize)
            #5_2
            if i >= num/2-1 and i < num/2+1 and j >= num2/2-1 and j < num2/2+1:
                for k in range(0,5):
                   for l in range(0,5): 
                       fill(255,0,0)
                       rect(i* rectSize + k*rectSize/2,j*rectSize + l*rectSize/2,rectSize/2,rectSize/2)