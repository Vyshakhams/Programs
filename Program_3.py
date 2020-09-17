heads = int(input("Enter Total Number Heads"))
legs = int(input("Enter Total Number legs"))
"""
c + r = Heads
4r + 2c = legs
r = Heads - C 
4(Heads-c) + 2c = legs
4 * Heads - 2c = legs

"""
def calculateNoOfChicken(heads,legs):
    chicken = 0
    #Based on equation we got above
    chicken = (4*heads - legs )/2
    return int(chicken)


noOfChickens = calculateNoOfChicken(heads,legs)

noOfRabbits = heads - noOfChickens

print("Number Of Rabbits = ",int(noOfRabbits))
print("Number Of Chickens = ",int(noOfChickens))

