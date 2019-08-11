#Python 3.7.3
#Example 2-1-1

def factorial(n):
    'หา factorial number'
    n = n+1
    fn=1
    for i in range(1,n):
        fn=fn*i
    return fn

if __name__ == "__main__":
    print ("3! =",factorial(3))
    print ("5! =",factorial(5))
    print ("1! =",factorial(1))
    print ("0! =",factorial(0))