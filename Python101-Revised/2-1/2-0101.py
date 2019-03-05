#Example 2.1.1

#Dice

import random

def Dice():
    return random.randint(1,6)

if __name__=='__main__':
    random.seed()
    print (Dice())
