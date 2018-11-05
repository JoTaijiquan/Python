#Chapter 1.5

#List

#Example 5.01
def example_501():    
    a = [1,2,3,4,5]
    b = ["abc",2,3,False]

    print ("1) a=",a)
    print ("2) b=",b)
    print ("3) type of a = ",type(a))
    print ("4) type of b = ",type(b))

#example_501()
###########################

#Example 5.02
def example_502():
    a = [1,2,3,4,5]
    b = ["abc",2,3,False]

    print("1) a[1] =",a[1])
    print("2) b[0] =",b[0])

#example_502()
###########################
    
#Example 5.03
def example_503():
    a = [1,2,3,4,5]

    print("1) a[-1]=",a[-1])
    print("2) a[-2]=",a[-2])

#example_503()
###########################
    
#Example 5.04
def example_504():
    a = [1,2,3,4,5]

    print ("1) a = ",a)
    a[0]=7
    a[2]=['a','b',"c,d,e",8,9+2]
    print ("2) a = ",a)

#example_504()
###########################
    
#Example 5.05
def example_505():
    a = [1,2,[11,12,13],4,(21,22,23)]
    
    print ("1) a = ",a)
    print ("2) a[2][1] = ",a[2][1])
    print ("3) type of a is",type(a))
    print ("4) type of a[1] is",type(a[1]))
    print ("5) type of a[2] is",type(a[2]))
    print ("6) type of a[2][1] is",type(a[2][1]))
    print ("7) type of a[4] is",type(a[4]))

#example_505()
###########################
    
#Example 5.06
def example_506():
    a=[1,2,3,4,5]

    print ("1) a=",a)
    a.append(9)
    print ("2) append 9 to a =",a)
    a.extend([7,8,9])
    print ("3) extend [7,8,9] to a =",a)
    a.insert(2,"xyz")
    print ("4) insert xyz at position 2 =",a)
    print ("5) find position of 9 = ",a.index(9))
    print ("6) find position of xyz = ",a.index("xyz"))
    
#example_506()
###########################
    
#Example 5.07
def example_507():
    a = [1,2,3,4,5,6,3,4,3,6]

    print ("1) a=",a)
    print ("2) count 3? =",a.count(3))
    print ("3) count 6? =",a.count(6))

#example_507()
###########################
    
#Example 5.08
def example_508():
    a = [1,2,3,4,5,6]
    print ("1) ",a)
    a.remove (3)
    print ("2) remove 3 from a",a)
    a = [1,2,3,4,5,6,3,4,3]
    print ("3) assign new a = ",a)
    a.remove(3)
    print ("4) remove 3 from a",a)
    a.remove(3)
    print ("5) remove 3 from a",a)
    
#example_508()
###########################
    
#Example 5.09
def example_509():
    x = ['a','b','c','a']
    
    print ("1) x=",x)
    x.append(['d','e'])
    print ("2) append list, x=",x)
    x.remove('a')
    print ("3) remove 'a', x=",x)
    x.remove(['d','e'])
    print ("4) remove ['d','e'], x=",x)
    x.remove('a')
    print ("5) remove 'a', x=",x)

#example_509()
###########################
    
#Example 5.10
def example_510():
    x = ['a','b','c',[3,4,5],'a','b','c']
    
    print ("1) x=",x)
    del x[3]; print ("2) del x[3]=",x)
    del x[2]; print ("3) del x[2]=",x)

#example_510()
###########################
    
#Example 5.11
def example_511():
    x = ['a','b','c',[3,4,5],'a','b','c']
    
    print ("1) x=",x)
    print ("2) pop(2) = ",x.pop(2))
    print ("3) x=",x)
    print ("4) pop(1) = ",x.pop(1))
    print ("5) x=",x)
    print ("6) pop() = ",x.pop())
    print ("7) x=",x)
    print ("8) pop() = ",x.pop())
    print ("9) x=",x)

#example_511()
###########################
    
#Example 5.12
def example_512():
    a = [2,3,6,1,4,8,1,5,3]
    c =[8,7,3,2,3,5,4,2,2,1]
    b = a
    
    print ("1) a=",a)
    print ("2) b=",b,"\n")
    a.sort()
    print("3) sorted a=",a)
    print("4) b=",b,"\n")
    b.reverse()
    print("5) reversed b=",b)
    print("6) a=",a,end="\n\n")
    print ("7) c=",c)
    c.reverse()
    print ("8) reversed c=",c)

#example_512()
###########################
    
