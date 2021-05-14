#Python 3.9.5
#Example 1-8-7

def func_1_8_7():
    'ตัวดำเนินการตรวจสอบการเป็นซับเซ็ตหรือซูเปอร์เซ็ต'

    x= set([3,5,7,9])
    y= set([1,3,5,7,9,11])

    print ("y is superset of x is",y.issuperset(x))
    print ("x is subset of y is",x.issubset(y))
    print ("set(3,7) is subset of y is",set((3,7)).issubset(y))
    if x < y: print ("x<y is",x<y)

if __name__ == "__main__":
    func_1_8_7()