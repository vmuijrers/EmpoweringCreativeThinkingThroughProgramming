#Oplossing Lab 7 - Valentijn Muijrers

#7_0
def round_sum(a,b,c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    rest = num % 10
    if rest >= 5:
        return num - rest + 10
    else:
        return num - rest
   
print round_sum(12,15,22)

#7_1
def scramble(word1, word2):
    longestWord = max(len(word1),len(word2))
    result = ''
    for i in range(longestWord):
        if i < len(word1):
            result+= word1[i]
        elif i != longestWord:
            result+= '0'
        if i < len(word2):
            result+= word2[i]
        elif i != longestWord:
            result+= '0'
    return result

print scramble('kip', 'koeijajaj')

#7_2
def unscramble(word):
    word1 = ''
    word2 = ''
    
    for i in range(len(word)):
        if word[i] != '0':
            if i %2 ==0:
                word1 += word[i]
            else:
                word2 += word[i]
    return (word1, word2)

print unscramble("uengsgcsr0a0m0b0l0e0d0")