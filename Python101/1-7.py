#Chapter 1.7

#Function


#Example 7.00
def example_700():
    print ("x inside function",x)

x=10
example_700()
print ("x outside function",x)

'''
#Error
def example_701():
    print (x)
    x=20

x=10
example_701()
print(x)
'''

'''
#Example 7.02
def example_702():
    x = 20
    print (x)
    x = x+10

x=10
print (x)
example_702()
print (x)
'''

