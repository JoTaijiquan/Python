#Python3.5
from random import randint,seed

#Recursive Dice
def DiceR(Faces=6,Number_of_Dice=1,Each_Face=[]): 
    Each_Face.append(randint(1,Faces))
    if Number_of_Dice != 1:
        DiceR(Faces,Number_of_Dice-1,Each_Face)
    return sum(Each_Face)

#Iterative Dice
def DiceI(Faces=6,Number_of_Dice=1,Each_Face=[]): 
    Total= 0
    Each_Roll = 0
    for i in range(Number_of_Dice):
        Each_Roll = randint(1,Faces)
        Each_Face.append(Each_Roll)
        Total = Total+Each_Roll
    return Total

if __name__ == '__main__':
    seed()
    
    Dices = DiceI 
    for i in range(5):
        Dice=[]
        print (Dices(6,4,Dice),Dice)
    print (Dices(6,1))

    print()
    
    Dices = DiceR
    for i in range(5):
        Dice=[]
        print (Dices(6,4,Dice),Dice)
    print (Dices(6,1))
