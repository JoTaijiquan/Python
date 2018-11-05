#Example 5.22
#Python3.6.5

def example_522():
    a = [1,2,3]
    b = [10,20,30]
    c = a+b
    print ("1)",c)
    print ("2)",a*2)

example_522()

'''
a = [1,2,3]
b = [10,20,30]
c = a+b         

print ("1)",c)      c= a+b นำ list a + list b = [1,2,3,10,20,30]
print ("2)",a*2)    a*2 = list a + list a = [1,2,3,1,2,3]
แสดงผล
1) [1, 2, 3, 10, 20, 30]
2) [1, 2, 3, 1, 2, 3]
'''
