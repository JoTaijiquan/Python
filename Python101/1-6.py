#Chapter 1.6

#Use of List

def example_600():
    #Example 6.00
    for i in (1,1,2,3,5,8,13):
        print (i)

#example_600()

def example_601():
    for i in ("abc",True,2,(3,4,5),"def"): print (i)
#example_601()

def example_602():
    for i in [2,4,6,8,10]:
        print(i)
#example_602()
    
def example_603():
    a =[1,2,3,4,5,6,7,8,9,10]
    for i in a:
        if i==3:
            a[5]=13
        print (i)
#example_603()

def example_604():
    for i in (1,3,5,7,8,9,10):
        print (i)
        if i==5:
            break
        else:
            pass
    print ("end at",i)

#example_604()

def example_605():
    x = [1,3,5,7,9]
    for i in x:
        print (i)
        if i==5:
            x.extend([10,11,12,13])
    print (x)

#example_605()

def example_606():
    for i in "Hello World!":
        print (i)
#example_606()

def example_607():
    for i in str(3.14159):
        print (i)
#example_607()

def example_608():
    for i in ("Superman", "Batman", "Aquaman"):
        print ("Hello",i)
#example_608()

def example_609():
    i=8
    for i in 3,5,7,9,"Superman",False,[1,2,3],(3,4,5),[],(),None,i:
        print (i)
#example_609()

def example_610():
    for i in range(10):
        if i==5:
            pass
        else:
            print (i)
#example_610()

def example_611():
    for i in range(10):
        if i==4:
            continue
        else:
            print (i)
#example_611()

def example_612():
    for i in range(10):
        if i==5:
            break
        else:
            print (i)

#example_612()

def example_613():
    x = [1,2,3]
    try:
        print (x[2])
    except:
        print ("Ha Ha Ha")
        
    try:
        print (x[6])
    except:
        print ("Error x is out of range")
        
example_613()
