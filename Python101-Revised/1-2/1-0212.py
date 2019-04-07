'''
Create By Joompot Sriyapan
Date 7/4/2019

Name 
    Example 1.2.12
Description 
    multi-command in a line
Note
    จบคำสั่งด้วย ; สามารถใช้หลายคำสั่งในหนึ่งบรรทัด
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.12
#Python 3.7.3

def example_212():
    a = 10;     print ("1) ",a)
    a = a+10;   print ("2) ",a)
    a+=10;      print ("3) ",a)
    a-=5;   print ("4) ",a); a*=2;  print ("5) ",a); a/=5;  print ("6) ",a)
    
example_212()

