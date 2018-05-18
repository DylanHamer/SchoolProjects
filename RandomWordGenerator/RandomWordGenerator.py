"""
Random Word Maker
Makes random words from a set of syllables
by Dylan Hamer

Note: I need to tidy this code and comment it
"""

import random, string

alphabet = string.ascii_lowercase
punctuation = ["!", ".", "..."]
vowels = ["a", "e", "o", "i", "u"]
uncommon = ["x", "q", "z", "v", "j", "y"]
consonants = []
syllables = []

"""Add all consonants except uncommon ones to the list of syllables"""
for letter in alphabet:
    if not letter in vowels and not letter in uncommon:
        consonants.append(letter)
        
"""Add pairs of consonants and vowels to the list of syllables"""
for consonant in consonants:
    for vowel in vowels:
        syllables.append(consonant+vowel)

"""Add vowels to the list of syllables"""
for vowel in vowels:
    syllables.append(vowel)

def genRandomWord(amountOfSyllables):
    """Generate a random word with a fixed amount of syllables"""
    randomWord = []
    for count in range(amountOfSyllables):
        randomSyllable = random.choice(syllables)
        randomWord.append(randomSyllable)
    return "".join(randomWord)
    
def capitaliseFirst(word):
    """Capitalise the first character of a string"""
    firstLetter = word[0].upper()
    if len(word) > 2:
        rest = word[1:]
    else:
        rest = word[1]
    return firstLetter+rest
    
def randomSentence(amountOfWords, minimumSyllables, maximumSyllables):
    """Generate a random sentence with a minimum and maximum possible amount of syllables"""
    randomSentence = []
    for count in range(amountOfWords):
        randomSyllableAmount = random.randint(minimumSyllables, maximumSyllables)
        randomWord = genRandomWord(randomSyllableAmount)
        randomSentence.append(randomWord)
        randomPunctuation = random.choice(punctuation)
        formattedSentence = [capitaliseFirst(randomSentence[0]), " ".join(randomSentence[1:]), randomPunctuation]
    newSentence = []
    for i in formattedSentence:
        newSentence.append(i)
    return "".join(newSentence)
    
def main():
    print("Your randomly generated sentence is:")
    print(randomSentence(10, 1, 3))
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    