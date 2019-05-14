#Python 3.7.3

def func_1_4_5():
    'while True'

    while True:
        x = input ("Input 1-10 (10 to Break) ")
        if x=="10":
            print ("END LOOP!!!")
            break
        else:
            print ("x =",x)
if __name__ == "__main__":
    func_1_4_5()