#Python 3.7.3
#Example 1-3-3

def func_1_3_3():
    'สร้างเกมทายตัวเลข'

    x=input("Input x (guess 1-10) ")

    if x=="10":
        print ("Yes, you win x=10!!!")
    else:
        print ("Nooo, try again (try 10)")
        
if __name__ == "__main__":
    func_1_3_3()