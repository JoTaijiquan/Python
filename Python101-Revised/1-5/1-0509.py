#Example 1.5.9
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_509():
    x = ['a','b','c','a']
    
    print ("1) x=",x)
    x.append(['d','e'])
    print ("2) append list, x=",x)
    x.remove('a')
    print ("3) remove 'a', x=",x)
    x.remove(['d','e'])
    print ("4) remove ['d','e'], x=",x)
    x.remove('a')
    print ("5) remove 'a', x=",x)

example_509()

'''
แสดงผล
1) x= ['a', 'b', 'c', 'a']
2) append list, x= ['a', 'b', 'c', 'a', ['d', 'e']]
3) remove 'a', x= ['b', 'c', 'a', ['d', 'e']]
4) remove ['d','e'], x= ['b', 'c', 'a']
5) remove 'a', x= ['b', 'c']
'''
