'''
Create By Joompot Sriyapan
Date 14/4/2019

Name 
    Example 1.4.9
Description 
    for loop
Note
while (True): เป็นจริงตลอดกาล จึงวนรอบไปเรื่อยๆ
ออกจากวนรอบได้เมื่อเจอคำสั่ง break
หรือกดปุ่ม Ctrl-C หรือ Ctrl-D เพื่อหยุดลูป (การวนรอบ)
    
Display
Input 1-10 (10 to Break) 5
x =  5
Input 1-10 (10 to Break) 7
x =  7
Input 1-10 (10 to Break) 10
End Loop
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.4.9
#Python 3.7.3

def example_409():
    while (True):
        x = input("Input 1-10 (10 to Break) ")
        if x== "10":
            print ("End Loop")
            break
        else:
            print ("x = ",x)
    #Can use Ctrl-C or Ctrl-D to break loop

example_409()

