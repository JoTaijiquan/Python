#Python 3.7.3
#Example 2-2-1

def fibo(n=2):
    'Fibonacci number'

    fn = [0,1]
    n0 = 0
    n1 = 1
    if n<3: return(fn)
        
    for i in range(2,n):
        #n0,n1 = n1,n0+n1
        fn.append(n1)
        n0+=1
        n1+=1
    return (fn)

if __name__ == "__main__":
    print (fibo())
    print (fibo(0))
    print (fibo(1))
    print (fibo(2))
    print (fibo(3))
    print (fibo(10))
    print (fibo(13))