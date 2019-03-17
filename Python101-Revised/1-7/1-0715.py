#Example 1.7.15
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_715(x):
    x+=10
    return x

y = 0
y = example_715(10)
print (y)

'''
คำสั่ง return x จะส่งค่า x คืนออกมาที่ function
การใช้งานจึงต้องมีตัวมารับค่าที่ส่งคืนมา ในที่นี้คือ
y = example_715(10)

y เป็นตัวมารับค่าที่ return x ส่งออกมา

แสดงผล
20
'''
