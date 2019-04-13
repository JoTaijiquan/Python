'''
Create By Joompot Sriyapan
Date 13/4/2019

Name 
    Example 1.3.4
Description 
    if else
Note
    if else
Display
    Input x (guess 1-10) 10
    Yes, you win X=10
ลองอีกที
    Input x (guess 1-10) 11
    Noooo, try again (try 10)
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
        print ("Yes, you win X=10")
    else:
        print ("Noooo, try again (try 10)")

example_304()
