#Example 8.02
#Python3.6.5

def example_802():
    x={ 'Jo': '123 Bangkok',
        'Mo': '456 Nonthaburi',
        'Yo': '789 Chiangmai'
        }

    for name,address in x.items():
        print (name,address)
        
    del x['Jo']
    print ('\n--- Delete Key Jo ---\n')

    for name,address in x.items():
        print (name,address)

    x['Go'] = '200 Chiangrai'
    x['Do'] = '321 Lumpoon'
    print ('\n--- Add Key Go and Do ---\n')

    for name,address in x.items():
        print (name,address)


example_802()

'''
for name,address in x.items():
    print (name,address)
สั่งให้แสดงผลข้อมูลทั้งหมดใน dictionary ออกมา

del x['Jo']
ลบข้อมูล key 'Jo' ออกจาก dictionary

x['Go'] = '200 Chiangrai'
x['Do'] = '321 Lumpoon'
เพิ่มข้อมูลเข้าไปใน dictionary

แสดงผล
Jo 123 Bangkok
Mo 456 Nonthaburi
Yo 789 Chiangmai

--- Delete Key Jo ---

Mo 456 Nonthaburi
Yo 789 Chiangmai

--- Add Key Go and Do ---

Mo 456 Nonthaburi
Yo 789 Chiangmai
Go 200 Chiangrai
Do 321 Lumpoon
'''
