'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.2.6
Description 
    variable type
Note
    -
Display
    1) a= 9 <class 'int'>
    2) b= 3.4 <class 'float'>
    3) c= 30000.0 <class 'float'>
    4) d= (3+4j) <class 'complex'>
    5) e= Hello <class 'str'>
    6) f= True <class 'bool'>
    7) g= None <class 'NoneType'>
    8) h= [] <class 'list'>
    9) i= [3, 4, 5, 'Hello'] <class 'list'>
    10) j= () <class 'tuple'>
    11) k= (3, 4, 5, 'Hello') <class 'tuple'>
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.6
#Python 3.7.3

def example_206():
    a = 9; b=3.4; c=3e4; 
    d = 3+4j; e = "Hello"; f = True; 
    g = None
    h = []
    i = [3,4,5,"Hello"]
    j = ()
    k = (3,4,5,"Hello")

    print ("1) a=",a,type(a))
    print ("2) b=",b,type(b))
    print ("3) c=",c,type(c))
    print ("4) d=",d,type(d))
    print ("5) e=",e,type(e))
    print ("6) f=",f,type(f))
    print ("7) g=",g,type(g))
    print ("8) h=",h,type(h))
    print ("9) i=",i,type(i))
    print ("10) j=",j,type(j))
    print ("11) k=",k,type(k))

example_206()
