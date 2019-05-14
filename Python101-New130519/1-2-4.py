#Python 3.7.3

def func_1_2_4():
    'การดำเนินการทางตรรกะ True=จริง False=เท็จ'

    a=True; b=False
    
    print ("True and True =",a&a)
    print ("True and False =",a&b)
    print ("False and False =",b&b)
    print ("True or True =",a|True)
    print ("True or False =",a|False)
    print ("False or False =",b|b)
    print ("Not True =",not(a))
    print ("a==a is",a==a)
    print ("9==8 is",a==b)
    print ("9>8 is",9>8)
    print ("8>=8 is",8>=8)
    print ("8!=9 is",8!=9)
    
if __name__ == "__main__":
    func_1_2_4()