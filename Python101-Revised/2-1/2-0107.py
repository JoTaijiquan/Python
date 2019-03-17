#Example 2.1.7
#Python 3.6.5
#Created By Jooompot Sriyapan

#Dice in Iterative version.

from random import randint,seed

def DiceI(Faces=6,Number_of_Dice=1,Each_Face=[]): 
    'Iterative Dice'
    for i in range(Number_of_Dice):
        Each_Face.append(randint(1,Faces))
    return sum(Each_Face)

if __name__=='__main__':
    seed()
    for i in range(5):
        Dice=[]
        print("ทอยลูกเต๋า 4 ลูก ได้", DiceI(6,4,Dice),"แต้ม, หน้าเต๋า",Dice)
