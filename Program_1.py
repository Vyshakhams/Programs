#!/usr/bin/python
# -*- coding: utf-8 -*-
sentence = str(input('Enter a sentence to capitailize'))


def upper_case(sen_data):
    results = ''
    for char in sen_data:
        if char == ' ':
            results += ' '
        #If Char between a to z    
        elif ord(char) >= 97 and ord(char) <= 122:
            results += chr(ord(char) - 32)
        else:
            results += char
    return results


upperCaseSentence = upper_case(sentence)
print (upperCaseSentence)