#Chapter 1.6

#Use of List

#Example 6.01
def example_601():
    #Example 6.01
    for i in (1,1,2,3,5,8,13):
        print (i)

#example_601()
###########################

#Example 6.02
def example_602():
    for i in ("abc",True,2,(3,4,5),"def"): print (i)

#example_602()
###########################

#Example 6.03
def example_603():
    for i in [2,4,6,8,10]:
        print(i)

#example_603()
###########################

#Example 6.04
def example_604():
    a =[1,2,3,4,5,6,7,8,9,10]
    for i in a:
        if i==3:
            a[5]=13
        print (i)
        
#example_604()
###########################
        
#Example 6.05
def example_605():
    for i in (1,3,5,7,8,9,10):
        print (i)
        if i==5:
            break
        else:
            pass
    print ("end at",i)

#example_605()
###########################

#Example 6.06
def example_606():
    x = [1,3,5,7,9]
    for i in x:
        print (i)
        if i==5:
            x.extend([10,11,12,13])
    print (x)

#example_606()
###########################
    
#Example 6.07
def example_607():
    for i in "Hello World!":
        print (i)

#example_607()
###########################
        
#Example 6.08
def example_608():
    for i in str(3.14159):
        print (i)

#example_608()
###########################
        
#Example 6.09
def example_609():
    for i in ("Superman", "Batman", "Aquaman"):
        print ("Hello",i)

#example_609()
###########################

#Example 6.10
def example_610():
    i=8
    for i in 3,"Superman",False,[1,2,3],(3,4),[],(),i,None,i:
        print (i)

#example_610()
###########################
        
#Example 6.11
def example_611():
    for i in range(10):
        if i==5:
            pass
        else:
            print (i)

#example_611()
###########################
            
#Example 6.12
def example_612():
    for i in range(10):
        if i==4:
            continue
        else:
            print (i)

#example_612()
###########################
                        
#Example 6.13
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
###########################
