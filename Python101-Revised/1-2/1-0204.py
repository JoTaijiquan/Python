'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.4
Description 
    play with variable
Note
    ความแตกต่างระหว่างตัวแปรแบบตัวเลขและแบบสายอักษร (string)

Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.4
#Python 3.7.3

def example_204(): 
    Hello = 10
    print ("1)",Hello, Hello+5, Hello*10)

    Hello = "10"
    print ("2)",Hello, Hello+"5", Hello*5)

    Hello = "Hello"
    print ("3)", Hello)

    Hello = Hello
    print ("4)", Hello)
    
    print ("5)",Hello+Hello, Hello*3)

    Hello = "Hello!!!" + Hello*3
    print ("6)", Hello)

example_204()
