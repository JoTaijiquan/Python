'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.1.13
Description 
    docstrings
Note
    docstrings หรือ Python documentation strings
    เป็นการสร้างเอกสารไว้ภายในโปรแกรมด้วยการใส่ค่าคงที่สายอักษร หรือ string
    ไว้เป็นคำสั่งแรกภายในโปรแกรม หรือฟังก์ชันนั้น
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.1.13
#Python 3.7.3

'Program document'
def example_113():
    '''Function document.
Can be multi-line.'''
    print ("Hello")


example_113()
print ("**************\n")
print (example_113.__name__)
print (example_113.__doc__)
print ("**************\n")
print(__doc__)
