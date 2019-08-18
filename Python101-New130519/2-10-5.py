#Python 3.7.3
#Example 2-10-1

def gcd(n1,n2):
    'หารร่วมมาก(หรม.) สองจำนวน'
    while n2!=0:
        n1,n2 = n2, n1%n2
    return n1

def lcm(n1,n2):
    'คูณร่วมน้อย(ครม.) least common multiple (lcm) สองจำนวน'
    return int(n1*n2/gcd(n1,n2))

if __name__ == "__main__":
    print (lcm(20,30))
    print (lcm(3,7))
    print(lcm(15,30))

