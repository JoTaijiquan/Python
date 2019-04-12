'''
Create By Joompot Sriyapan
Date 5/4/2019

Name 
    Example 1.1.6
Description 
    escape character
Note
    กรณีต้องการแสดงผล " ใช้ \"
    กรณีต้องการแสดงผล \ ใช้ \\
    เรียกว่า escape character

    \n ขึ้นบรรทัดใหม่
    \n\n ชึ้นบรรทัดใหม่สองครั้ง
    \t เว้นวรรค (tab)
    \U000001a9 รหัสยูนิโค้ดเครื่องหมาย Ʃ
Display
    "Hello"
    \Hello\
    Hello

    World!
    Hello


    World!
    Hello   World!
    'Hello'
    Ʃ
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.1.6
#Python 3.7.3

print ("\"Hello\"")     #แสดงผล "Hello"
print ("\\Hello\\")     #แสดงผล \Hello\

print ("Hello\n")       #escape character \n สั่งขึ้นบรรทัดใหม่     
print ("World!")
print ("Hello\n\n")     # \n\n ขึ้นบรรทัดใหม่สองครั้ง
print ("World!")
print ("Hello\tWorld!") #\t เว้นวรรค tab
print ("\'Hello\'")
print ("\U000001a9")