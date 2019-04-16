'''
Create By Joompot Sriyapan
Date 16/4/2019

Name 
    Example 1.5.6
Description 
    list
Note
    del ลลข้อมูลใน list
Display
    1) x= ['a', 'b', 'c', 'a']
    2) append ['d','e'], x= ['a', 'b', 'c', 'a', ['d', 'e']]
    3) remove 'a', x= ['b', 'c', 'a', ['d', 'e']]
    4) remove ['d','e'], x= ['b', 'c', 'a']
    5) extend [1,2,3,4] x= ['b', 'c', 'a', 1, 2, 3, 4]
    6) del x[2], x= ['b', 'c', 1, 2, 3, 4]
    7) del x[0], x= ['c', 1, 2, 3, 4]
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.7
#Python 3.7.3

def example_507():
    x = ['a','b','c','a']
    
    print ("1) x=",x)
    x.append(['d','e'])
    print ("2) append ['d','e'], x=",x)
    x.remove('a')
    print ("3) remove 'a', x=",x)
    x.remove(['d','e'])
    print ("4) remove ['d','e'], x=",x)
    x.extend ([1,2,3,4])
    print ("5) extend [1,2,3,4] x=",x)
    del x[2]
    print ("6) del x[2], x=",x)
    del x[0]
    print ("7) del x[0], x=",x)
example_507()
