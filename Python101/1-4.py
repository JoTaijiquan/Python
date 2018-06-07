#Chapter 1.4

#Loop

def example_400():
    #Example 4.00
    for i in range(10):
        print (i)

#example_400()

def example_401():
    #Example 4.01
    for i in range(1,10):
        print (i)

#example_401()

def example_402():
    #Example 4.02
    for i in range(1,11,2):
        print (i)

#example_402()

def example_403():
    #Example 4.03
    for i in range(10,1,-2):
        print (i)

#example_403()

def example_404():
    #Example 4.04
    for i in range(-10,10,2):
        print (i)

#example_404()

def example_405():
    #Example 4.05
    for i in range(10,-10,-2):
        print (i)

#example_405()

def example_406():
    #Example 4.06
    for i in range(10):
        if i==5:
            i=i+3
        print (i)

#example_406()

def example_407():
    #Example 4.07
    for i in range(10):
        print (i+1)

#example_407()

def example_408():
    #Example 4.08
    x=1
    while x<5:
        print ("x =",x)
        x=x+1

#example_408()

def example_409():
    #Example 4.09
    x=1
    while x<10:
        print("x=",x)
        x+=2
#example_409()

def example_410():
    #Example 4.10
    z=10
    while z>1:
        print("z=",z)
        z-=2

#example_410()

def example_411():
    #Example 4.11
    y=2
    while y<10000:
        print ("y=",y)
        y*=2

#example_411()

def example_412():
    #Example 4.12
    y=2
    while y<1000000:
        print ("y=",y)
        y**=2

#example_412()

def example_413():
    #Example 4.13
    while (True):
        x = input("Input 10 to Break ")
        if x== "10":
            print ("End Loop")
            break
        else:
            print ("x = ",x)
    #Can use Ctrl-C or Ctrl-D to break loop

#example_413()

