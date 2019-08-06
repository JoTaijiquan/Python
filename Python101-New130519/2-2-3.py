#Python 3.7.3
#Example 2-2-3

def fibo(n=0,fn=[],n0=0,n1=1):
    'Modified Fibonacci number in recursion'

    if len(fn)<n:
        fn.append(n0)
        n0,n1=n1,n0+n1
    else:
        return fn
    return fibo(n,fn,n0,n1)

if __name__ == "__main__":    
    print (fibo())
    print (fibo(0,fn=[]))
    print (fibo(1,fn=[]))
    print (fibo(2,fn=[]))
    print (fibo(3,fn=[]))
    print (fibo(10,fn=[]))
    print (fibo(13,fn=[]))
    