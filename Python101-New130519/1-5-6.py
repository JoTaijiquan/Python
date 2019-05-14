#Python 3.7.3

def func_1_5_6():
    'list'
    a = [1,2,3,4,5,6,3,4,3,6]
    b = "HELLO"

    print ("a =",a)
    print ("count 3 in a =",a.count(3))
    print ("count L in b =",b.count("L"))
    a.remove(3)
    print ("a =",a)
    a.remove(3)
    print ("a =",a)
    del a[0]
    print ("a =",a)

if __name__ == "__main__":
    func_1_5_6()
