#Example 10.01
#Python 3.6.5

def example_1001():
    f = open("test.txt","w")
    f.write ("abcde abcde abcde")
    f.write ("def def def\n")
    f.write ("abc abc abc\n")
    print ("Hello",file=f) 
    print ("There",file=f)
    f.close()


example_1001()


'''

แสดงผล
'''
