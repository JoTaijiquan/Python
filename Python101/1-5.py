#Chapter 1.5

#List

def example_500():
    #Example 5.00
    a = [1,2,3,4,5]
    b = ["abc",2,3,False]

    print ("a=",a)
    print ("b=",b)
    print ("type of a = ",type(a))
    print ("type of b = ",type(b))

#example_500()  ###########################

def example_501():
    #Example 5.01
    a = [1,2,3,4,5]
    b = ["abc",2,3,False]

    print("a[1] =",a[1])
    print("b[0] =",b[0])

#example_501()

def example_502():
    #Example 5.02
    a = [1,2,3,4,5]

    print("a[-1]=",a[-1])
    print("a[-2]=",a[-2])

#example_502()

def example_503():
    #Example 5.03
    a = [1,2,3,4,5]

    print ("a = ",a)
    a[0]=7
    a[2]=['a','b',"c,d,e",8,9+2]
    print ("a = ",a)

#example_503()

def example_504():
    #Example 5.04
    a = [1,2,[11,12,13],4,(21,22,23)]
    
    print ("a = ",a)
    print ("a[2][1] = ",a[2][1])
    print ("type of a is",type(a))
    print ("type of a[1] is",type(a[1]))
    print ("type of a[2] is",type(a[2]))
    print ("type of a[2][1] is",type(a[2][1]))
    print ("type of a[4] is",type(a[4]))

#example_504()

def example_505():
    #Example 5.05
    a=[1,2,3,4,5]

    print ("a=",a)
    a.append(9)
    print ("append 9 to a =",a)
    a.extend([7,8,9])
    print ("extend [7,8,9] to a =",a)
    a.insert(2,"xyz")
    print ("insert xyz at position 2 =",a)
    print ("find position of 9 = ",a.index(9))
    print ("find position of xyz = ",a.index("xyz"))
    
#example_505()

def example_506():
    #Example 5.06
    a = [1,2,3,4,5,6,3,4,3,6]

    print ("a=",a)
    print ("count how many 3? =",a.count(3))
    print ("count how many 6? =",a.count(6))

#example_506()

def example_507():
    #Example 5.07
    a = [1,2,3,4,5,6]
    print (a)
    a.remove (3)
    print ("remove 3 from a",a)
    a = [1,2,3,4,5,6,3,4,3]
    print ("assign new a = ",a)
    a.remove(3)
    print ("remove 3 from a",a)
    a.remove(3)
    print ("remove 3 from a",a)
    
#example_507()

def example_508():
    #Example 5.08
    x = ['a','b','c','a']
    print ("x=",x)
    x.append(['d','e'])
    print ("append list to x, x=",x)
    x.remove('a')
    print ("remove a from list, x=",x)
    x.remove(['d','e'])
    print ("remove ['d','e'] from list, x=",x)
    x.remove("a")
    print ("remove a from list,x=",x)

#example_508()

def example_509():
    #Example 5.09
    x = ['a','b','c',[3,4,5],'a','b','c']
    print ("x=",x)
    del x[3]; print ("del x[3]=",x)
    del x[2]; print ("del x[2]=",x)

#example_509()

def example_510():
    #Example 5.10
    x = ['a','b','c',[3,4,5],'a','b','c']
    print ("x=",x)
    print ("pop(2) = ",x.pop(2))
    print()
    print ("x=",x)
    print ("pop(1) = ",x.pop(1))
    print()
    print ("x=",x)
    print ("pop() = ",x.pop())
    print ("x=",x)
    print ("pop() = ",x.pop())
    print ("x=",x)

#example_510()

def example_511():
    #Example 5.11
    a = [2,3,6,1,4,8,1,5,3]
    c =[8,7,3,2,3,5,4,2,2,1]
    b = a
    print ("a=",a)
    print ("b=",b,"\n")
    a.sort()
    print("sorted a=",a)
    print("b=",b,"\n")
    b.reverse()
    print("reversed b=",b)
    print("a=",a,end="\n\n")
    print ("c=",c)
    c.reverse()
    print ("reversed c=",c)

#example_511()
    
