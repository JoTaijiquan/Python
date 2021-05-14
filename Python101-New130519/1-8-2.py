#Python 3.9.5
#Example 1-8-2

def func_1_8_2():
    'การลบข้อมูลใน dictionary'
    
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

if __name__ == "__main__":
    func_1_8_2()
