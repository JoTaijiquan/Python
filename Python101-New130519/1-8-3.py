#Python 3.9.5
#Example 1-8-3

def func_1_8_3():
    'การเพิ่มข้อมูลใน dictionary'
    
    x={ 'Jo': '123 Bangkok',
        'Mo': '456 Nonthaburi',
        'Yo': '789 Chiangmai'
        }

    for name,address in x.items():
        print (name,address)

    print ('\n--- Add Key Go and Do ---\n')
    x['Go'] = '200 Chiangrai'
    x['Do'] = '321 Lumpoon'

    for name,address in x.items():
        print (name,address)

if __name__ == "__main__":
    func_1_8_3()