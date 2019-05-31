#Python 3.7.3

def func_1_6_5():
    'for i in tuple'

    x = [1,3,5,7,9]
    for i in x:
        print (i)
        if i==5:
            x.extend([10,11,12,13])
    print (x)

if __name__ == "__main__":
    func_1_6_5()
