#Python 3.9.5
#Example 1-8-6

def func_1_8_6():
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
    func_1_8_6()