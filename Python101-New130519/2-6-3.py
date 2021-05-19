#Python 3.9.5
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
    print ("fib() =",fibo3())
    print ("fib 0 =",fibo3(0,aList=[]))
    print ("fib 1 =",fibo3(1,aList=[]))
    print ("fib 2 =",fibo3(2,aList=[]))
    print ("fib 3 =",fibo3(3,aList=[]))
    print ("fib 10 =",fibo3(10,aList=[]))
    print ("fib 13 =",fibo3(13,aList=[]))
    print ("fib 15 =",fibo3(15,aList=[]))
