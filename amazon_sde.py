#!/usr/bin/env python
def parser(input):
    #remove periods and other characters. Useful to detect words that are ending with
    #capital letters.
    input = input.translate(None, ',.!@#$')
    tokens = input.split()
    ALL_CAPS = list()
    length = len(tokens)
    initCap = list()
    lastCap = list()
    palindromes = list()
    anagrams = list()
    count_anagrams = 0
    for item in tokens:
        if (item.isupper()):
            ALL_CAPS.append(item)
        if (item[0].isupper()):
            initCap.append(item)
        if (item[len(item)-1].isupper()):
            lastCap.append(item)
        #convert words to lowercase to match palindromes that start with a capital letter
        #one letter are words are assumed not to be palindromes
        if (str(item.lower()) == str(item.lower())[::-1] and len(item)>1):
            palindromes.append(item)
    for item in tokens:
        for item2 in tokens:
            if(len(item) == len(item2)):
                if (sorted(item) == sorted(item2)):
                    count_anagrams=count_anagrams+1


    print "1) Total Words: ", length
    print "2) Words with all caps: ", " ".join(ALL_CAPS)
    print "3) Words with starting Caps: ", " ".join(initCap)
    print "4) Words Ending with Caps: ", " ".join(lastCap)
    print "5) Palindromes: ", " ".join(palindromes)
    print "6) Anagrams: ", count_anagrams
    #print "7) Anagrams: ", " ".join(anagrams)

#driver

input = "Anna took an applE from the basket, BUT EMma did noT. Noon came and Anna decided the applE was not a lemon, not a melon but still was an apple. And she ate it."
input2 = "L9WmE0V/ZG0Ky9AToF5vDu5Jpj58nqh+Ds+g270KtU8="
parser(input)


"""
USE BELOW TO READ FROM A FILE
with open(fname) as f:
    content = f.readlines()
"""
