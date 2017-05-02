import re

def is_letter(character):
    return character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def split_words(input_string):
    words = []
    current_word = ''
    for character in input_string:
        if character == ' ':
            words.append(current_word)
            current_word = ''
        elif is_letter(character):
            current_word += character
    return set(words)

def word_cloud(long_string):
    d = {}
    for word in split_words(long_string):
        try:
            if word not in d:
                d[word] = 1
                print 'added: ', word
                d[word] += d[word.capitalize()]
                print 'added: ', word.capitalize()
                del d[word.capitalize()]
                print 'removed: ', word.capitalize()
            else:
                d[word.lower()]+=1
        except KeyError:
            continue
    return d
long_string = "After beating the eggs, Dana read the next step: Add milk and eggs, then add 2 Lbs of flour and sugar."
print word_cloud(long_string)
