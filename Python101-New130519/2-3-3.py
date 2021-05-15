#Python 3.9.5
#Example 2-3-3

def sum_to_n3(n):return n*(n+1)/2 
'หาผลบวกของ 1+2+3+...+n จากสูตร n*(n+1)/2 ในหนึ่งบรรทัด'

if __name__ == "__main__":
    print("หาผลบวก 1-n จากสูตร n*(n+1)/2 ในหนึ่งบรรทัด")
    print ("n=5 ผลบวก=",sum_to_n3(5))
    print ("n=10 ผลบวก=",sum_to_n3(10))
    print ("n=2 ผลบวก=",sum_to_n3(2))
    print ("n=100 ผลบวก=",sum_to_n3(100))
    print (sum_to_n3.__doc__)