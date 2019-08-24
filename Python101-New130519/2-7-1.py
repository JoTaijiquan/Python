#Python 3.7.3
#Example 2-7-1

'MORSE Code encoder/decoder'
morse_dict= {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 
    'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 
    'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 
    'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 
    'z':'--..', 
    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
    '.':'.-.-.-', ',':'--..--', ':':'---...', '?':'..--..', '\'':'.----.', 
    '-':'-....-', '/':'-..-.', '(':'-.--.', ')':'-.--.-', '"':'.-..-.', 
    '=':'-...-', '+':'.-.-.', '*':'-..-', '@':'.--.-.', 
    }

def text_morse(txt):
    m_code = []
    for letter in txt.lower():
        if letter in morse_dict:
            m_code.append(morse_dict[letter])
        else:
            m_code.append('')
    return m_code

def morse_text(txt):
    t_code = ''
    
    for letter in txt:
        try:
            t_code+=list(morse_dict.keys()) \
            [list(morse_dict.values()).index(letter)]
        except:
            t_code+=' '
    return t_code

if __name__ == "__main__":
    print ("hello,world! ",*text_morse("hello,world!"))
    print ("sos SOS!! ",text_morse("sos SOS!!"))
    print ("'S' ",*text_morse("'S'"))
    print ("\"O\"",*text_morse('\"O\"'))
    print(morse_text(['...','---','abcd','...',]))