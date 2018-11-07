#Example 7.12
#Python3.6.5

def example_712(*x):
    for i in x:
        print (i)
    print()
    print ("Number of Element in x=",len(x))
    print ("x=",x)
    try:
        print ("x[2]=",x[2])
    except:
        print ("x[0]=",x[0])
        
example_712(1,2,3,"Hello",[0,0,0])
print("----------")
example_712([5,2,'a'])

'''
ส่งค่าต้วแปรเข้าไปใน function แบบไม่จำกัดจำนวนค่า

แสดงผล
1
2
3
Hello
[0, 0, 0]

Number of Element in x= 5
x= (1, 2, 3, 'Hello', [0, 0, 0])
x[2]= 3
----------
[5, 2, 'a']

Number of Element in x= 1
x= ([5, 2, 'a'],)
x[0]= [5, 2, 'a'] 
'''
