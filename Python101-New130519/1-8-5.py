#Python 3.7.3
#Example 1-8-5

def func_1_8_5():
    'ตัวดำเนินการอินเตอร์เซ็คชั่น และยูเนี่ยน สำหรับเซ็ต'

    x = set([5, 7, 8, 22])
    y = set([8, 3, 5, 7])
    print (x,y)
    print ("**************************")
    print (x.intersection(y))
    print (x & y)

    print (x.union(y))    
    print (x | y)

if __name__ == "__main__":
    func_1_8_5()