#Example 8.03
#Python3.6.5

def example_803():
        x={}

        x['A'] = 'Ada'
        x['B'] = 'Basic'
        x['C'] = 'Cobol'

        for first, second in x.items():
            print (first,second)

        if 'A' in x:
            print (x['A'])

        print (x.items())
        print ("number of item in x=",len(x.items()))

example_803()

'''
รูปแบบการใช้งาน dictionary

แสดงผล
A Ada
B Basic
C Cobol
Ada
dict_items([('A', 'Ada'), ('B', 'Basic'), ('C', 'Cobol')])
number of item in x= 3
'''
