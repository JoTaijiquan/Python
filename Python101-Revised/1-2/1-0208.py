'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.8
Description 
    test variable type 
Note
    1) 3x10 power 5 = 300000.0
    2) type of 3e5 = <class 'float'>
    3) 3x10 power 5 = 300000
    4) type of 3*10**5 = <class 'int'>
    5) 3.12345 * 10 power 5 = 312345.0
    6) type of 3.12345e5 = <class 'float'>
    7) 3.12345 * 10 power 5 = 312345.0
    8) type of 3.12345 * 10**5 = <class 'float'>

    แปลงชนิดตัวแปร
    int()    แปลงตัวเลขเป็นชนิด integer
    float()  แปลงตัวเลขเป็น floating point
    string() แปลงตัวเลขเป็น string เก็บตัวอักษร
    แสดงผล
    1) interger of 3.5 = 3
    2) float of 3 = 3.0
    3) 3+3 = 6
    4) float of 3+3 = 6.0
    5) string of 3 + string of 3 = 33
    6) "3" , "3" = 3 3
    7) "3" + "3" = 33
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.8
#Python 3.7.3

def example_208():
    print ("1) 3x10 power 5 =",3e5)
    print ("2) type of 3e5 =",type(3e5))
    print ("3) 3x10 power 5 =",3*10**5)
    print ("4) type of 3*10**5 =",type(3*10**5))
    print ("5) 3.12345 * 10 power 5 =",3.12345e5)
    print ("6) type of 3.12345e5 =",type(3.12345e5))
    print ("7) 3.12345 * 10 power 5 =",3.12345*10**5)
    print ("8) type of 3.12345 * 10**5 =",type(3.12345*10**5))

    print ("1) interger of 3.5 =",int(3.5))
    print ("2) float of 3 =",float(3))
    print ("3) 3+3 =",3+3)
    print ("4) float of 3+3 =",float(3+3))
    print ("5) string of 3 + string of 3 =",str(3)+str(3))
    print ("6) \"3\" , \"3\" =","3","3")
    print ("7) \"3\" + \"3\" =","3"+"3")

example_208()
