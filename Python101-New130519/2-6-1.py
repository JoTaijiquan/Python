#Python 3.9.5
#Example 2-6-1

def fibo1(n=2):
    'Fibonacci number'

    aList = [0,1]
    n0 = 0
    n1 = 1
    if n<3: return aList
        
    for i in range(2,n):
        n0,n1 = n1,n0+n1
        aList.append(n1)
    return aList

if __name__ == "__main__":
    print ("fib() =",fibo1())
    print ("fib 0=",fibo1(0))
    print ("fib 1=",fibo1(1))
    print ("fib 2=",fibo1(2))
    print ("fib 3=",fibo1(3))
    print ("fib 10=",fibo1(10))
    print ("fib 13=",fibo1(13))