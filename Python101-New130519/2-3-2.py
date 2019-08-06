#Python 3.7.3
#Example 2-3-1

'Not complete yet*****************'

def prime(n):
    num = list(range(2,n))
    for i in num:
        if i%2==0:
            num.remove(i)
    return num
if __name__ == "__main__":
    print (prime(97))