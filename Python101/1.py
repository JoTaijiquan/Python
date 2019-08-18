


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





