#Python 3.7.3

def func_1_3_1():
    'keyboard input'

    x = input ("Input x ")
    print ("x=",x)
    print ("x=",x,type(x))
    print ("x+3 =",x+"3")
    x = int(x)
    print ("int(x) =",x,type(x))
    print ("x+3 =",x+3)
    x = float(x)
    print ("float(x) =",x,type(x))
    print ("x+3 =",x+3)

if __name__ == "__main__":
    func_1_3_1()