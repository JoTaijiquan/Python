#Example 2.1.6

#Dice

import random

class Dice:
    'คลาสลูกเต๋า สำหรับหาแต้มรวมของลูกเต๋าหลายหน้า'
    NumOfDice = 1
    DiceFace = 6
    TotalScore = 0

    Score=0
    Result=[]

    def __init__(self,NumOfDice=1,DiceFace=6):
        self.NumOfDice = NumOfDice
        self.DiceFace = DiceFace
        random.seed()

    def __TurnDice(self):
        return random.randint(1,self.DiceFace)

    def TurnDices(self):
        self.Result=[]
        self.Score=0
        result=0
        
        for i in range(self.NumOfDice):
            result= self.__TurnDice()
            self.Result.append(result)
            self.Score += result
            
        self.TotalScore += self.Score
        return self.Score

    def Reset(self):
        self.TotalScore = 0
        self.Score = 0
        self.Result = []

    
if __name__=='__main__':
    d = Dice()
    d.NumOfDice = 5
    
    for i in range(3):
        print ("ทอยเต๋าครั้งที่",i+1)
        print ("จำนวน",d.NumOfDice,"ลูก ผลรวม",d.TurnDices(),"แต้ม")
        print ("แต้มที่ออกบนเต๋าแต่ละลูกคือ",d.Result)
        print ("ผลรวมแต้มสะสมคือ", d.TotalScore)
        print ("**********************************\n")

    d.Reset()
    print ("รีเซ็ตแต้มสะสม")
    print ("ทอยเต๋าจำนวน",d.NumOfDice,"ลูก ผลรวม",d.TurnDices(),"แต้ม")
    print ("แต้มที่ออกบนเต๋าแต่ละลูกคือ",d.Result)
    print ("ผลรวมแต้มสะสมคือ", d.TotalScore)
    print ("***********************\n")

    d10 = Dice(NumOfDice=7, DiceFace=10)
    print ("ทอยเต๋า",d10.DiceFace,"หน้า")
    print ("ทอยเต๋าจำนวน",d10.NumOfDice,"ลูก ผลรวม",d10.TurnDices(),"แต้ม")
    print ("แต้มที่ออกบนเต๋าแต่ละลูกคือ",d10.Result)
    print ("ผลรวมแต้มสะสมคือ", d10.TotalScore)
    print ("***********************\n")
    
    d20 = Dice(3, 20)
    print ("ทอยเต๋า",d20.DiceFace,"หน้า")
    print ("ทอยเต๋าจำนวน",d20.NumOfDice,"ลูก ผลรวม",d20.TurnDices(),"แต้ม")
    print ("แต้มที่ออกบนเต๋าแต่ละลูกคือ",d20.Result)
    print ("ผลรวมแต้มสะสมคือ", d20.TotalScore)
    print ("***********************\n")

    print ("Class Document :",d20.__doc__)

    del d, d10, d20
