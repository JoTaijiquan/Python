'''
Create By Joompot Sriyapan
Date 7/4/2019

Name 
    Example 1.2.9
Description 
    multi-command in a line
Note
    จบคำสั่งด้วย ; สามารถใช้หลายคำสั่งในหนึ่งบรรทัด
Display
1.  10
2.  20
3.  30
4.  25
5.  50
6.  10.0
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.9
#Python 3.7.3

def example_209():
    a = 10;     print ("1. ",a)
    a = a+10;   print ("2. ",a)
    a+=10;      print ("3. ",a)
    a-=5;       print ("4. ",a)
    a*=2;       print ("5. ",a); a/=5;  print ("6. ",a)
    
example_209()

