#Example 1.3.8
#Python 3.6.5
#Created By Jooompot Sriyapan

import random
def example_308():
    x = 0
    y = random.randint(1,10)
    while x!=y:
        x = int(input ("Input x (1-10) "))
        
        if x==y:
            print ("Yes, you win x=",y)
        elif x>y:
            print ("Too much, try again")
        elif x<y:
            print ("Too little, try again")

    print ("End Game!!!")

example_308()

'''
ลองสร้างเกมทายตัวเลขแบบง่ายๆ ระหว่าง 1-10
'''
