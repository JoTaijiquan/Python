#Example 1.1.13
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_113():
    'Example 1.13 Document, Write any thing here!!'
    print ("Hello")


example_113()
print ("**************\n")
print (example_113)
print (example_113.__name__)
print (example_113.__doc__)

'''
เมื่อสร้าง function แล้ว สามารถใส่คำอธิบายฟังก์ชันไว้ในเครื่องหมาย '' ในบรรทัดถัดจากชื่อฟังก์ชัน
เมื่อสั่งพิมพ์ function.__doc__ ก็จะสามารถแสดงคำอธิบายฟังก์ชันที่ใส่ไว้ได้

example_113()                   แสดงผล Hello
print ("**************\n")      แสดงผล ************** เว้นหนึ่งบรรทัด
print (example_113)             แสดงผล <function example_113 at 0xxxxxxxxxx>
print (example_113.__name__)    แสดงผล example_113
print (example_113.__doc__)     แสดงผล Example 1.13 Document, Write any thing here!!

'''
