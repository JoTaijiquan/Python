#Python 3.8.1
#Example 3-1-1

def vowels(word):
    vowels_list = [x for x in word if x.casefold() in "aeiou"]
    return word, vowels_list, len(vowels_list)

if __name__ == "__main__":
    print (vowels("Thailand"))
    print (vowels("Malaysia"))
    print (vowels("Singapore"))