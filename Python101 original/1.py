


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





