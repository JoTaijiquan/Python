#Example 2.1.8
#Python 3.6.5
#Dice in Recursive version.

from random import randint,seed

def DiceR(Faces=6,Number_of_Dice=1,Each_Face=[]):
    'Recursive Dice'
    Each_Face.append(randint(1,Faces))
    if Number_of_Dice != 1:
        DiceR(Faces,Number_of_Dice-1,Each_Face)
    return sum(Each_Face)

if __name__=='__main__':
    seed()
    for i in range(5):
        Dice=[]
        print("ทอยลูกเต๋า 4 ลูก ได้", DiceR(6,4,Dice),"แต้ม, หน้าเต๋า",Dice)
