#Example 2.1.4

#Dice

import random

def Dice():
    return random.randint(1,6)

def Dices(NumOfDice=1):
    result=[]
    for i in range(NumOfDice):
        result.append(Dice())
    return result

def Turn(NumOfTurn=1,NumOfDice=1):
    result=[]
    for i in range(NumOfTurn):
        result.append(Dices(NumOfDice))
    return result
    
if __name__=='__main__':
    random.seed()
    print ("ทอยเต๋า 5 ครั้ง ครั้งละ 1 ลูก",Turn(5))
    print ("ทอยเต๋า 5 ครั้ง ครั้งละ 2 ลูก",Turn(5,2))
    print ("ทอยเต๋า 2 ครั้ง ครั้งละ 3 ลูก",Turn(2,3))
    print ("ทอยเต๋า 1 ครั้ง ครั้งละ 1 ลูก",Turn())
