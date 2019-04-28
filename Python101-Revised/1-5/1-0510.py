'''
Create By Joompot Sriyapan
Date 20/4/2019

Name 
    Example 1.5.10
Description 
    list
Note

Display

Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.10
#Python 3.7.3

def example_510():
    x = [1,2,3,4,5]
    y = x
    z = x[:]

    print ("1) x=",x)
    print ("2) y = x, y=",y)
    print ("3) z = x[:], z=",z)
    print()
    x.append(6)
    print ("4) append 6 to x, x=",x)
    print ("5) y=",y)
    print ("6) z=",z)
    print()
    
    x = ['a','x','a','c,','z','a']
    print ("7) Assign x=",x)
    print ("8) y=",y)
    print ("9) z=",z)
    print()
    
    y = [5,6,8,1,2,8,8,4,1,2]
    print ("10) Assign y=",y)
    print ("11) x=",x)
    print ("12) z=",z)
    
example_510()

'''
print ("1) x=",x)                   แสดงค่า x= [1, 2, 3, 4, 5]
print ("2) y = x, y=",y)            แสดงค่า y= [1, 2, 3, 4, 5]
print ("3) z = x[:], z=",z)         แสดงค่า z= [1, 2, 3, 4, 5]

ข้อสังเกต 
y=x กำหนดให้ y = x
z=x[:] z = ค่าภายใน x

x.append(6)                         เพิ่มค่า 6 ให้ x
print ("4) append 6 to x, x=",x)    แสดงค่า x= [1, 2, 3, 4, 5, 6]
print ("5) y=",y)                   แสดงค่า y= [1, 2, 3, 4, 5, 6]
print ("6) z=",z)                   แสดงค่า z= [1, 2, 3, 4, 5]

ข้อสังเกต
เมื่อเพิ่มค่าใน list x, list y จะเปลี่ยนแปลงตามไปด้วย
แต่ list z ไม่เปลี่ยนแปลง

x = ['a','x','a','c,','z','a']      กำหนดค่า x= ['a','x','a','c,','z','a'] 
print ("7) Assign x=",x)            แสดงค่า x= ['a','x','a','c,','z','a']  
print ("8) y=",y)                   แสดงค่า y= [1, 2, 3, 4, 5, 6]
print ("9) z=",z)                   แสดงค่า z= [1, 2, 3, 4, 5]

ข้อสังเกต
เมื่อกำหนดค่า list x ใหม่ให้ x = ['a','x','a','c,','z','a'] ไม่ส่งผลต่อ list y และ list z

y = [5,6,8,1,2,8,8,4,1,2]           กำหนดค่า y= [5,6,8,1,2,8,8,4,1,2] 
print ("10) Assign y=",y)           แสดงค่า y= [5,6,8,1,2,8,8,4,1,2] 
print ("11) x=",x)                  แสดงค่า x= ['a','x','a','c,','z','a']
print ("12) z=",z)                  แสดงค่า z= [1, 2, 3, 4, 5]

แสดงผล
1) x= [1, 2, 3, 4, 5]
2) y = x, y= [1, 2, 3, 4, 5]
3) z = x[:], z= [1, 2, 3, 4, 5]

4) append 6 to x, x= [1, 2, 3, 4, 5, 6]
5) y= [1, 2, 3, 4, 5, 6]
6) z= [1, 2, 3, 4, 5]

7) Assign x= ['a', 'x', 'a', 'c,', 'z', 'a']
8) y= [1, 2, 3, 4, 5, 6]
9) z= [1, 2, 3, 4, 5]

10) Assign y= [5, 6, 8, 1, 2, 8, 8, 4, 1, 2]
11) x= ['a', 'x', 'a', 'c,', 'z', 'a']
12) z= [1, 2, 3, 4, 5]
'''
