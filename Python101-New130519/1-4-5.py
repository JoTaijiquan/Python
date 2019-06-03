#Python 3.7.3
#Example 1-4-5

def func_1_4_5():
    'while True วงรอบอนันต์ ทำงานไปเรื่อยๆ จนกว่าจะเจอ break'

    while True:
        x = input ("Input 1-10 (10 to Break) ")
        if x=="10":
            print ("END LOOP!!!")
            break
        else:
            print ("x =",x)
if __name__ == "__main__":
    func_1_4_5()