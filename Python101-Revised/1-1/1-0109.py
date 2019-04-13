'''
Create By Joompot Sriyapan
Date 6/4/2019

Name 
    Example 1.1.9
Description 
    function 
Note
    สร้างคำสั่งหรือ function ด้วย def
    function ที่สร้างไว้แล้ว สามารถเรียกใช้ได้เรื่อยๆ 

    example_112()       แสดงผล Hello!
    example_112()       แสดงผล Hello!
    print ("World!")    แสดงผล World!
    example_112()       แสดงผล Hello!
    example_112()       แสดงผล Hello!

    docstrings หรือ Python documentation strings
    เป็นการสร้างเอกสารไว้ภายในโปรแกรมด้วยการใส่ค่าคงที่สายอักษร หรือ string
    ไว้เป็นคำสั่งแรกภายในโปรแกรม หรือฟังก์ชันนั้น
Display
    
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.1.9
#Python 3.7.3

'คำอธิบายโปรแกรม'
def example_109():
    '''คำอธิบายฟังก์ชัน 
    แบบหลายบรรทัด'''

    print ("Hello!")

example_109()
example_109()
print ("World!")
example_109()

print ("**************\n")
print ("Function Name=",example_109.__name__)
print ("Function Docs=",example_109.__doc__)
print ("**************\n")
print ("Program name=",__name__)
print("Program Docs=",__doc__)