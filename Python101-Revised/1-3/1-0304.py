'''
Create By Joompot Sriyapan
Date 7/4/2019

Name 
    Example 1.3.4
Description 
    input
Note
    if elif else
    แสดงผล

        input x (guess 1-10)
        ลองป้อน 1
        Noooo, try again (try 11)

        สั่ง Run อีกที
        input x (guess 1-10)
        ลองป้อน 11
        Very close, try again (try 10)

        สั่ง Run อีกที
        input x (guess 1-10)
        ลองป้อน 10
        Yes, you win x=10
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.3.4
#Python 3.7.3

def example_304():
    x = input("Input x (guess 1-10) ")

    if x=="10":
        print ("Yes, you win x=10")
    elif x=="11":
        print ("Very close, try again (try 10)")
    else:
        print ("Noooo, try again (try 11)")

example_304()
