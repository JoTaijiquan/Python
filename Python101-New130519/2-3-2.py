#Python 3.7.3
#Example 2-3-2
'หาผลบวกของ 1+2+3+...+n จากสูตร n*(n+1)/2'

def sum_to_n3(n):return n*(n+1)/2 
'เขียนฟังก์ชันในหนึ่งบรรทัด'

if __name__ == "__main__":
    print ("เขียนฟังก์ชันให้เหลือบรรทัดเดียว sum 1-10 =",sum_to_n3(10))

    x=lambda n:n*(n+1)/2
    print ("ใช้ lambda function sum 1-10 =",x(10))
    print (__doc__)
    print (sum_to_n3.__doc__)
    