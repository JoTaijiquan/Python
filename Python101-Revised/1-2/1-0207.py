'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.7
Description 
    mathematics with variable
Note
    print ("1) a+b =",a+b)                           แสดงผล 1) a+b = 17
    print ("2) a-b =",a-b)                           แสดงผล 2) a-b = 1
    print ("3) axb =",a*b)                           แสดงผล 3) axb = 72
    print ("4) a/b =",a/b)                           แสดงผล 4) a/b = 1.125
    print ("5) a//b =",a//b) #หารเอาส่วน              แสดงผล 5) a//b = 1
    print ("6) a mod b =",a%b) #หารเอาเศษ            แสดงผล 6) a mod b = 1
    print ("7) a power b =",a**b) #ยกกำลัง            แสดงผล 7) a power b = 43046721
    print ("8) 3*4+2*3**2*(1+1) =",3*4+2*3**2*(1+1)) แสดงผล 8) 3*4+2*3**2*(1+1) = 48

    ว่าด้วยตัวกระทำทางตรรกะ
    & คือ และ (and)
    | คือ หรือ (or)
    == คือ เท่ากับหรือไม่ (is equal?)
    != คือ ไม่เท่ากับหรือไม่ (is not equal?)
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.7
#Python 3.7.3

def example_207():
    a,b = 9,8
    print ("1) a+b =",a+b)
    print ("2) a-b =",a-b)
    print ("3) axb =",a*b)
    print ("4) a/b =",a/b)
    print ("5) a//b =",a//b) #หารเอาส่วน
    print ("6) a mod b =",a%b) #หารเอาเศษ
    print ("7) a power b =",a**b) #ยกกำลัง
    print ("8) 3*4+2*3**2*(1+1) =",3*4+2*3**2*(1+1))

    print ("1) True and False is",True & False)
    print ("2) True or False is",True | False)
    print ("3) Not True is",not(True))
    print ("4) 3 == 3 is",3==3)
    print ("5) 3 == 4 is",3==4)
    print ("6) not (3==4) is",not(3==4))
    print ("7) 5>4 is",5>4)
    print ("8) 4>4 is",4>4)
    print ("9) 4>=4 is",4>=4)
    print ("10) 5==4 is",5==4)
    print ("11) 5!=5 is",5!=4)
    print ("12) 4==4 is",4==4)  

example_207()
