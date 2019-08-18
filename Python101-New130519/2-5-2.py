#Python 3.7.3
#Example 2-5-2

def factorial(n):
    'หา factorial number ด้วย recusion'

    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    print ("3! =",factorial(3))
    print ("5! =",factorial(5))
    print ("1! =",factorial(1))
    print ("0! =",factorial(0))
    
