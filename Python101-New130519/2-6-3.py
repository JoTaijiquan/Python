#Python 3.7.3
#Example 2-6-3

def fibo3(n=0,aList=[],n0=0,n1=1):
    'Modified Fibonacci number in recursion'

    if len(aList)<n:
        aList.append(n0)
        n0,n1=n1,n0+n1
    else:
        return aList
    return fibo3(n,aList,n0,n1)

if __name__ == "__main__":    
    print (fibo3())
    print (fibo3(0,aList=[]))
    print (fibo3(1,aList=[]))
    print (fibo3(2,aList=[]))
    print (fibo3(3,aList=[]))
    print (fibo3(10,aList=[]))
    print (fibo3(13,aList=[]))
    print (fibo3(15,aList=[]))
