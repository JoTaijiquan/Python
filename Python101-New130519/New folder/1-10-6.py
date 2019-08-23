#Python 3.7.3
#Example 1-10-6

import json

def func_1_10_6():

    'Not complete yet....'
    try:
        with open("test.txt","r") as f:
            x = json.load(f)
        print ("File Open!!!")
    except:
        print ("Cannot open file!!!")
    
    for i in x['name']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
    

if __name__ == "__main__":
    func_1_10_6()
