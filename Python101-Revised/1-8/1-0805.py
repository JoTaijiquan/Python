#Example 8.05
#Python3.6.5

def example_805():
    x = set([5, 7, 8, 22])
    y = set([8, 3, 5, 7])
    print (x,y)
    print (set(x).intersection(y))
    print (x & y)

    print (set(x).union(y))    
    print (y | x)

example_805()

'''
แสดงตัวอย่างการดำเนินการกับ set

print(x,y) ก็แสดงผล 2 set เฉยๆ

intersectioin แสดงผลเฉพาะค่าที่ซ้ำกันระหว่าง 2 set ทำได้สองวิธี
print (set(x).intersection(y))
หรือ
print (x & y)

union รวมค่าของสองเซ็ตเข้าด้วยกัน (ไม่นับตัวซ้ำ) ก็ทำได้สองวิธี
print (set(x).union(y))
หรือ
print (y | x)

ข้อสังเกต
ข้อมูลใน set จะไม่สนใจลำดับของสมาชิก อยู่ก่อนอยู่หลัง ไม่ได้มีผลอะไร

แสดงผล
{8, 5, 22, 7} {8, 3, 5, 7}
{8, 5, 7}
{8, 5, 7}
{3, 5, 7, 8, 22}
{3, 5, 7, 8, 22}
'''
