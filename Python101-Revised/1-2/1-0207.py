#Example 1.2.7
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_207():
    a = 9
    b = 3.4
    c = 3e4
    d = "Hello"
    e = True
    f = None
    g = []
    h = [3,4,5,"Hello"]
    i = ()
    j = (3,4,5,"Hello")

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

example_207()

'''
print ("1) a=",a,type(a))   แสดงผล 1) a= 9 <class 'int'>
                            ชนิดของตัวแปล a คือ int
                            
print ("2) b=",b,type(b))   แสดงผล 2) b= 3.4 <class 'float'>
                            ชนิดของตัวแปร b คือ float

print ("3) c=",c,type(c))   แสดงผล 3) c= 30000.0 <class 'float'>
                            ชนิดของตัวแปร c คือ float

print ("4) d=",d,type(d))   แสดงผล 4) d= Hello <class 'str'>
                            ชนิดของตัวแปร d คือ string

print ("5) e=",e,type(e))   แสดงผล 5) e= True <class 'bool'>
                            ชนิดของตัวแปร e คือ boolean
                            
print ("6) f=",f,type(f))   แสดงผล 6) f= None <class 'NoneType'>
                            ชนิดของตัวแปร f คือ NonType
                            
print ("7) g=",g,type(g))   แสดงผล 7) g= [] <class 'list'>
                            ชนิดของตัวแปร g คือ list
                            
print ("8) h=",h,type(h))   แสดงผล 8) h= [3, 4, 5, 'Hello'] <class 'list'>
                            ชนิดของตัวแปร h คือ list

print ("9) i=",i,type(i))   แสดงผล 9) i= () <class 'tuple'>
                            ชนิดของตัวแปร i คือ tuple
                            
print ("10) j=",j,type(j))  แสดงผล 10) j= (3, 4, 5, 'Hello') <class 'tuple'>
                            ชนิดของตัวแปร j คือ tuple
'''
