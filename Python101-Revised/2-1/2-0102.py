#Example 2.1.2
#Python 3.6.5
#Created By Jooompot Sriyapan

#Turn random dice 10 rounds

import random

def Dice():
    return random.randint(1,6)

if __name__=='__main__':
    random.seed()
    for i in range (10):
        print (Dice())
