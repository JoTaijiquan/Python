#Chapter 1.2

#Know the variable.

def example_200():
    #Example 200
    a = 2
    b = 999999988888877777
    c = 3.14159265358
    d = "ABC"
    e = True

    print ("a=",a)
    print ("b=",b)
    print ("c=",c)
    print ("a=",a,"b=",b,"c=",c,"d=",d,"e=",e)

    a = b = c
    print (a,b,c)

#example_200()    ###########################

def example_201():
    #Example 2.01
    a = 2
    b = "abc"
    print (a,b)
    b,a = a,b
    print (a,b)

#example_201()  ###########################

def example_202():
    #Example 2.02
    a = b = 2
    c = d = 4
    print (a,b,c,d)

#example_202()  ###########################

def example_203():
    #Example 2.03
    a = 3+5
    b = True
    c = 999
    d = "ddd"
    e = "eee"
    f = "fff"

    print ("a b c =",a,b,c)

    a,b,c = b,c,a
    print ("a b c =",a,b,c,)

    a,b,c = d,e,f
    print ("a b c = ",a,b,c)

#example_203()  ###########################

def example_204():
    #Example 2.04
    Hello = 0
    print (Hello)
    print ("-------")
    Hello = "Hello"
    print (Hello)
    print ("-------")
    print ('Hello')
    print ("Hello")
    print ("-------")
    print ("\"Hello\"")
    print ("\'Hello\'")
    print ("-------")
    print ("'Hello'")
    print ('"Hello"')
    print ("-------")
    print ("\\Hello\\")
    print ("Hello\tHello")

#example_204()  ###########################

def example_205():
    #Example 2.05
    a,b,c = 1,3,5
    print (a,b,c)
    print ((a,b,c)*2)
    print ((a,b,c)*3)

#example_205()  ###########################

def example_206():
    #Example 2.06

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

    print ("a=",a)
    print("type a is",type(a),"\n")

    print ("b=",b)
    print("type b is",type(b),"\n")

    print ("c=",c)
    print("type c is",type(c),"\n")

    print ("d=",d)
    print("type d is",type (d),"\n")

    print ("e=",e)
    print("type e is",type(e),"\n")

    print ("f=",f)
    print("type f is",type(f),"\n")

    print ("g=",g)
    print("type g is",type(g),"\n")

    print ("h=",h)
    print("type h is",type(h),"\n")

    print ("i=",i)
    print("type i is",type(i),"\n")

    print ("j=",j)
    print("type j is",type(j),"\n")

#example_206()  ###########################

def example_207():
    #Example 2.07
    a,b = 9,8
    print("a+b =",a+b)
    print("a-b =",a-b)
    print("axb =",a*b)
    print("a/b =",a/b)
    print("a//b =",a//b) #หารเอาส่วน
    print("a mod b =",a%b) #หารเอาเศษ
    print("a power b =", a**b) #ยกกำลัง
    print ("3*4+2*3**2*(1+1) = ",3*4+2*3**2*(1+1))

#example_207()  ###########################

def example_208():
    #Example 2.08
    print ("True and False is ",True & False)
    print ("True or False is ",True | False)
    print ("Not True is ", not(True))
    print ("3 == 3 is ",3==3)
    print ("3 == 4 is ",3==4)
    print ("not (3==4) is",not(3==4))
    print ("5>4 is",5>4)
    print ("4>4 is",4>4)
    print ("4>=4 is",4>=4)
    print ("5==4 is",5==4)
    print ("5!=5 is",5!=4)
    print ("4==4 is",4==4)
    

#example_208()  ###########################

def example_209():
    #Example 2.09
    print ("3x10 power 5 = ",3e5)
    print ("type of 3e5 = ",type(3e5),"\n")

    print ("3x10 power 5 = ",3*10**5)
    print ("type of 3*10**5 = ",type(3*10**5),"\n")

    print ("3.12345 * 10 power 5 = ",3.12345e5)
    print ("type of 3.12345e5 = ",type(3.12345e5),"\n")

    print ("3.12345 * 10 power 5 = ",3.12345*10**5)
    print ("type of 3.12345 * 10**5 = ",type(3.12345*10**5),"\n")

#example_209()  ###########################

def example_210():
    #Example 2.10
    print ("interger of 3.5 = ",int(3.5))
    print ("float of 3 = ",float(3))
    print ("3+3 = ",3+3)
    print ("float of 3+3 = ",float(3+3))
    print ("string of 3 + string of 3 = ",str(3)+str(3))
    print ("\"3\" , \"3\" = ","3","3")
    print ("\"3\" + \"3\" = ","3"+"3")

#example_210()  ###########################

def example_211():
    #Example 2.11
    a = 10
    print (a)
    a = a+10
    print (a)
    a+=10
    print (a)
    a-=5
    print (a)
    a*=2
    print (a)
    a/=5
    print (a)
    
#example_211()  ###########################


    

#example_200()
#example_201()
#example_202()
#example_203()
#example_204()
#example_205()
#example_206()
#example_207()
#example_208()
#example_209()
#example_210()
#example_211()

