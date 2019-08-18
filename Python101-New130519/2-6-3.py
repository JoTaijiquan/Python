#Python 3.7.3
#Example 2-6-3

def fibo(n=0,aList=[],n0=0,n1=1):
    'Modified Fibonacci number in recursion'

    if len(aList)<n:
        aList.append(n0)
        n0,n1=n1,n0+n1
    else:
        return aList
    return fibo(n,aList,n0,n1)

if __name__ == "__main__":    
    print (fibo())
    print (fibo(0,aList=[]))
    print (fibo(1,aList=[]))
    print (fibo(2,aList=[]))
    print (fibo(3,aList=[]))
    print (fibo(10,aList=[]))
    print (fibo(13,aList=[]))
    print (fibo(15,aList=[]))
