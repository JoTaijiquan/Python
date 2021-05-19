#Python 3.9.5
#Example 2-6-4
'Modified Fibonacci number in lambda function'

if __name__ == "__main__":
    
    fibo4 = lambda n=0, o=[]: [o.append(i) or \
    i if i<=1 else o.append(o[-1]+o[-2]) or \
    o[-1] for i in range(n)]

    print ("fib() =",fibo4())
    print ("fib 0 =",fibo4(0))
    print ("fib 1 =",fibo4(1))
    print ("fib 2 =",fibo4(2))
    print ("fib 3 =",fibo4(3))
    print ("fib 10 =",fibo4(10))
    print ("fib 13 =",fibo4(13))
