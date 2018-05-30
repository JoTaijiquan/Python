#Python3.6
# -*- coding: utf-8 -*-

'''
# Example 1 
print ("Hello World!")
'''

'''
# Example 2
print (3+4)
'''

'''
# Example 3
a = 2
b = 999999988888877777
c = 3.14159265358
d = "ABC"
e = True

print (a,b,c,d,e)
a = b = c
print (a,b,c)
'''

'''
# Example 4
a = 2
b = "abc"

print (a,b)
b,a = a,b
print (a,b)
'''

'''
# Example 5
a = b = 2
c = d = 4
print (a,b,c,d)
'''

'''
#Example 6
a = 3+5
b = True
c = 999
d = "abc"
print (a,b,c,d)

a,b = c,d
print (a,b,c,d)
'''

'''
#Example 7
a,b,c = 1,3,5
print (a,b,c)
print ((a,b,c)*2)
print ((a,b,c)*3)
'''

'''
#Example 8

a = 9
b = 8
c = 7
d = 0.1


print (a+b, a-b, a*b, a/b, a%b, a**b)
print (3+4, 6-2, 4*3, 6/3, 11%8, 2**3)
print (3*4+2*3**2*(1+1))
print (True & False)
print (True | False)
print (not(True))
print (3==3)
print (3==4)
print (not(3==4))
print (type(a), type (d))
'''

'''
#Example 9

a = [1,2,3,4,5]
b = ["abc",2,3,False]
print (a)
print (b)
print (type(a))
print (a[1],b[0])
#print (a[5],b[-1]) #Error
a[0] = 7
print (a)
a[2]  = [3,4,5]
print (a)
print (a[2][1])

print ("**********")

a = (7,8,9)
print (a)
print (type(a))
print (a[1])
#a[1] = 99 #Error
print (a)


b[2] = (3,4,5,6)
print (b)
print (b[2][2])
print (type(b))
print (type(b[2]))
'''

'''
#Example 10
a = [1,2,3,4]
b = [1,2,3,4,3,5,4]
print (a)
a.append (5)
print (a)
a.insert (2,"xyz")
print (a)
print (a.index(5))
print (a.index(1))
print (b.count(3))
print (b.count(2))
print (b.count(6))
'''

'''
#Example 11
a = [1,2,3,4,5,6]
print (a)
a.remove(3)
print (a)

b = [2,3,6,1,4,8,1,5,3]
d =[8,7,3,2,3,5,4,2,2,1]
c=b
print (b)
print (c)
b.sort()
print (b)
b.reverse()
print(b)
print ("******")
print (c)
print ("******")
print (d)
d.reverse()
print (d)
'''

'''
#Example 12
print (5>4)
print (4>4)
print (4>=4)
print (5==4)
print (5!=4)
print (4==4)
'''

'''
#Example 13
print (4 is 4)
print (4 is (4,3))
print (4 in (4,3))
print ((3,4) in (2,3,4))
print ((3,4) in (2,(3,4),4))
print ((3,4) is (2,3,4))
print ("****")
print ((3,4) is (3,4))
print ((3,4) in (3,4))
'''

#Example 14

x = 10

if x is 10:
    print ("Yes")
else:
    print ("no")




       










