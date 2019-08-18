#Python 3.7.3
#Example 2-8-2

def root(n,order=2):
    'หาค่ารากลำดับใดๆ ของ n'
    if n<1: return 0

    n0,n1,n2 = 1,n,0
    while abs(n2-n)>0.0001:
        n_mid = (n0+n1)/2
        n2 = n_mid**order
        if n2 < n:
            n0 = n_mid
        elif n2 > n:
            n1 = n_mid
        elif n2 ==n:
            return round(n_mid,3)
    return round(n_mid,3)

if __name__ == "__main__":
    print (root(-2))
    print (root(2))
    print (root(3))
    print (root(4))
    print (root(8,3))
    print (root(81,4))
    print (root(3,2.5))