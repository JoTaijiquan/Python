'''
Create By Joompot Sriyapan
Date 13/4/2019

Name 
    Example 1.3.6
Description 
    input
Note
    while x!=10 ให้ทำซ้ำไปเรื่อยๆ ถ้า x ไม่เท่ากับ 10
Display
    Input x 2
    Too little, try again
    Input x 8
    Too little, try again
    Input x 10
    Yes, you win x=10
    End Game!!!
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.3.6
#Python 3.7.3

def example_306():
    x=0
    
    while x!=10:
        x = input ("Input x ")
        x = int(x)
    
        if x==10:
            print ("Yes, you win x=10")
        elif x>10:
            print ("Too much, try again")
        elif x<10:
            print ("Too little, try again")

    print ("End Game!!!")

example_306()

'''
แสดงผล

Input x

ลองป้อน 5

Too little, try again
Input x

ลองป้อน 11

Too much, try again
Input x

ลองป้อน 10
Yes, you win x=10
End Game!!!

คำสั่ง while x!=10 คือคำสั่งวนรอบ ถ้า x!=10 (x ไม่เท่ากับ 10) ให้วนไปเรื่อยๆ 
'''
