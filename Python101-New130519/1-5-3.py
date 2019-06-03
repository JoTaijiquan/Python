#Python 3.7.3
#Example 1-5-3

def func_1_5_3():
    'list a[start:end] not include end'
    
    a = [9,2,5,3,8,7]
    print ('a =',a)
    a[0] = 7
    a[2] =['a','Hello',9+2]
    print ('a =',a)
    a[1:4] = 1,3
    print ('a =',a)

if __name__ == "__main__":
    func_1_5_3()
