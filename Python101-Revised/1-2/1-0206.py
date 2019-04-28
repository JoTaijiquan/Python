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
a= 9 <class 'int'>
b= 3.4 <class 'float'>
c= 30000.0 <class 'float'>
d= (3+4j) <class 'complex'>
e= Hello <class 'str'>
f= True <class 'bool'>
g= None <class 'NoneType'>
h= [] <class 'list'>
i= [3, 4, 5, 'Hello'] <class 'list'>
j= () <class 'tuple'>
k= (3, 4, 5, 'Hello') <class 'tuple'>
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

    print ("a=",a,type(a))
    print ("b=",b,type(b))
    print ("c=",c,type(c))
    print ("d=",d,type(d))
    print ("e=",e,type(e))
    print ("f=",f,type(f))
    print ("g=",g,type(g))
    print ("h=",h,type(h))
    print ("i=",i,type(i))
    print ("j=",j,type(j))
    print ("k=",k,type(k))

example_206()
