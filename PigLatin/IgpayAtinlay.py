"""
Pig Latin
Convert text to pig latin
This is probably the worst code I've ever written and frankly I'm embarrased to put my name on it
by Dylan Hamer
October 12th 2017
"""

import string

alphabet = string.ascii_lowercase
vowels = ["a", "e", "i", "o", "u"]

def pigLatin(word):
    consonantsInWord = []
    if word[0] in vowels:
        pigLatin = word + "ay"
    else:
        for letter in word:
            if letter not in vowels:
                consonantsInWord.append(letter)
            else:
                break
        pigLatin = word[len(consonantsInWord):] + "".join(consonantsInWord) + "ay"
    return pigLatin

while True:
    sentence = []
    text = input("Text to convert: ")
    for word in text.split(" "):
        sentence.append(pigLatin(word))
    print(" ".join(sentence))
        
        
            
    
            
    
    
