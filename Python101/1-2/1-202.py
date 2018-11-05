#Example 2.02
#Python3.6.5

def example_202():
    a = 2
    b = "abc"
    print ("1)",a,b)
    b,a = a,b
    print ("2)",a,b)

example_202()

'''
a = 2               กำหนดค่า a = 2
b = "abc"           กำหนดค่า b = "abc"
print ("1)",a,b)    แสดงผล 1) 2 abc
b,a = a,b           สลับค่า a กับ b
print ("2)",a,b)    แสดงผล 2) abc 2
'''
