#Example 1.5.17
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_517():
    a = [11,12,13,14,21,22]
    print ("1)",a[2:2])
    a = [11,12,['xx','yy'],14,21,22]
    print ("2)",a[2:4])

example_517()

'''
a = [11,12,13,14,21,22,23,24]           กำหนดค่า list a=[11,12,13,14,21,22] 
print ("1)",a[2:2])                     แสดงผล list a ตั้งแต่ตัวที่ 2 ไม่เกินตัวที่ 2 ได้ []

a = [11,12,['xx','yy'],14,21,22,23,24]  กำหนดค่า list a=[11,12,['xx','yy'],14,21,22]
print ("2)",a[2:4])                     แสดงผล list a ตั้งแต่ตัวที่ 2 ไม่เกินตัวที่ 4 ได้[['xx', 'yy'], 14]

แสดงผล
1) []
2) [['xx', 'yy'], 14]
'''
