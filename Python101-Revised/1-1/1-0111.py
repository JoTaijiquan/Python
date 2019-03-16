#Example 1.1.11
#Python 3.6.5
#Created By Jooompot Sriyapan

print ("Hello {0}")
print ("Hello {0} World! {1}".format(3,10))
print ("Hello {1} World! {0}".format(3,10))

print (r"Hello World /n")
print (r"Hello /t World // /n")

'''
raw string จะพิมพ์ทุกตัวในเครื่องหมาย " ออกมาโดยไม่สนใจ escape charactor

print (r"Hello World /n")           แสดงผล Hello World /n
print (r"Hello /t World // /n")     แสดงผล Hello /t World // /n
'''
