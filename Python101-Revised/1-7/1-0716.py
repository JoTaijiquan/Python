#Example 1.7.16
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_716(x):
    x = x+"abc"
    return x

print(example_716(""))
print (example_716("123"))

'''
คำสั่ง return จะส่งค่าคืนออกมาทาง function
จึงสามารถสั่ง
print(example_716("123")) ซึ่งจะมีค่าเท่ากับสั่ง print("123abc")


แสดงผล
abc
123abc
'''
