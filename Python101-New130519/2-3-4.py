#Python 3.7.3
#Example 2-3-4
'ใช้ lambda function หาผลบวกของ 1+2+3+...+n'

if __name__ == "__main__":
    sum_to_n4=lambda n:n*(n+1)/2
    
    print (__doc__)
    print ("n=5 ผลบวก=",sum_to_n4(5))
    print ("n=10 ผลบวก=",sum_to_n4(10))
    print ("n=2 ผลบวก=",sum_to_n4(2))
    print ("n=100 ผลบวก=",sum_to_n4(100))
    print (type(sum_to_n4))
    