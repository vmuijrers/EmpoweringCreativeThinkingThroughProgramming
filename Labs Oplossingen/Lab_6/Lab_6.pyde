#Lab 6 Valentijn Muijrers

#6_0
def wheels(cars,trikes,bikes):
    return 4*cars + 3 *trikes + 2*bikes

#6_1
def XOR(a, b):
    return !a and b or a and !b

#6_2
def pancakes(eggs, milk, flower):
    
    batches = min(eggs /2, milk/500, flower/250)
    eggsUsed = batches * 2
    milkUsed = batches * 500
    flowerUsed = batches * 250
    eggsLeft = eggs- eggsUsed
    milkLeft = milk - milkUsed
    flowerLeft = flower - flowerUsed
    print("You can make: " +str(batches*10)+" pancakes from "+ str(eggsUsed) +" eggs, " + str(milkUsed) + " ml milk and " + str(flowerUsed)+ " grams of flower and\n \
          have: "+str(eggsLeft)+" eggs left, " +str(milkLeft) +" ml of milk left and " + str(flowerLeft) + " grams of flower left")
    return batches * 10

print pancakes(10,2000,1000)
    
