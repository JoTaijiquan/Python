


'''
#Example 1.3
import random
a = [1,2,3,4,5,6,7]
b = (1,3,5,7,9,11,13)
random.shuffle(a)
print (a)
random.shuffle(a)
print (a)
random.shuffle(a)
print (a)

#random.shuffle(b) error cannot shuffle tuple
#print (b)
'''

'''
#Example 1.4
import random
a = [1,2,3,4,5,6,7,8]
print (a)
b = random.choices(a)
print (b)
b = random.choices(a)
print (b)
b = random.choices(a,k=3)
print (b)
b = random.choices(a,k=4)
print (b)
'''





'''
#Example 11

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
#Example 11.1
i = [1,2,3,4,5,6,7,8,9,10]
print (i[2:5])
print (i[2:9:2])
print (i[:5])
print (i[::2])
print (i[::-1])
print (i[::-2])
print (i[-8:-1])
print (i[-8:-1:2])
print (i[-8:-1:-2])
print (i[-1:-8])
'''

'''
#Example 11.2
x = [1,2,3,4,5]
x.append(6)
x.extend([7,8,9])
print (x)
x.insert(2,'a')
print (x)
x.insert(2,['x','y','z'])
print (x)
'''

'''
#Example 11.3
x = ['a','b','c','a']
x.append(['d','e'])
print (x)
x.remove('a')
print (x)
x.remove(['d','e'])
print (x)
x.remove ('a')
print (x)
x = ['a','b','c',[3,4,5],'a','b','c']
print (x)
del x[3]
print (x)
del x[2]
print (x)
print ("********")
x = ['a','b','c',[3,4,5],'a','b','c']
print (x)
print (x.pop(2))
print (x)
print (x.pop())
print (x)
print (x.pop())
print (x)
'''

'''
#Example 11.4
x = [1,2,3,4,5]
y = x
z = x[:]
print (x)
print (y)
print (z)
x.append (6)
print (x)
print (y)
print (z)
print ("*********")
x = ['a','x','a','c,','z','a']
print (x)
print (y)
print (z)
y = [5,6,8,1,2,8,8,4,1,2]
print (x)
print (y)
print (z)
print ("***********")
x = ['a','x','a','c,','z','a']
y = x
print (x)
print (y)
x = sorted(x)
print (x)
print (y)
print ("************")
x = ['a','x','a','c,','z','a']
y = x
x.sort()
print (x)
print (y)
print ("************")
x = ['a','x','a','c,','z','a']
y = x
y.sort()
print (x)
print (y)
'''

'''
#Example 11.5
a = [11,12,13,14,21,22,23,24,31,32,33,34]
print (a[2:2])
'a = [11,12,['xx','yy','zz'],14,21,22,23,24,31,32,33,34]'
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


'''
#Example 14.1

x = input ("Input Number ")

x = int(x)
if x==10:
    print (x)
else:
    print ("ho ho ho")
'''           
'''
#Example 14.2
x = input ("Input X ")
y = input ("Input Y ")

if x == "10" and y == "10":
    print (x,"and",y)
elif x == "10" or y == "10":
    print (x,"or",y)
elif x !="10" and y !="10":
    print ("not",x,y)
'''    


'''
#Example 16


print ("*******")

for i in (1,2,3,5,8):
    print (i)

print ("*******")

for i in ("abc",True,2,(3,4),"def"):
    print (i)
print ("*******")

for i in (1,3,5,7,8,9,10):
    print (i)
    if i==5:
        break
    else:
        pass
print ("end at",i)
print ("*******")



'''
#Example 16.1
x = [1,3,5,7,9]
for i in x:
    print (i)
    if i==5:
        x.append(10)
print (x)
'''    

'''
#Example 16.2

for i in "Hello World!":
    print (i)
print ("*******")
for i in str(3.14159):
    print (i)
print ("*******")
for i in ["Superman", "Batman","Wonderwoman"]:
    print ("Hello ",i)
    print ("Hello "+i)
'''

'''
#Example 16.3
for i in range(10):
    if i == 5:
        pass
    else:
        print (i)
print ("*******")
for i in range(10):
    if i==4:
        continue
    else:
        print (i)
'''

'''
#Example 16.4
for i in range(10):
    if i==5:
        break
    else:
        print(i)
'''



'''
#example 17

#x=[3,4,5]
#print (x[6])
    
x = [3,4,5]
try:
    print (x[6])
except:
    print ("Error x is out of range")
'''    

'''
#Example 18
name = input("What is your name? ")
print ("Hello "+name+"!")
'''

'''
#Example 18.5
number = input("Number? ")
print (number)
print (number*3)
print (type(number))
number = float(number)
print (number*3)
print (type(number))
'''

'''
#Example 19
f = open("test.html","w")
f.write ("abcde abcde abcde")
f.write ("def def def\n")
f.write ("abc abc abc\n")
print ("Hello",file=f) 
print ("There",file=f)
f.close()
'''
'''
#Example 20
f= open("test.html","a")
f.write ("well well well\n")
f.close()
'''

'''
#Example 21
f = open("test.html","r")

a = f.readline()
print (a)
print (f.readline())
print ("*******")
print (f.readlines())
print ("******")
f.seek (0)
print (f.readlines())
print ("***************")
f.seek(2)
print (f.readlines())
f.close()
'''
''''
#Example 22

f = open("test.html","r+")
print (f.readline())
f.write ("xxxxxxxxxx\n")
print (f.readline())
f.seek(0)
print (f.readlines())
f.close()
#r read, r+ read/write, w write, a append, rb binary read, wb binary write, ab bianry append
'''
'''
#Example 23
f = open("test.html","r")
print (f.read(10))
print ("*********")
print (f.read())
'''

'''
#Example 24
f = open("test.html", "r+")
f.seek(0,2) #start end  (0 begining, 1 current, 2 end)
f.writelines("test")
f.writelines("Hello")
f.close()
'''

'''
#Example 25
f = open("test2.html",mode="w+",encoding="utf-8") 
f.write("สวัสดี\n")
f.write("Hello\n")
f.seek(0)
print(f.read())
f.close()
'''

'''
#Example 26
def f1 ():
    print ("ha ha ha")

def f2 ():
    print ("ho ho ho")
    return("hu hu")

f1()
f2()
print ("*******")

a = f1()
b = f2()
print (a,b)
'''
'''
#Example 27
def add(x,y):
    return (x+y)
print (add(10,20))
print ("*********")
a = 10
b = 11
print (a,b,add(a,b))
'''

'''
#Example 28
def double_add(x,y):
    x = x*2
    y= y*2
    return(x+y)
print (double_add(10,20))
a = 10
b = 20
print (double_add(a,b))
print (a,b)
'''

'''
#Example 29
def multi_return():
    x = 11
    return 10,20,30,x

print (multi_return())
a,b,c,d = multi_return()
print ("a=",a,"b=",b,"c=",c,"d=",d)
'''

'''
#Example 30
def multi_return2():
    return (10,20),("a","b",(1,2,3)),True

x = multi_return2()
print (x)

a,b,c = multi_return2()
print (a,b,c)
print (b[1])
print (b[2][2])
'''

#Example 31



