#Python3.6 
# -*- coding: utf-8 -*-


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

#Example 212

class p:
    def pr(self):
        print ("xxx")

x = p()
x.pr()


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
