#Python 3.7.3
#Example 2-6-4
'Modified Fibonacci number in lambda function'

if __name__ == "__main__":
    #fibo = lambda n=10, fibo=[0,1]: fibo[:n]+[fibo.append(fibo[-1]+fibo[-2]) or fibo[-1] for i in range(n-len(fibo))]    
    
    fibo = lambda n=10, o=[]: [o.append(i) or i if i<=1 else o.append(o[-1]+o[-2]) or o[-1] for i in range(n)]

    print(fibo())
    print (fibo(0))
    print (fibo(1))
    print (fibo(2))
    print (fibo(3))
    print (fibo(10))
    print (fibo(13))
