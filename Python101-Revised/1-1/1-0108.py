'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.1.8
Description 
    format and raw
Note
    ตัวอย่างการใช้ format กับ print
    print ("Hello {0}")                         แสดงผล Hello {0}
    print ("Hello {0} World! {1}".format(3,10)) แสดงผล Hello 3 World! 10
    print ("Hello {1} World! {0}".format(3,10)) แสดงผล Hello 10 World! 3

    raw string จะพิมพ์ทุกตัวในเครื่องหมาย " ออกมาโดยไม่สนใจ escape charactor
    print (r"Hello World /n")           แสดงผล Hello World /n
    print (r"Hello /t World // /n")     แสดงผล Hello /t World // /n
Display
Hello {0}
Hello 3 World! 10
Hello 10 World! 3
Hello World \n
Hello    World \ 

Hello \t World \\ \n
Hel\tlo World   !
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.1.8
#Python 3.7.3

print ("Hello {0}")
print ("Hello {0} World! {1}".format(3,10))
print ("Hello {1} World! {0}".format(3,10))

print (r"Hello World \n")
print ("Hello\t World \\ \n")
print (r"Hello \t World \\ \n")
print (r"Hel\tlo","World\t!")
