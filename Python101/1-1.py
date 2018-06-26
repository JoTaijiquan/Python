#Chapter 1

#Hello Python

'''
#Example 1.01 
print ("Hello World!")
'''

###########################

'''
#Example 1.02
#Python3.6
# -*- coding: utf-8 -*-

print ("Hello World!")
print ("สวัสดี ชาวโลก")
'''

###########################

'''
#Example 1.03
print (3+4); print (6-2)
print ("4x5 =",4*5); print ("4/2 =",4/2); print ("3/2 =",3/2)
print ("7/3 =",7/3);
print ("4 modulus 2 =",4%2);
print ("8 modulus 3 =",8%3)
print ("8 floor division 3 = ",8//3)
print ("2 power 3 = ",2**3)
print ("2x10 power 3 = ",2e3)
print ("Hello"+"!")
print ("Hello"*3)
print ("2-(2x3)) = ",2-(2*3))
'''

###########################

'''
#Example 1.04
print (1,2,3)
print (1,2,3,sep="")
print (1,2,3,sep="..")
print ("Hello","World","!",sep="__")
'''

###########################

'''
#Example 1.05
print ("\"Hello\"")
print ("\\Hello\\")
print ("Hello\n")
print ("World!")
print ("Hello\n\n\n")
print ("World!")
print ("Hello\tWorld!")
'''

###########################

'''
#Example 1.06
print ("Hello \
World!")
print ("3+\
5")
print (3\
+5)

'''

###########################


#Example 1.07
print ("Hello\nWorld!")
print ('''abc
def''')


###########################

'''
#Example 1.08 format string
print ("Hello {0}")
print ("Hello {0} World! {1}".format(3,10))
'''

###########################

'''
#Example 1.09 raw string
print (r"Hello World /n")
'''

###########################

'''
#Example 1.10 defind function with def
def example_110():
    print ("Hello")

example_110()
example_110()
example_110()
'''


#Example 1.11
def example_111():
    'Example 1.11 Document, Write any thing here!!'
    print ("Hello")

example_111()
print ("**************\n")
print (example_111)
print (example_111.__name__)
print (example_111.__doc__)


#Example 1.12
def example_112():
    '''Example 1.12 Document,
    Write any thing here!!
    in multi-line'''
    
    print ("Hello")

print (example_112)
print (example_112.__name__)
print (example_112.__doc__)
