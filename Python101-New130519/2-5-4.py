#Python 3.7.3
#Example 2-5-4
'หา factorial number ด้วย lambda function'

if __name__ == "__main__":
    factorial = lambda n: 1 if n==0 else n*factorial(n-1)

    print ("3! =",factorial(3))
    print ("5! =",factorial(5))
    print ("1! =",factorial(1))
    print ("0! =",factorial(0))
    