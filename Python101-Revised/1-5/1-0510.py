#Example 5.10
#Python3.6.5

def example_510():
    x = ['a','b','c',[3,4,5],'a','b','c']
    
    print ("1) x=",x)
    del x[3]; print ("2) del x[3]=",x)
    del x[2]; print ("3) del x[2]=",x)

example_510()

'''
แสดงผล
1) x= ['a', 'b', 'c', [3, 4, 5], 'a', 'b', 'c']
2) del x[3]= ['a', 'b', 'c', 'a', 'b', 'c']
3) del x[2]= ['a', 'b', 'a', 'b', 'c']
'''
