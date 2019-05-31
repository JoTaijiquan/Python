#Python 3.7.3

def func_1_7_4(x):
    x[0] +=10
    print ("Now x=",x)

if __name__ == "__main__":
    x=[10]
    print ("x=",x)
    func_1_7_4(x)
    print ("x=",x)
    func_1_7_4(x)