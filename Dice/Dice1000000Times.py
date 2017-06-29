#Python3.6
# -*- coding: utf-8 -*-
#หาสถิติการทอยลูกเต๋า 100000 ครั้ง

from random import randint,seed

class Dice:
    Faces = 0
    Number_of_Dice = 0
    Maximum_Score = 0
    
    Scores = []

    def __init__(self,Faces=6,NumberOfDice=1):
        self.Faces = Faces
        self.Number_of_Dice = NumberOfDice
        self.Maximum_Score = Faces*NumberOfDice
        
    def Rolls(self,Number_of_Roll=1):
        Score = 0
        TotalScore = 0
        
        self.Maximum_Score = self.Faces*self.Number_of_Dice
        self.Scores = [0]*self.Maximum_Score

        for i in range(Number_of_Roll):
            Score = 0
            for j in range(self.Number_of_Dice):
                Score =Score+randint(1,self.Faces)
            self.Scores[Score-1] +=1
            TotalScore += Score
        
        return TotalScore

def ShowGraph (Data=[]):
    DataLen = len(Data)
    DataMax = max(Data)
    DataMax_Len = len(str(DataMax))
    DataCut = 0
    
    if DataMax_Len > 2 :
        DataCut = DataMax_Len-2
    DataDiv = 10**DataCut
    print('____________________________________________')
    print('Score   Amount')
    print('____________________________________________')
    for i in range(DataLen):
        print (repr(i+1).rjust(2),' |', Data[i],'\t| ', end="")
        for j in range(Data[i]//DataDiv):
            print ('+',end=' ')
        print('')

def ShowRoll (Faces,NumberOfDice,NumberOfRoll):
    d = Dice(Faces,NumberOfDice)
    print ('Number of Dices =',d.Number_of_Dice)
    print ('Number of Roll =',NumberOfRoll)
    print ('Maximum Score =',d.Maximum_Score)
    print ('Total Scores =',d.Rolls(NumberOfRoll))    
    print ('Number of Each Faces = ',d.Scores)
    ShowGraph(d.Scores)
    print ('---------')

if __name__ == '__main__':
    seed()
    #ทอยลูกเต๋า 2 ลูก 1,000,000 ครั้ง
    ShowRoll(6,2,1000000)
    print ('')

    #ทอยลูกเต๋า 1 ลูก 1,000,000 ครั้ง
    e = Dice()
    print ('Number of Dices =',e.Number_of_Dice)
    print ('Number of Roll =',1000000)
    print ('Maximum Score =',e.Maximum_Score)    
    print ('Total Score = ',e.Rolls(1000000))
    ShowGraph(e.Scores)
    #del e
