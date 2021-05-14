#Python 3.9.5
#Example 1-3-5

def func_1_3_5():
    'while ทำงานเป็นวงรอบ ตราบที่ยังเป็นจริง'

    x=0
    while x!=10:
        x = input ("Input x ")
        x = int(x)

        if x==10:
            print ("Yes, you win x=10!!!")
        elif x>10:
            print ("Too high, try again.")
        elif x<10:
            print ("Too low, try again.")
    
    print ("END GAME!!!")

if __name__ == "__main__":
    func_1_3_5()