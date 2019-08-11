#Python 3.7.3
#Example 2-2-2

def fibo(n):
    'Fibonacci number in recursion'
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

def fibo_list(n):
    fn=[]
    for i in range(n):
        fn.append(fibo(i))
    return fn

if __name__ == "__main__": 
    print(fibo_list(0))
    print(fibo_list(1))
    print(fibo_list(2))
    print(fibo_list(3))
    print(fibo_list(10))
    print(fibo_list(13))
    
    

    