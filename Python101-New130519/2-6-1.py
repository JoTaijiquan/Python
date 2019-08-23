#Python 3.7.3
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
    print (fibo1())
    print (fibo1(0))
    print (fibo1(1))
    print (fibo1(2))
    print (fibo1(3))
    print (fibo1(10))
    print (fibo1(13))