#Example 1.8.4
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_804():
    x = set([3,5,7,8,3])
    y = x.copy()
    
    print ("1)",x,y)
    x.add(22)
    print ("2)",x,y)
    y.add(3)
    print ("3)",x,y)
    x.remove(3)
    print ("4)",x,y)

example_804()

'''
x = set[3,5,7,8,3] สร้าง set x
y = x.copy() ลอกข้อมูลใน set x มาใส่ใน set y

print ("1)",x,y) ได้ 1) {8, 3, 5, 7} {8, 3, 5, 7}
สังเกตว่าตอนสร้าง set x เราใส่ 3 ไว้สองตัว แต่พอ print ออกมาเหลือตัวเดียว
ทั้งนี้เพราะข้อมูลใน set ถ้าซ้ำกันจะถือว่าเป็นตัวเดียวกัน จะไม่สร้างข้อมูลซ้ำให้

x.add(22) เพิ่มข้อมูลใน set

x.remove(3) ลบข้อมูลออกจาก set

ข้อสังเกต
y= x.copy() เป็นการลอกข้อมูลจาก x ไปใส่ใน y การเปลี่ยนแปลงข้อมูลของแต่ละ set
ไม่มีผลต่อกัน


แสดงผล
1) {8, 3, 5, 7} {8, 3, 5, 7}
2) {3, 5, 7, 8, 22} {8, 3, 5, 7}
3) {3, 5, 7, 8, 22} {8, 3, 5, 7}
4) {5, 7, 8, 22} {8, 3, 5, 7}
'''
