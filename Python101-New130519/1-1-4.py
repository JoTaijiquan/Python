#Python 3.7.3
#Example 1-1-4

'บันทึกสนุกๆ'
def MySecondFunction():
    'เขียนเล่น'
    print ("ขีดๆ","เขียนๆ","เรียนๆ","เล่นๆ")

if __name__ == "__main__":
    MySecondFunction()
    print ("Program Name is",__name__)
    print ("Program Document is",__doc__)
    print ("Function Name is", MySecondFunction.__name__)
    print ("Function Document is", MySecondFunction.__doc__)