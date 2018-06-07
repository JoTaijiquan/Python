#Chapter 1.3

#What if

def example_300():
    #Example 3.00
    x = 10
    y = 11
    
    if x==10:
        print ("Yes, x =",x)

    if y==10:
        print ("Yes, y =",10)
    
#example_300()  ###########################

def example_301():
    #Example 3.01
    x = 10
    y = 11
    
    if x is 10:
        print ("Yes, x =",x)
    if y is 10:
        print ("Yes, y =",y)

#example_301()  ###########################
        
def example_302():
    #Example 3.02
    x = input("Input x (guess 1-10) ")
    
    if x == "10":
        print ("Yes, you win X=10")
    else:
        print ("Noooo, try again (try 10)")

#example_302()

def example_303():
    #Example 3.03
    x = input("Input x (guess 1-10) ")

    if x== "10":
        print ("Yes, you win x=10")
    elif x=="11":
        print ("Very close, try again (try 10)")
    else:
        print ("Noooo, try again (try 11)")

#example_303()

def example_304():
    #Example 3.04
    x = input ("Input x ")
    print (x)
    print (type(x),x)
    x = int(x)
    print (type(x),x)
    x = float(x)
    print (type(x),x)

#example_304()
    
def example_305():
    #Example 3.05
    x=0
    
    while x!=10:
        x = input ("Input x ")
        x = int(x)
    
        if x==10:
            print ("Yes, you win x=10")
        elif x>10:
            print ("Too much, try again")
        elif x<10:
            print ("Too little, try again")

    print ("End Game!!!")

#example_305()


def example_306():
    #Example 3.06
    import random
    
    x = random.randint(1,10)
    print (x)


#example_306()

def example_307():
    #Example 3.07
    import random
    x = 0
    y = random.randint(1,10)
    while x!=y:
        x = int(input ("Input x "))
        
        if x==y:
            print ("Yes, you win x=",y)
        elif x>y:
            print ("Too much, try again")
        elif x<y:
            print ("Too little, try again")

    print ("End Game!!!")

#example_307()

