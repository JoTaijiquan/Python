'''
Create By Joompot Sriyapan
Date 16/4/2019

Name 
    Example 1.5.7
Description 
    list
Note
    del, pop
Display
    1) x= ['a', 'b', 'c', 1, 3, 5, 7, [0, 1, 2]]
    2) del x[0] x= ['b', 'c', 1, 3, 5, 7, [0, 1, 2]]
    3) del x[3] x= ['b', 'c', 1, 5, 7, [0, 1, 2]]
    4) x.pop()= [0, 1, 2]  x= ['b', 'c', 1, 5, 7]
    5) x.pop()= 7  x= ['b', 'c', 1, 5]
    6) x.pop(1)= c  x= ['b', 1, 5]
    7) x.pop(0)= b  x= [1, 5]
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.7
#Python 3.7.3

def example_507():

    x = ['a','b','c',1,3,5,7,[0,1,2]]

    print ("1) x=",x)
    del x[0]
    print ("2) del x[0] x=",x)
    del x[3]
    print ("3) del x[3] x=",x)
    y = x.pop()
    print ("4) x.pop()=",y," x=",x)
    print ("5) x.pop()=", x.pop()," x=",x)
    print ("6) x.pop(1)=", x.pop(1)," x=",x)
    print ("7) x.pop(0)=", x.pop(0)," x=",x)
    
example_507()
