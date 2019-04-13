'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.7
Description 
    Logic
Note

    ว่าด้วยตัวกระทำทางตรรกะ
    & คือ และ (and)
    | คือ หรือ (or)
    == คือ เท่ากับหรือไม่ (is equal?)
    != คือ ไม่เท่ากับหรือไม่ (is not equal?)
Display
    1) a+b = 17
    2) a-b = 1
    3) True and False is  False
    4) True or False is  True
    5) Not True is  False
    6) a == a is True
    7) a == b is False
    8) not (a==b) is True
    9) a>b is True
    10) a>a is False
    11) a>=a is True
    12) a!=a is False
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.7
#Python 3.7.3

def example_207():
    a,b = 9,8
    c,d = True, False
    print ("1) a+b =",a+b)
    print ("2) a-b =",a-b)
    print ("3) True and False is ", c&d)
    print ("4) True or False is ",c|d)
    print ("5) Not True is ", not(c))
    print ("6) a == a is",a==a)
    print ("7) a == b is",a==b)
    print ("8) not (a==b) is",not(a==b))
    print ("9) a>b is",a>b)
    print ("10) a>a is",a>a)
    print ("11) a>=a is",a>=a)
    print ("12) a!=a is",a!=a)

example_207()
