#Example 1.5.6
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_506():
    a=[1,2,3,4,5]

    print ("1) a=",a)
    a.append(9)
    print ("2) append 9 to a =",a)
    a.extend([7,8,9])
    print ("3) extend [7,8,9] to a =",a)
    a.insert(2,"xyz")
    print ("4) insert xyz at position 2 =",a)
    print ("5) find position of 9 = ",a.index(9))
    print ("6) find position of 1 = ",a.index(1))
    print ("7) find position of xyz = ",a.index("xyz"))
    a.append ([11,12,13])
    print ("8) append [11,12,13] to a =",a)    
    
example_506()

'''
print ("1) a=",a) แสดงค่าใน list คือ [1, 2, 3, 4, 5]
a.append(9) เพิ่มข้อมูล 9 ใน list a
print ("2) append 9 to a =",a) แสดงค่าใน a = [1, 2, 3, 4, 5, 9]
a.extend([7,8,9]) นำ list [7,8,9] ต่อกับ list a
print ("3) extend [7,8,9] to a =",a) แสดงค่าใน a = [1, 2, 3, 4, 5, 9, 7, 8, 9]
a.insert(2,"xyz") แทรก "xyz" ในตำแหน่งที่ 2 ของ list a
print ("4) insert xyz at position 2 =",a) แสดงค่าใน a = [1, 2, 'xyz', 3, 4, 5, 9, 7, 8, 9]
print ("5) find position of 9 = ",a.index(9)) หาตำแหน่งของ 9 ใน a ได้ 6 (นับตำแหน่งแรกเป็น 0)
print ("6) find position of 1 = ",a.index(1)) หาตำแหน่งของ 1 ใน a ได้ 0
print ("7) find position of xyz = ",a.index("xyz")) หาตำแหน่งของ "xyz" ได้ 2
a.append ([11,12,13]) เพิ่ม list [11,12,13] ใน list a
print ("8) append [11,12,13] to a =",a) ได้ [1, 2, 'xyz', 3, 4, 5, 9, 7, 8, 9, [11, 12, 13]]

ข้อสังเกต
a.extend([7,8,9]) จะนำ list [7,8,9] เข้าไปต่อกับ list a
a.append([11,12,13]) จะนำ list [11,12,13] เข้าไปใส่ใน list a


แสดงผล
1) a= [1, 2, 3, 4, 5]
2) append 9 to a = [1, 2, 3, 4, 5, 9]
3) extend [7,8,9] to a = [1, 2, 3, 4, 5, 9, 7, 8, 9]
4) insert xyz at position 2 = [1, 2, 'xyz', 3, 4, 5, 9, 7, 8, 9]
5) find position of 9 =  6
6) find position of 1 =  0
7) find position of xyz =  2
8) append [11,12,13] to a = [1, 2, 'xyz', 3, 4, 5, 9, 7, 8, 9, [11, 12, 13]]
'''
