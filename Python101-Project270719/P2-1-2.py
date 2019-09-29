#Python 3.7.4
#Example P2-1-2

'''จำนวนที่หารด้วย 5 หรือ 7 ลงตัวระหว่าง 10 ถึง 30 คือ 14,15,20,21,25,28  
ซึ่งมีผลบวกคือ 14+15+20+21+25+28 = 123 
ให้หาผลบวกของจำนวนที่หารด้วย 5 หรือ 7 ลงตัวระหว่าง 100 ถึง 300'''

def func_2_1_2():
    ansList=[]
    ansSum = 0
    for i in range (101,300):
        if i%5==0 or i%7==0:
            ansList.append(i)
            ansSum+=i
    return ansList,ansSum


if __name__=="__main__":
    print (__doc__,"\n")
    x = func_2_1_2()
    print('จำนวนทั้งหมดที่หาได้คือ',x[0],'\n')
    print('ผลรวม',x[1])
