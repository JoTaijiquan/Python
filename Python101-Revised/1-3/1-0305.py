'''
Create By Joompot Sriyapan
Date 13/4/2019

Name 
    Example 1.3.5
Description 
    if elif else
Note
    if elif else
Display
ลองป้อนค่าต่างๆ เริ่มจาก 9

Input x (guess 1-10) 9
Too little, try again (try 11)

ลองอีกที ป้อน 11
Input x (guess 1-10) 11
Too much, try again (try 10)

ป้อน 10
Input x (guess 1-10) 10
Yes, you win x=10
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.3.5
#Python 3.7.3

def example_304():
    x = input("Input x (guess 1-10) ")

    if x=="10":
        print ("Yes, you win x=10")
    elif x=="9":
        print ("Too little, try again (try 11)")
    elif x=="11":
        print ("Too much, try again (try 10)")
    else:
        print ("Noooo, try again (try 11)")

example_304()
