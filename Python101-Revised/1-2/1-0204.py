'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.4
Description 
    swap multiple variable
Note
    สลับค่าตัวแปรทีละหลายๆ ตัว
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.4
#Python 3.7.3

def example_204():
    a = 3+5
    b = True
    c = 999
    d = "ddd"
    e = "eee"
    f = "fff"

    print ("1) a b c =",a,b,c)

    a,b,c = b,c,a
    print ("2) a b c =",a,b,c,)

    a,b,c = d,e,f
    print ("3) a b c = ",a,b,c)

example_204()
