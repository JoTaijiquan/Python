#Python 3.7.4
#Example F2-1-1

def multiply_2(number):
    aList = []
    for i in number:
        aList.append(i*2)
    return aList

if __name__=="__main__":
    input_ = [1,3,5,7,9,11]
    output_ = multiply_2(input_)
    print (output_)

    multiply_2l = lambda number: for i in number: number*2
    output__ = multiply_2l(input_)
    print (output__)