#Python 3.9.5
#Example 1-3-4

def func_1_3_4():
    'พัฒนาเกมทายตัวเลข'

    x=input("Input x (guess 1-10) ")

    if x=="10":
        print ("Yes, you win x=10!!!")
    elif x=="9":
        print ("Too low, try again (try 11)")
    elif x=="11":
        print ("Too high, try again (try 10)")
    else:
        print ("Nooo, try again (try 11)")
        
if __name__ == "__main__":
    func_1_3_4()