#Python 3.7.3
#Example 1-5-7

def func_1_5_7():
    'เรียงข้อมูลใน list ด้วย sort และ reverse'

    a = [2,3,6,1,4,8,1,5,3]
    b = a
    
    print ("a =",a)
    print ("b =",b)
    a.sort()
    print ("a =",a)
    print ("b =",b)
    b.reverse()
    print ("a =",a)
    print ("b =",b)



if __name__ == "__main__":
    func_1_5_7()
