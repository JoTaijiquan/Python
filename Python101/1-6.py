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

example_604()
