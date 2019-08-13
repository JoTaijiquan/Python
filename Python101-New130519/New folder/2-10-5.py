#Python 3.7.3
#Example 2-10-1

def gcd(n1,n2):
    'หาค่าหารร่วมมากของเลขสองจำนวน'
    while n2!=0:
        n1,n2 = n2, n1%n2
    return n1

def lcm(n1,n2):
    'หาค่าคูณร่วมน้อย least common multiple หรือ ครน ของเลขสองจำนวน'
    return int(n1*n2/gcd(n1,n2))

if __name__ == "__main__":
    print (lcm(20,30))
    print (lcm(3,7))
    print(lcm(15,30))

