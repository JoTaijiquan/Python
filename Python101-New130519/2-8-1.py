#Python 3.9.5
#Example 2-8-1

def square_root(n):
    'หาค่ารากที่สองของ n'
    n0 = 1
    n1 = n
    for i in range(100):
        n_mid = (n0+n1)/2
        n2 = n_mid*n_mid
        if n2 == n:
            return n_mid
        elif n2 < n:
            n0 = n_mid
        elif n2 > n:
            n1 = n_mid
    return n_mid

if __name__ == "__main__":
    print ("Square Root 2 =",square_root(2))
    print ("Square Root 4 =",square_root(4))
    print ("Square Root 5 =",square_root(5))
    
