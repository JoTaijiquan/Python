#Example 1.4.7
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_407():
    for i in range(10):
        if i==5:
            i=i+3
        print (i)

example_407()

'''
เมื่อ i มีค่าเท่ากับ 5 ให้เอา i=i+3  ได้ 8 แล้วไปแสดงผล
ดังนั้นค่าที่แสดงจะกระโดด 0 1 2 3 4 8 (5+3) แล้วจึงค่อยเป็น 6
    
แสดงผล
0
1
2
3
4
8
6
7
8
9
'''
