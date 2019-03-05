#Example 2.1.2

#Dice

import random

def Dice():
    return random.randint(1,6)

if __name__=='__main__':
    random.seed()
    for i in range (10):
        print (Dice())
