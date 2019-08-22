#Python 3.7.3
#Example 2-3-1

def sum_to_n(n):
    'หาผลบวกของ 1+2+3+...+n ด้วยคำสั่ง for loop'
    x=0
    n=n+1
    for i in range(1,n):
        x+=i
    return x

if __name__ == "__main__":
    print (sum_to_n.__doc__)
    print ("n=5 ผลบวก=",sum_to_n(5))
    print ("n=10 ผลบวก=",sum_to_n(10))
    print ("n=2 ผลบวก=",sum_to_n(2))
    print ("n=100 ผลบวก=",sum_to_n(100))
    