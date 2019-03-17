#Example 2.1.3
#Python 3.6.5
#Created By Jooompot Sriyapan

#Turn random dice and keep result in List

import random

def Dice():
    return random.randint(1,6)

def Turn(intTurn=1):
    result=[]
    for i in range (intTurn):
        result.append(Dice())
    return result
    
if __name__=='__main__':
    random.seed()
    print (Turn(10))
    print (Turn())
    print (Turn())
