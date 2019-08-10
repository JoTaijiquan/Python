#Python 3.7.3
#Example 2-1-2

def factorial_recursion(n):
    'หา factorial number ด้วย recusion ตั้งแต่ 1-n'

    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1)

if __name__ == "__main__":
    print ("3! =",factorial_recursion(3))
    print ("5! =",factorial_recursion(5))
    print ("1! =",factorial_recursion(1))
