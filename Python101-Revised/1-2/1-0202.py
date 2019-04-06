'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.2
Description 
    swap variable
Note
    สลับค่าระหว่างตัวแปรสองตัวได้ง่ายๆ ด้วยการสั่ง 
    variable_1, variable_2 = variable_2, variable_1
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.2
#Python 3.7.3

def example_202():
    a = 2
    b = "abc"
    print ("1)",a,b)
    b,a = a,b
    print ("2)",a,b)

example_202()
