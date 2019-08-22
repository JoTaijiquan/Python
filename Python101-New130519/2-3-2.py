#Python 3.7.3
#Example 2-3-2

def sum_to_n2(n):
    'หาผลบวกของ 1+2+3+...+n จากสูตร n*(n+1)/2'
    return n*(n+1)/2

if __name__ == "__main__":
    print (sum_to_n2.__doc__)
    print ("n=5 ผลบวก=",sum_to_n2(5))
    print ("n=10 ผลบวก=",sum_to_n2(10))
    print ("n=2 ผลบวก=",sum_to_n2(2))
    print ("n=100 ผลบวก=",sum_to_n2(100))
    