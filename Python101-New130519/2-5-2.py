#Python 3.9.5
#Example 2-5-2

def factorial2(n):
    'หา factorial number ด้วย recursion'
    if n==1 or n==0:
        return 1
    else:
        return n*factorial2(n-1)

if __name__ == "__main__":
    print ("3! =",factorial2(3))
    print ("5! =",factorial2(5))
    print ("1! =",factorial2(1))
    print ("0! =",factorial2(0))