from random import randint,seed

def DiceI(Faces=6,Number_of_Dice=1,Each_Face=[]): 
    Total= 0
    Each_Roll = 0
    for i in range(Number_of_Dice):
        Each_Roll = randint(1,Faces)
        Each_Face.append(Each_Roll)
        Total = Total+Each_Roll
    return Total

seed()

def Dice():
    Face = randint(1,6)
    print (Face)


    

Dice()



