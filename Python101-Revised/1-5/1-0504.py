#Example 1.5.4
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_504():
    a = [1,2,3,4,5]

    print ("1) a = ",a)
    a[0]=7
    a[2]=['a','b',"c,d,e",8,9+2]
    print ("2) a = ",a)

example_504()

'''
กำหนดค่าภายในลิสต์ได้โดยระบุตำแหน่งในลิสต์
a[0] = 7 กำหนดค่าให้ a[0] = 7
a[2]=['a','b',"c,d,e",8,9+2] กำหนดค่าให้ a[2] เป็นอีกลิสต์หนึ่งซ้อนเข้าไปได้

แสดงผล
1) a =  [1, 2, 3, 4, 5]
2) a =  [7, 2, ['a', 'b', 'c,d,e', 8, 11], 4, 5]
'''