def example_512():
    #Example 5.12
    i = [11,12,13,14,15,16,17,18,19,20]
    print ("i=",i)
    print ("i[2:5]=",i[2:5]) 
    print ("i[2:9:2]=",i[2:9:2]) #Start:End before:Skip
    print ("i[:5]=",i[:5])
    print ("i[::2]=",i[::2])
    print ("i[::-1]=",i[::-1])
    print ("i[::-2]=",i[::-2])
    print ("i[-8:-1]=",i[-8:-1])
    print ("i[-8:-1:2]=",i[-8:-1:2])
    print ("i[-8:-1:-2]=",i[-8:-1:-2])
    print ("i[-1:-8]=",i[-1:-8])

#example_512()

def example_513():
    #Example 5.13
    x = [1,2,3,4,5]
    y = x
    z = x[:]
    print ("x=",x)
    print ("y = x, y=",y)
    print ("z = x[:], z=",z)
    print()
    x.append(6)
    print ("append 6 to x, x=",x)
    print ("y=",y)
    print ("z=",z)
    print()
    x = x = ['a','x','a','c,','z','a']
    print ("Assign x=",x)
    print ("y=",y)
    print ("z=",z)
    print()
    y = [5,6,8,1,2,8,8,4,1,2]
    print ("Assign y=",y)
    print ("x=",x)
    print ("z=",z)
    print()
    
#example_513()

def example_514():
    #Example 5.14
    x = ['a','x','a','c,','z','a']
    y = x
    print ("x=",x)
    print ("y=",y)
    x.sort()
    print ("x.sort() x=",x)
    print ("y=",y)
    print ()

    x = ['a','x','a','c,','z','a']
    y = x
    print ("x=",x)
    print ("y=",y)
    y.sort()
    print ("y.sort() y=",y)
    print ("x=",x)
    print ()
    
    x = ['a','x','a','c,','z','a']
    y = x
    print ("x=",x)
    print ("y=",y)
    x = sorted(x)
    print ("x=sorted(x), x=",x)
    print ("y=",y)
    
#example_514()

def example_515():
    #Example 5.15
    a = [11,12,13,14,21,22,23,24,31,32,33,34]
    print (a[2:2])
    a = [11,12,['xx','yy','zz'],14,21,22,23,24,31,32,33,34]
    print (a[2:4])

#example_515()

def example_516():
    #Example 5.16
    print ("4 is 4",4 is 4)
    print ("4 is (4,3)",4 is (4,3))
    print ("4 in (4,3)",4 in (4,3))
    print ("(3,4) in (2,3,4)",(3,4) in (2,3,4))
    print ("(3,4) in (2,(3,4),4)",(3,4) in (2,(3,4),4))
    print ("(3,4) is (2,3,4)",(3,4) is (2,3,4))
    print ("(3,4) is (3,4)",(3,4) is (3,4))
    print ("(3,4) in (3,4)",(3,4) in (3,4))
    print ("(3,4) == (3,4)",(3,4)==(3,4))

#example_516()

def example_517():
    #Example 5.17
    a = (7,8,9)
    print (a)
    print (type(a))
    
    print (a[1])
    print (a(2))

#example_517()

def example_518():
    #Example 5.18
    a = [2,3,4]
    b = (9,10,11)
    c = (4,5,6,[1,2,3],8,(9,10,11),15,16)
    d = [a,b,c]
    e = (a,b,c)
    f = a,b,c
    g = 2,3,8,10,"a","b"
    print ("a=",a)
    print ("b=",b)
    print ("type of a=",type(a))
    print ("type of b=",type(b))
    print ("a[1]=",a[1])
    print ("c[1]=",c[1])
    print ("c[3]=",c[3])
    print ("c[5]=",c[5])
    print ("c[3][1]=",c[3][1])
    print ("d=[a,b,c] =",d)
    print ("e=(a,b,c) =",e)
    print ("f=a,b,c =",f)
    print ("g=",g)

#example_518()

def example_519():
    #Example 5.19
    a = [1,2,3]
    b = [10,20,30]
    c = a+b
    print (c)

#example_519()

def example_520():
    #Example 5.20
    a = 1,2,3
    b = 5,6,7,8
    c = a+b
    print (c)

#example_520()

def example_521():
    #Example 5.21
    a = [1,2,3]
    print (a*2)

#example_521
    
def example_522():
    #Example 5.22
    a = 3,4,5
    print (a*3)

#example_522()
