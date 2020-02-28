#Python 3.8.1
#Example 3-1-2

def x3(num):
    return num*3

if __name__ == "__main__":
    aList = [1,2,3,5,8,11]
    print (*list(map(x3,aList)))
    print (*list(map(x3,[2,4,6,8])),sep="\n")
