#Example 1.6.4
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_604():
    a =[1,2,3,4,5,6,7,8,9,10]
    for i in a:
        if i==3:
            a[5]=13
        print (i)
        
example_604()

'''
ข้อสังเกต
เมื่อ i==3 มีการเปลี่ยนค่า a[5] =13
ดังนั้น ผลจึงเป็น 1 2 3 4 5 13 7 8 9 10

แสดงผล
1
2
3
4
5
13
7
8
9
10
'''
