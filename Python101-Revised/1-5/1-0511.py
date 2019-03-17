#Example 1.5.11
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_511():
    x = ['a','b','c',[3,4,5],'a','b','c']
    
    print ("1) x=",x)
    print ("2) pop(2) = ",x.pop(2))
    print ("3) x=",x)
    print ("4) pop(1) = ",x.pop(1))
    print ("5) x=",x)
    print ("6) pop() = ",x.pop())
    print ("7) x=",x)
    print ("8) pop() = ",x.pop())
    print ("9) x=",x)

example_511()

'''
pop() ดึงค่าออกมาจาก list ค่าที่ถูก pop มาก็จะหายออกไปจาก list เลย

แสดงผล
1) x= ['a', 'b', 'c', [3, 4, 5], 'a', 'b', 'c']
2) pop(2) =  c
3) x= ['a', 'b', [3, 4, 5], 'a', 'b', 'c']
4) pop(1) =  b
5) x= ['a', [3, 4, 5], 'a', 'b', 'c']
6) pop() =  c
7) x= ['a', [3, 4, 5], 'a', 'b']
8) pop() =  b
9) x= ['a', [3, 4, 5], 'a']
'''
