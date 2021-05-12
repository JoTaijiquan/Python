#Python 3.9.5
#Example 1-2-5

def func_1_2_5():
    'การทำงานกับตัวแปร'

    a,b,c,d = 1,2,"hello", "world"

    print (a,b,c,d)
    print (a+b, c+d)
    print (a*3, c*3)
    a = a+4 
    b+=7
    print (a,b)
    c+="!"; d*=3
    print (c,d)
    
if __name__ == "__main__":
    func_1_2_5()