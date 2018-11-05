#Example 5.08
#Python3.6.5

def example_508():
    a = [1,2,3,4,5,6]
    print ("1) a= ",a)
    a.remove (3)
    print ("2) remove 3 from a",a)
    a = [1,2,3,4,5,6,3,4,3]
    print ("3) assign new a = ",a)
    a.remove(3)
    print ("4) remove 3 from a",a)
    a.remove(3)
    print ("5) remove 3 from a",a)
    
example_508()

'''
แสดงผล
1) a=  [1, 2, 3, 4, 5, 6]
2) remove 3 from a [1, 2, 4, 5, 6]
3) assign new a =  [1, 2, 3, 4, 5, 6, 3, 4, 3]
4) remove 3 from a [1, 2, 4, 5, 6, 3, 4, 3]
5) remove 3 from a [1, 2, 4, 5, 6, 4, 3]
'''
