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

example_506()

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

    
def example_520():
    #Example 5.02
    a = (7,8,9)
    print (a)
    print (type(a))
    
    print (a[1])
    print (a(2))

#example_520()
