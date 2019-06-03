#Python 3.7.3
#Example 1-3-7

import random

def func_1_3_7():
    'นำ random ไปทำเป็นเกมทายตัวเลข'

    x=0
    random.seed()
    y=random.randint(1,10)

    while x!=y:
        x = int(input("Input x (1-10)"))
        if x==y:
            print ("Yes, you win x=",y,"!!!")
        elif x>y:
            print ("Too high, try again.")
        elif x<y:
            print ("Too low, try again.")
    
    print ("END GAME!!!")

if __name__ == "__main__":
    func_1_3_7()