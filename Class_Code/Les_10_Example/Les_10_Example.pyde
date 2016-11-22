
scramble("Kip", "kaars")

def scramble(word1, word2):
    lengthWord = max(len(word1), len(word2)) 
    result = ""
    for i in range(0,lengthWord):
        
        if (len(word1) < i):
            result+= word1[i]
        else:
            if(i != lengthWord -1):
                result+='0'
        if (len(word2) < i):
            result+= word2[i]
        else:
            if(i != lengthWord -1):
                result+='0'
    
    if(result[len(result)-1] == '0'):
        result = result[0 : len(result)-1]       
            
    return result





'''
myList = [ "hoi", "doei" ]

myList2 = []
myList2.append("hoi")
myList2.append("doei")

for kip in [0, 1] :
    for inceptionKip in range(0,len(myList[kip])):
        if(myList[kip][inceptionKip]  == 'o':
               myList[kip][inceptionKip] = 'a'
        print myList[kip][inceptionKip] 


kip =0
while (kip < len(myList)):
    print myList[kip]
    kip +=1
    



for (int kip = 0 ; kip < myList.Length()  ; kip+=1 )
{
print myList[kip]
}
'''