#Example 5.15
#Python3.6.5

def example_515():
    x = ['a','x','a','c,','z','a']
    y = x
    
    print ("1) x=",x)
    print ("2) y=",y)
    x.sort()
    print ("3) x.sort() x=",x)
    print ("4) y=",y)
    print ()

    x = ['a','x','a','c,','z','a']
    y = x
    print ("5) x=",x)
    print ("6) y=",y)
    y.sort()
    print ("7) y.sort() y=",y)
    print ("8) x=",x)
    
example_515()

'''
เมื่อกำหนด x=y
x.sort() ค่า y จะเปลี่ยนตาม x ด้วย
หรือ
y.sort() ค่า x ก็จะเปลี่ยนแปลงตาม y

แสดงผล
1) x= ['a', 'x', 'a', 'c,', 'z', 'a']
2) y= ['a', 'x', 'a', 'c,', 'z', 'a']
3) x.sort() x= ['a', 'a', 'a', 'c,', 'x', 'z']
4) y= ['a', 'a', 'a', 'c,', 'x', 'z']

5) x= ['a', 'x', 'a', 'c,', 'z', 'a']
6) y= ['a', 'x', 'a', 'c,', 'z', 'a']
7) y.sort() y= ['a', 'a', 'a', 'c,', 'x', 'z']
8) x= ['a', 'a', 'a', 'c,', 'x', 'z']
'''
