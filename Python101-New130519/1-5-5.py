#Python 3.7.3
#Example 1-5-5

def func_1_5_5():
    'การเพิ่มข้อมูลเข้าใน list'
    
    a =[]

    print ("1. a =",a)
    a.append("hello")
    print ("2. a =",a)
    a.append("world")
    print ("3. a =",a)
    a.extend(["!",9,9])
    print ("4. a =",a)
    a.insert (2,"สวัสดี")
    print ("5. a =",a)
    print ("6. find position of '!'=",a.index('!'))
    a.append([0,0,1])
    print ("7. a =",a)

if __name__ == "__main__":
    func_1_5_5()
