'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.5
Description 
    play with variable
Note
    -
Display
1 3 5
(1, 3, 5, 1, 3, 5)
(1, 3, 5, 1, 3, 5, 1, 3, 5)
1 6 15
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.5
#Python 3.7.3

def example_205():
    a,b,c = 1,3,5
    print (a,b,c)
    print ((a,b,c)*2)
    print ((a,b,c)*3)
    print (a*1,b*2,c*3)

example_205()
