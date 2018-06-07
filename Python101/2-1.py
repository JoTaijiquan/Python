#Python3.6 
# -*- coding: utf-8 -*-

a="1234567"
b=1234567

c="1234567"
d="1234567"

e=a<<2

print (e)
print ("******")



'''
#Example 211

class p:
    def pr(self):
        print ("yyy")

x = p()
x.pr()
'''

'''
#Example 212

class p:
    def __init__(self):
        print ("xxx")

x = p()
'''

'''
#Example 213
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
x = p()
x.pr()
print (x)
print ("******")
print (x.pr())
'''

'''
#Example 214
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
    def __str__(self):
        return("Class p")

x = p()
x.pr()
print (x)
print ("******")
print (x.pr())
'''

'''
#Example 215
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
    def __str__(self):
        return("Class p")
    def __del__(self):
        print ("Class p Deleted")

x = p()
x.pr()
print (x)
print ("******")
del x
#print (x) #Error
'''

'''
#Example 216
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
    def __str__(self):
        return("Class p")
    def __del__(self):
        print ("Class p Deleted")
x=p()
y = x
x.pr()
y.pr()
print ("*******")
print (x)
print (y)
print ("Try del x")
del x

print (y)
print ("Try del y")
del y
'''

'''
#Example 217
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
    def __str__(self):
        return ("Class p")
    def __del__(self):
        print ("Class p Deleted")

x=p()
y=p()
del x
print ("*******")
del y
'''
'''
#Example 218
class p:
    def __init__(self,x):
        print ("Start!!",x)
    def pr(self,x):
        print ("pr!!",x)
    def __str__(self):
        return ("Class p")
    def __del__(self):
        print ("Class p Delete,")
x=p(10)
x.pr(11)
print (x)
x.pr(12)
'''

'''
#Example 219
class p:
    z=0
    def __init__(self,x):
        print ("Start!!",x)
        z=x
    def pr(self):
        print ("pr!!",self.z)
    def __str__(self):
        return ("Class p")
    def __del__(self):
        print ("Class p Delete,")
x=p(10)
x.pr()
print (x.z)
print (x)
'''

'''
#Example 220
class p:
    z=0
    def __init__(self,x):
        print ("Start!!",x)
        self.z = x
    def pr(self):
        print ("pr!!",self.z)
    def __str__(self):
        return ("Class p")
    def __del__(self):
        print ("Class p Delete,")
x=p(10)
x.pr()
print (x.z)
print (x)
'''

'''
#Example 221
class p:
    z=0
    def __init__(self,x):
        print ("Start!!",x)
        self.z = x
    def change_z (self,x):
        self.z = x
    def __str__(self):
        return ("Class p, z="+str(self.z))
    def __del__(self):
        print ("Class p Delete, z="+str(self.z))
x=p(10)
print (x)
x.change_z(11)
print (x)
y=x
y.change_z(12)
print (x)
x.change_z(13)
print (y)
print ("*****")
del x
print (y)
del y
'''

'''
#Example 222
class p:
    z=0
    def __init__(self,x):
        print ("Start!!",x)
        self.z = x
    def change_z (self,x):
        self.z = x
    def __str__(self):
        return ("Class p, z="+str(self.z))
    def __del__(self):
        print ("Class p Delete, z="+str(self.z))
x=p(10)
y=p(11)
print (x)
print (y)
x.change_z(15)
print (x)
print (y)

print ("*******")
del x
del y
'''

'''
# this is our descriptor object
class Bar(object):
    def __init__(self):
        self.value = ''
    def __get__(self, instance, owner):
        print "returned from descriptor object"
        return self.value
    def __set__(self, instance, value):
        print "set in descriptor object"
        self.value = value
    def __delete__(self, instance):
        print "deleted in descriptor object"
        del self.value

class Foo(object):
    bar = Bar()

f = Foo()
f.bar = 10
print f.bar
del f.bar

set in descriptor object
returned from descriptor object
10
deleted in descriptor object
'''

#Example 223
class Rectangle:
    def area(self):
        return (self.l * self.w)
r = Rectangle()
r.l=5
r.w=6
print (r.l,r.w,r.area())
r.l=10
print (r.l,r.w,r.area())

'''
#Example 215
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
x = p()
y = x
x.pr()
y.pr()
print ("******")
print (x)
print (y)
'''

'''
#Example 216
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
    def __str__(self):
        return("Class p")
x = p()
y = x
x.pr()
y.pr()
print ("*******")
print (x)
print (y)
print ("******")
del x
#print (x) #error
print (y)
y.pr()
'''

'''
#Example 217
class p:
    def __init__(self):
        print ("xxx")
    def pr(self):
        print ("yyy")
    def __str__(self):
        return("Class p")
x = p()
y = x
x.pr()
y.pr()
print ("*******")
print (x)
print (y)
print ("******")
x = None
print (x) 
print (y)
y.pr()
'''


'''
#Example 21
class Fighter:
    Model = ""
    Pilot = ""
    Bot = ""
    def __init__(self):
        pass


s1 = Fighter()
s2 = Fighter()

s1.Model = "Millenium Falcon"
s1.Pilot = "Han Solo"
s1.Bot = "C3PO"

s2.Model = "X-Wing"
s2.Pilot = "Luke Skywalker"
s2.Bot = "R2D2"

print (s1.Model)
print (s1.Pilot)
print (s1.Bot)

print (s2.Model)
print (s2.Pilot)
print (s2.Bot)
'''

'''
#Example 211
class p:
    x = 10

    def __init__(self):
        self.a = "abc"
        self.b = ""
        self.c = ""
        
    def pr(self):
        self.x= 11
        self.a = "xyz"
        
x  = p()
print (x.a)
print (x.b)
x.pr()
print (x.a)

#print (x.x)
#x.pr

print (x.x)

'''


'''
#Example 22
class Fighter:
    Model = ""
    Pilot = ""
    Bot = ""
    
    def __init__(self,iModel="X-Wing",iPilot="Luke",iBot="R2D2"):
        self.Model = iModel
        self.Pilot = iPilot
        self.Bot = iBot

    def __str__(self):
        msg = "Hello I am a Fighter!!!"
        return (msg)
    
    def ShowFighter():
        print ("xx")
        print (Model+"1")
        print (Pilot)
        print (Bot)

    def x():
        print ("test")

s1 = Fighter()
print (s1)
s1.ShowFighter()
#s1.ShowFighter
s1.x
#print (s1.Model)
#print (s1.Pilot)

s2 = Fighter("A-Wing","Han","C3PO")
s2.x
#print (s2.Model)
#print (s2.Pilot)
'''
