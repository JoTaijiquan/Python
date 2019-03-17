#Example 1.6.12
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_612():

    for i in range(5):
        if i:
            pass
        print (i)

    print()
    
    for j in range(5):
        if j:
            continue
        print (j)

example_612()
'''
คำสั่ง pass แค่ไม่ทำอะไร ผ่านไปเฉยๆ
แล้วไปทำคำสั่ง print(i) ต่อ

ส่วน continue จะทำให้ขึ้นรอบใหม่เลย
โดยไม่ทำคำสั่งถัดไป คำสั่ง print(j) จึงไม่ทำงาน

แสดงผล
0
1
2
3
4

0
'''
