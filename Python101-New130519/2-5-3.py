#Python 3.7.3
#Example 2-5-3

def factorial(n):
    'หา factorial number โดยนับถอยหลัง'
    ans=1
    while n!=0:
        ans*=n
        n-=1
    return ans

if __name__ == "__main__":
    print ("3! =",factorial(3))
    print ("5! =",factorial(5))
    print ("1! =",factorial(1))
    print ("0! =",factorial(0))