#Example 5.13
def example_513():
    i = [11,12,13,14,15,16,17,18,19,20]
    
    print ("1) i=",i)
    print ("2) i[2:5]=",i[2:5]) 
    print ("3) i[2:9:2]=",i[2:9:2])
    #[Start: End before: Skip]#
    print ("4) i[:5]=",i[:5])
    print ("5) i[::2]=",i[::2])
    print ("6) i[::-1]=",i[::-1])
    print ("7) i[::-2]=",i[::-2])
    print ("8) i[-8:-1]=",i[-8:-1])
    print ("9) i[-8:-1:2]=",i[-8:-1:2])
    print ("10) i[-8:-1:-2]=",i[-8:-1:-2])
    print ("11) i[-1:-8]=",i[-1:-8])

#example_513()
###########################
    
#Example 5.14
def example_514():
    x = [1,2,3,4,5]
    y = x
    z = x[:]

    print ("1) x=",x)
    print ("2) y = x, y=",y)
    print ("3) z = x[:], z=",z)
    print()
    x.append(6)
    print ("4) append 6 to x, x=",x)
    print ("5) y=",y)
    print ("6) z=",z)
    print()
    
    x = x = ['a','x','a','c,','z','a']
    print ("7) Assign x=",x)
    print ("8) y=",y)
    print ("9) z=",z)
    print()
    
    y = [5,6,8,1,2,8,8,4,1,2]
    print ("10) Assign y=",y)
    print ("11) x=",x)
    print ("12) z=",z)
    
#example_514()
###########################
    
#Example 5.15
def example_515():
    x = ['a','x','a','c,','z','a']
    y = x
    
    print ("1) x=",x)
    print ("2) y=",y)
    x.sort()
    print ("3) x.sort() x=",x)
    print ("4) y=",y)
    print ()

    x = ['a','x','a','c,','z','a']
    y = x
    print ("5) x=",x)
    print ("6) y=",y)
    y.sort()
    print ("7) y.sort() y=",y)
    print ("8) x=",x)
    
#example_515()
###########################
    
#Example 5.16
def example_516():
    x = ['a','x','a','c,','z','a']
    
    y = x
    print ("1) x=",x)
    print ("2) y=",y)
    x = sorted(x)
    print ("3) x=sorted(x), x=",x)
    print ("4) y=",y)

#example_516()
###########################
    
#Example 5.17
def example_517():
    a = [11,12,13,14,21,22,23,24]
    print ("1)",a[2:2])
    a = [11,12,['xx','yy','zz'],14,21,22,23,24]
    print ("2)",a[2:4])

#example_517()
###########################
    
#Example 5.18
def example_518():
    print ("1) 4 is 4:",4 is 4)
    print ("2) 4 is (4,3):",4 is (4,3))
    print ("3) 4 in (4,3):",4 in (4,3))
    print ("4) (3,4) in (2,3,4):",(3,4) in (2,3,4))
    print ("5) (3,4) in (2,(3,4),4):",(3,4) in (2,(3,4),4))
    print ("6) (3,4) is (2,3,4):",(3,4) is (2,3,4))
    print ("7) (3,4) is (3,4):",(3,4) is (3,4))
    print ("8) (3,4) in (3,4):",(3,4) in (3,4))
    print ("9) (3,4) == (3,4):",(3,4)==(3,4))

#example_518()
###########################
    
#Example 5.19
def example_519():
    a = (7,8,9)
    
    print ("1) ",a)
    print ("2) ",type(a))
    print ("3) ",a[1])

#example_519()
###########################
    
#Example 5.20
def example_520():
    a = [2,3,4]
    b = (9,10,11)
    c = (4,5,6,[1,2,3],8,(9,10),15)
    d = [a,b,c]
    e = (a,b,c)
    f = a,b,c
    g = 2,3,8,10,"a","b"
    
    print ("1) a=",a,"type=",type(a))
    print ("2) b=",b,"type=",type(b))
    print ("3) a[1]=",a[1],type(a[1]))
    print ("4) c[1]=",c[1],type(c[1]))
    print ("5) c[3]=",c[3],type(c[3]))
    print ("6) c[5]=",c[5],type(c[5]))
    print ("7) c[3][1]=",c[3][1],type(c[3][1]))
    print ("8) d=[a,b,c] =",d)
    print ("9) e=(a,b,c) =",e)
    print ("10) f=a,b,c =",f)
    print ("11) g=",g,"type=",type(g))

#example_520()
###########################
    
#Example 5.21
def example_521():
    a = [1,2,3]
    b = [10,20,30]
    c = a+b
    print ("1)",c)
    print ("2)",a*2)
    
#example_521()
###########################

#Example 5.22
def example_522():
    a = 1,2,3
    b = 2,3,4
    c = a+b
    print ("1)",c)
    print ("2)",b*3)
#example_522()
###########################
    
