#Python 3.7.3
#Example 2-6-4
'Modified Fibonacci number in lambda function'

if __name__ == "__main__":
    
    fibo4 = lambda n=0, o=[]: [o.append(i) or \
    i if i<=1 else o.append(o[-1]+o[-2]) or \
    o[-1] for i in range(n)]

    print (fibo4())
    print (fibo4(0))
    print (fibo4(1))
    print (fibo4(2))
    print (fibo4(3))
    print (fibo4(10))
    print (fibo4(13))
