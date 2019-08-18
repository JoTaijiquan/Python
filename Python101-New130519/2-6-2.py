#Python 3.7.3
#Example 2-6-2
'Fibonacci number in recursion'

def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

def fibo_list(n=2):
    aList=[]
    for i in range(n):
        aList.append(fibo(i))
    return aList

if __name__ == "__main__": 
    print(fibo_list(0))
    print(fibo_list(1))
    print(fibo_list(2))
    print(fibo_list(3))
    print(fibo_list(10))
    print(fibo_list(13))
    
    

    