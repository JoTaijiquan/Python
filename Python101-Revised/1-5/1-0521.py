#Example 1.5.21
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_521():
    a = [2,3,4]
    b = (9,10,11)
    c = (4,5,6,[1,2,3],8,(9,10),15)
    d = [a,b,c]
    e = (a,b,c)
    f = a,b,c
    g = 2,3,8,10,"a","b"
    
    print ("1) a=",a,"type=",type(a))
    print ("2) b=",b,"type=",type(b))
    print ("3) a[1]=",a[1],type(a[1]))
    print ("4) c[1]=",c[1],type(c[1]))
    print ("5) c[3]=",c[3],type(c[3]))
    print ("6) c[5]=",c[5],type(c[5]))
    print ("7) c[3][1]=",c[3][1],type(c[3][1]))
    print ("8) d=[a,b,c] =",d)
    print ("9) e=(a,b,c) =",e)
    print ("10) f=a,b,c =",f)
    print ("11) g=",g,"type=",type(g))

example_521()

'''
list และ tuple

แสดงผล
1) a= [2, 3, 4] type= <class 'list'>
2) b= (9, 10, 11) type= <class 'tuple'>
3) a[1]= 3 <class 'int'>
4) c[1]= 5 <class 'int'>
5) c[3]= [1, 2, 3] <class 'list'>
6) c[5]= (9, 10) <class 'tuple'>
7) c[3][1]= 2 <class 'int'>
8) d=[a,b,c] = [[2, 3, 4], (9, 10, 11), (4, 5, 6, [1, 2, 3], 8, (9, 10), 15)]
9) e=(a,b,c) = ([2, 3, 4], (9, 10, 11), (4, 5, 6, [1, 2, 3], 8, (9, 10), 15))
10) f=a,b,c = ([2, 3, 4], (9, 10, 11), (4, 5, 6, [1, 2, 3], 8, (9, 10), 15))
11) g= (2, 3, 8, 10, 'a', 'b') type= <class 'tuple'>
'''
