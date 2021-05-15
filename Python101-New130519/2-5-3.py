#Python 3.9.5
#Example 2-5-3

def factorial3(n):
    'หา factorial number โดยนับถอยหลัง'
    ans=1
    while n!=0:
        ans*=n
        n-=1
    return ans

if __name__ == "__main__":
    print ("3! =",factorial3(3))
    print ("5! =",factorial3(5))
    print ("1! =",factorial3(1))
    print ("0! =",factorial3(0))