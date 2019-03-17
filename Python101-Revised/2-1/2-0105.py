#Example 2.1.5
#Python 3.6.5
#Created By Jooompot Sriyapan

#Turn multiple dices keep result or each dice and summary score.

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

def SumDices(NumOfDice=1):
    sum_result=0
    result=Dices(NumOfDice)
    for i in result:
        sum_result = sum_result+i
        
    return result,sum_result
    
if __name__=='__main__':
    random.seed()

    print("ทอยเต๋า 2 ลูก",SumDices(2))
    print ("************")

    x = SumDices(5)
    print ("ทอยเต๋า 5 ลูก ได้",x[0],"รวม",x[1])
    print ("************")

    x = SumDices(5)
    print ("ทอยเต๋า 5 ลูก ได้",x[0],"รวม",x[1])
    print ("************")
    
    print("ทอยเต๋า ไม่กำหนดจำนวนลูก",SumDices())
    
