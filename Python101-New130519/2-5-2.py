#Python 3.7.3
#Example 2-5-2

def BinarySearch(aList,key):
    'Binary Search return location of key in list'

    first = 0
    last = len(aList)-1
    i = "Not Found!!!"
    
    while (first<=last) and (i=="Not Found!!!"):
        mid = (first+last)//2
        if aList[mid] == key:
            i=mid
        else:
            if key<aList[mid]:
                last = mid-1
            else:
                first = mid+1
    return i

if __name__ == "__main__":
    aList=[20,12,3,18,7,8,25,14]
    print ("Unsorted List = ", aList)
    aList.sort()
    print ("Sorted List = ",aList)
    print ("Search 3 = ",BinarySearch(aList,3))
    print ("Search 18 = ",BinarySearch(aList,18))
    print ("Search 25 = ",BinarySearch(aList,25))
    print ("Search 30 = ",BinarySearch(aList,30))

