__author__ = 'Valentijn'

def optelsom(begingetal,eindgetal):
    resultaat = eindgetal
    for index in range(begingetal,eindgetal, 1):
        resultaat = resultaat + index

    return resultaat


print optelsom(4,6)

def alarm_klok(dag,vakantie):

    if vakantie:
       if dag < 6:
          return "10:00"
       else:
           return "off"
    else:
       if dag < 6:
          return "7:00"
       else:
           return "10:00"

print alarm_klok(4, True)

def rondom_tien(nummer):
    mod = (nummer +2 )% 10
    return mod <= 4


print rondom_tien(8)
print rondom_tien(12)
print rondom_tien(6)
print rondom_tien(10)

def dubbele_letters(woord):
    resultaat = ""
    for index in range(0,len(woord)):
        resultaat += woord[index] + woord[index]
    return resultaat

print dubbele_letters("The")