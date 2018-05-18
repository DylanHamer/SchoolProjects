"""
Check if Palindrome
Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
by Dylan Hamer
October 12th 2017
"""

def reverseString(text):
    reversedText = text[::-1]  # Advanced slice snytax to reverse a string
    return reversedText

def main():
    text = input("Please enter the text you would like to check: ")
    if text == reverseString(text):
        print(text + " is a palindrome!")
    else:
        print(text + " is not a palindrome!")

if __name__ == "__main__":
    main()
