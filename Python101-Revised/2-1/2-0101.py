#Example 2.1.1
#Python 3.6.5
#Created By Jooompot Sriyapan

#Dice random dice.

import random

def Dice():
    return random.randint(1,6)

if __name__=='__main__':
    random.seed()
    print (Dice())
