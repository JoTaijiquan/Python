'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.1
Description 
    variable
Note
    การกำหนดค่าให้กับตัวแปรหรือ variable เช่นให้

    a = 2               กำหนดค่าตัวแปร a = 2
    b = 999988887777    กำหนดค่าตัวแปร b = 999988887777 
    c = 3.14159         กำหนดค่าตัวแปร c = 3.14159
    d = "ABC"           กำหนดค่าตัวแปร d = "ABC"
    e = "123"           กำหนดค่าตัวแปร e = "123" (เป็นตัวอักษร)
    f = True            กำหนดค่าตัวแปร f = True (จริง)
    F = False           กำหนดค่าตีัวแปร g = False (เท็ํจ)
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.1
#Python 3.7.3

def example_201():
    a = 2
    b = 999988887777 
    c = 3.14159
    d = "ABC"
    e = "123"
    f = True
    F = False

    print ("1) a=",a)
    print ("2) b=",b)
    print ("2) c=",c)
    print ("3) d=",d)
    print ("4) e=",e,"f=",f, "F=",F)

    a = b = c
    print ("5)",a,b,c)

example_201()