'''
#Example 2
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
'''
###########################

'''
#Example 2.01
a = 2
b = "abc"
print (a,b)
b,a = a,b
print (a,b)
'''

###########################

'''
#Example 2.02
a = b = 2
c = d = 4
print (a,b,c,d)
'''

###########################

'''
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
'''

###########################

'''
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
'''

###########################

'''
#Example 2.05
a,b,c = 1,3,5
print (a,b,c)
print ((a,b,c)*2)
print ((a,b,c)*3)
'''

###########################

'''
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
'''

###########################

'''
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
'''

###########################

'''
#Example 2.08
print ("True and False = ",True & False)
print ("True or False = ",True | False)
print ("Not True = ", not(True))
print ("3 = 3 ? ",3==3)
print ("3 = 4 ? ",3==4)
print ("not (3=4?)",not(3==4))
print ("-------")
'''

###########################

'''
#Example 2.09
print ("3x10 power 5 = ",3e5)
print ("type of 3e5 = ",type(3e5),"\n")

print ("3x10 power 5 = ",3*10**5)
print ("type of 3*10**5 = ",type(3*10**5),"\n")

print ("3.12345 * 10 power 5 = ",3.12345e5)
print ("type of 3.12345e5 = ",type(3.12345e5),"\n")

print ("3.12345 * 10 power 5 = ",3.12345*10**5)
print ("type of 3.12345 * 10**5 = ",type(3.12345*10**5),"\n")
'''

#Example 2.10

print ("3//2 = ",3//2)
print ("3/2 = ",3/2)
print ("7//4 = ",11//4)
print ("7/4 = ",11/4)
print ("7%4 = ",11%4)

print ("interger of 3.5 = ",int(3.5))
print ("float of 3 = ",float(3))
print ("3+3 = ",3+3)
print ("float of 3+3 = ",float(3+3))
print ("string of 3 + string of 3 = ",str(3)+str(3))
print ("\"3\" , \"3\" = ","3","3")
print ("\"3\" = \"3\"","3"+"3")

#print ('*',repr("Hello").rjust(4),'*')
