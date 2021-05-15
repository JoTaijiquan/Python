#Python 3.9.5
#Example 2-8-2

def root(n,order=2):
    'หาค่ารากลำดับใดๆ ของ n'
    if n==0: 
        return 0
    elif n<0:
        return "Cannot Calculate"

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
    print ("Root 2 of -2 =",root(-2)) 
    print ("Root 2 of 0 =",root(0))
    print ("Root 2 of 2 =",root(2))
    print ("Root 2 of 3 =",root(3))
    print ("Root 2 of 4 =",root(4))
    print ("Root 3 of 8 =",root(8,3))
    print ("Root 4 of 81 =",root(81,4))
    print ("Root 2.5 of 3 =",root(3,2.5))