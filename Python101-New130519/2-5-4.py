#Python 3.7.3
#Example 2-5-4
'หา factorial number ด้วย lambda function'

if __name__ == "__main__":
    factorial4 = lambda n: 1 if n==0 else n*factorial4(n-1)

    print ("3! =",factorial4(3))
    print ("5! =",factorial4(5))
    print ("1! =",factorial4(1))
    print ("0! =",factorial4(0))
    