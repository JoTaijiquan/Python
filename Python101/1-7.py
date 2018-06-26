#Chapter 1.7

#Function

'''
#Example 7.01
def example_701():
    print ("Hello")

example_701()
'''

'''
#Example 7.02
def example_702(x):
    print ("x=",x)

example_702(10)
'''

'''
#Example 7.03
def example_703(x,y):
    print ("x=",x)
    print ("y=",y)

example_703(10,20)
'''

'''
#Example 7.04
def example_704(x,y):
    print ("x=",x)
    print ("y=",y)

x=10; y=20; a=30; b=40;
example_704(x,y)
example_704(a,b)
'''

'''
#Example 7.05
def example_705(x,y):
    x+=1
    y+=2
    print ("x=",x)
    print ("y=",y)

x=10; y=20
example_705(x,y)
print ("x=",x)
print ("y=",y)
'''

'''
#Example 7.06
def example_706(x):
    x[0] +=10
    print ("Now x=",x,x[0])

x = [10]
print (x,x[0])
example_706(x)
print (x,x[0])
'''

'''
#Example 7.07
def example_707(x,y):
    print ("x=",x)
    print ("y=",y)

x = [10,20,30]
y = 1,1,2,3,5,8

example_707(x,y)
'''

'''
#Example 7.08
def example_708():
    global x
    x = x+10

x = 10
print (x)
example_708()
print (x)
'''

'''
#Example 7.09
def example_709(x,y=10):
    print (x,y)

example_709(10,20)
example_709(10)
'''

'''
#Example 7.10
def example_710(x=10,y=20):
    print (x,y)

example_710()
example_710(1)
example_710(y=100)
example_710(100,200)
example_710(y=100,x=10)
'''

'''
#Example 7.11
def example_711(a=1,b=2,c=3):
    print (a,b,c)

example_711()
example_711(10,c=20)
'''

'''
#Example 7.12
def example_712(*x):
    for i in x:
        print (i)
    print (x)

example_712(1,2,3,"Hello",[0,0,0])
'''

'''
#Example 7.13
def example_713(a=1,b=2,*x):
    for i in x:
        print (i)
    print (a,b,x)
    print ("******")

example_713()
example_713(10)
example_713(11,12)
example_713(10,20,30)
example_713(10,20,30,40,50)
'''

'''
#Example 7.14
def example_714(**x):
    for i,j in x.items():
        print (i,j)
    print ("********")

example_714()
example_714(a=123)
example_714(x=456)
example_714(a=123,b=456,c="Hello",d=[7,8,9],e=(11,12,13),f=(),x=[])
'''

'''
#Example 7.15
def example_715(x):
    x+=10
    return x

y = 0
y = example_715(10)
print (y)
'''

'''
#Example 7.16
def example_716(x):
    x = x+"abc"
    return x

print(example_716(""))
print (example_716("123"))
'''

'''
#Example 7.17
def example_717(x,y,z):
    return [x,y,z]

x = example_717(10,20,30)
print (x)
'''

'''
#Example 7.18
def example_718(x,y,z):
    return(x,y,z)

x = example_718(1,2,3)
print (x)
'''

'''
#Example 7.19
def example_719(x,y,z):
    return [x,y,z]

print (example_719(10,20,[1,3,5]))
'''

'''
#Example 7.20
def example_720(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return "x=y"

print (example_720(10,20))
print (example_720(9,1))
print (example_720(100,100))
'''

'''
#Example 7.21
def example_721(a=0,b=0,c=0):
    return a,b,c

print (example_721())
print (example_721(b=10))
print (example_721(100,101,102)[1])
print (example_721(100,101,102)[2])
'''

'''
#Example 7.22
def example_722():
    pass

example_722()
'''

#Example 7.23
def example_723():
    '''Document
    !!! '''
    pass

example_723()
print (example_722.__doc__)

    
#Example 7.24
def example_724():
    #Document
    pass

print(example_724.__doc__)
