'''
Create By Joompot Sriyapan
Date 7/4/2019

Name 
    Example 1.3.3
Description 
    input
Note
    ใช้คำสั่ง input เพื่อรับค่าจากคีย์บอร์ด

    แสดงผล

        Input x (guess 1-10)
        ลองป้อน 1

        Noooo, try again (try 10)

        สั่ง Run อีกที

        Input x (guess 1-10)
        ลองป้อน 10
        Yes, you win X=10
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.3.3
#Python 3.7.3

def example_303():

    x = input("Input x (guess 1-10) ")
    
    if x=="10":
        print ("Yes, you win X=10")
    else:
        print ("Noooo, try again (try 10)")

example_303()
