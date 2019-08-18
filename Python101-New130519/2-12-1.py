#Python 3.7.3
#Example 2-5-1

def LinearSearch(aList,key):
    'LinearSearch return index'

    for i in range(len(aList)):
        if aList[i]==key:
            return i
    return "Not Found!!!"

if __name__ == "__main__":
    aList=[20,12,3,18,7,8,25,14]
    print ("Search 20 = ",LinearSearch(aList,20))
    print ("Search 18 = ",LinearSearch(aList,18))
    print ("Search 14 = ",LinearSearch(aList,14))
    print ("Search 30 = ",LinearSearch(aList,30))  