#Example 7.08
#Python3.6.5

def example_708():
    global x
    x = x+10

x = 10
print (x)
example_708()
print (x)
example_708()
print (x)


'''
ปกติการเปลี่ยนค่าตัวแปรใน function จะไม่กระทบตัวแปรนอก function
แต่ถ้ากำหนดให้ตัวแปรใน function เป็น global
คำสั่ง global x

ทำให้ตัวแปร x เป็นตัวแปร global ใช้ได้ทั้งในและนอก function

แสดงผล
10
20
30
'''
