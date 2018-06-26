#Chapter 2

#Know the variable.

#Example 201
def example_201():  
    a = 2
    b = 999999988888877777
    c = 3.14159
    d = "ABC"
    e = True

    print ("1) a=",a)
    print ("2) b=",b)
    print ("2) c=",c)
    print ("4) d=",d,"e=",e)

    a = b = c
    print ("5)",a,b,c)

#example_201()
###########################

#Example 2.02
def example_202():
    a = 2
    b = "abc"
    print ("1)",a,b)
    b,a = a,b
    print ("2)",a,b)

#example_202()
###########################

#Example 2.03
def example_203():
    a = b = 2
    c = d = 4
    print ("1) a,b,c,d =",a,b,c,d)

#example_203()
###########################

#Example 2.04
def example_204():
    a = 3+5
    b = True
    c = 999
    d = "ddd"
    e = "eee"
    f = "fff"

    print ("1) a b c =",a,b,c)

    a,b,c = b,c,a
    print ("2) a b c =",a,b,c,)

    a,b,c = d,e,f
    print ("3) a b c = ",a,b,c)

#example_204()
###########################

#Example 2.05
def example_205(): 
    Hello = 0
    print ("1)",Hello)

    Hello = "Hello"
    print ("2)",Hello)

    print ('3) Hello')
    print ("4) Hello")
    print ("5) \"Hello\"")
    print ("6) \'Hello\'")
    print ("7) 'Hello'")
    print ('8) "Hello"')
    print ("9) \\Hello\\")
    print ("10) Hello\tHello")

#example_205()
###########################

#Example 2.06
def example_206():
    a,b,c = 1,3,5
    print ("1) ",a,b,c)
    print ("2) ",(a,b,c)*2)
    print ("3) ",(a,b,c)*3)

#example_206()
###########################

#Example 2.07
def example_207():
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

    print ("1) a=",a,type(a))
    print ("2) b=",b,type(b))
    print ("3) c=",c,type(c))
    print ("4) d=",d,type(d))
    print ("5) e=",e,type(e))
    print ("6) f=",f,type(f))
    print ("7) g=",g,type(g))
    print ("8) h=",h,type(h))
    print ("9) i=",i,type(i))
    print ("10) j=",j,type(j))

#example_207()
###########################

#Example 2.08
def example_208():
    a,b = 9,8
    print ("1) a+b =",a+b)
    print ("2) a-b =",a-b)
    print ("3) axb =",a*b)
    print ("4) a/b =",a/b)
    print ("5) a//b =",a//b) #หารเอาส่วน
    print ("6) a mod b =",a%b) #หารเอาเศษ
    print ("7) a power b =",a**b) #ยกกำลัง
    print ("8) 3*4+2*3**2*(1+1) =",3*4+2*3**2*(1+1))

#example_208()
###########################

#Example 2.09
def example_209():
    print ("1) True and False is",True & False)
    print ("2) True or False is",True | False)
    print ("3) Not True is",not(True))
    print ("4) 3 == 3 is",3==3)
    print ("5) 3 == 4 is",3==4)
    print ("6) not (3==4) is",not(3==4))
    print ("7) 5>4 is",5>4)
    print ("8) 4>4 is",4>4)
    print ("9) 4>=4 is",4>=4)
    print ("10) 5==4 is",5==4)
    print ("11) 5!=5 is",5!=4)
    print ("12) 4==4 is",4==4)    

#example_209()
###########################

#Example 2.10
def example_210():
    print ("1) 3x10 power 5 =",3e5)
    print ("2) type of 3e5 =",type(3e5))
    print ("3) 3x10 power 5 =",3*10**5)
    print ("4) type of 3*10**5 =",type(3*10**5))
    print ("5) 3.12345 * 10 power 5 =",3.12345e5)
    print ("6) type of 3.12345e5 =",type(3.12345e5))
    print ("7) 3.12345 * 10 power 5 =",3.12345*10**5)
    print ("8) type of 3.12345 * 10**5 =",type(3.12345*10**5))

example_210()
###########################

#Example 2.11
def example_211():
    print ("1) interger of 3.5 =",int(3.5))
    print ("2) float of 3 =",float(3))
    print ("3) 3+3 =",3+3)
    print ("4) float of 3+3 =",float(3+3))
    print ("5) string of 3 + string of 3 =",str(3)+str(3))
    print ("6) \"3\" , \"3\" =","3","3")
    print ("7) \"3\" + \"3\" =","3"+"3")

#example_211()
###########################

#Example 2.12
def example_212():
    a = 10;     print ("1) ",a)
    a = a+10;   print ("2) ",a)
    a+=10;      print ("3) ",a)
    a-=5;       print ("4) ",a)
    a*=2;       print ("5) ",a)
    a/=5;       print ("6) ",a)
    
#example_212()
###########################

#Example 2.13
def example_213():
    a = """Hello
World!"""
    b = "Hello!\nWorld."
    c = "Hello \
World"
    d \
      =5
    e= \
       6
    print ("1) ",a)
    print ("2) ",b)
    print ("3) ",c)
    print ("4) ",d)
    print ("5) ",e)

#example_213()    
###########################

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
#example_212()
#example_213()
