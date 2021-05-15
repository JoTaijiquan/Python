#Python 3.9.5
#Example 2-5-1

def factorial1(n):
    'หา factorial number'
    n = n+1
    ans=1
    for i in range(1,n):
        ans=ans*i
    return ans

if __name__ == "__main__":
    print ("3! =",factorial1(3))
    print ("5! =",factorial1(5))
    print ("1! =",factorial1(1))
    print ("0! =",factorial1(0))