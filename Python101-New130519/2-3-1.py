#Python 3.7.3
#Example 2-3-1

def sum_to_n(n):
    'หาผลบวกของ 1+2+3+...+n'
    x=0
    n=n+1
    for i in range(1,n):
        x+=i
    return x

def sum_to_n2(n):
    'หาผลบวกของ 1+2+3+...+n จากสูตร n*(n+1)/2'
    return n*(n+1)/2

if __name__ == "__main__":
    print ("หาผลบวกจาก loop")
    print ("n=5 ผลบวก=",sum_to_n(5))
    print ("n=10 ผลบวก=",sum_to_n(10))
    print("\nหาผลบวกจากสูตร n*(n+1)/2")
    print ("n=5 ผลบวก=",sum_to_n2(5))
    print ("n=10 ผลบวก=",sum_to_n2(10))
