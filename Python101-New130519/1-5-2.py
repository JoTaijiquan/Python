#Python 3.7.3
#Example 1-5-2

def func_1_5_2():
    'การเรียกข้อมูลใน list'
    
    a = [9,2,5,3,8,7]
    b = ["abc",2,3,False]
    c = "HELLO"

    print ("a[1] =",a[1])
    print ("b[0] =",b[0])
    print ("a[-2] =",a[-2])
    print ("a[1:4]",a[1:4])
    print ("c[2] =",c[2])
    print ("c[2:] =",c[2:])

if __name__ == "__main__":
    func_1_5_2()