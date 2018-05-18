"""
PasswordToolkit 0.1
Generate or check a secure Password
by Dylan Hamer
"""

import random  # Random choices
import string  # String constants

class generator:
    """Password generator class"""
    def __init__(self):
        self.minLength = 8  # Minimum password length
        self.maxLength = 12  # Maximum password length
        
        """String constants for character types"""
        self.lowercase = list(string.ascii_lowercase)
        self.uppercase = list(string.ascii_uppercase)
        self.symbols = ["!", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
        self.digits = list(string.digits)
        
        self.allowedChars = list(self.lowercase + self.uppercase + self.symbols + self.digits)  # All allowed characters
                    
    def generate(self):
        """Generate a secure password"""
        strong = False
        while not strong:
            password = ""  # String to store password
            length = random.randint(self.minLength, self.maxLength)  # Random password length
            for character in range(length):  # Iteratively fill password
                password += random.choice(self.allowedChars)  # Choose a random character from allowed characters
            passwordChecker = checker()
            score = passwordChecker.check(password)["score"]
            strong = bool(score > 20)
        return password, score
        
class checker:
    """Password checker class"""
    def __init__(self):
        self.minLength = 8  # Minimum password length
        self.maxLength = 24  # Maximum password length
        
        """These need to be a list for the countAll function"""
        self.lowercase = list(string.ascii_lowercase) 
        self.uppercase = list(string.ascii_uppercase)
        self.symbols = ["!", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
        self.digits = list(string.digits)
        self.allowed = self.lowercase + self.uppercase + self.symbols + self.digits
      
    def checkQwerty(self, password):
        """Check for consecutive keyboard letters"""
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        chunks = []
        total = 0
        for row in keyboard:
            for i in range(len(row)-2):
                chunks.append(row[i:i+3])
                
        for chunk in chunks:
            total += password.count(chunk)
        
        return total
        
    def countAll(self, listOfChars, text):
        """Count all occurences of any letter in an array"""
        total = 0
        for char in listOfChars:
            total += text.count(char)  # Text.count returns the amount of a certain character in a string, do this recursively
        return total
        
    def check(self, password, display=False):
        """Check various elements that make up a secure password"""
        
        if len(password) < 8 or len(password) > 24:
            print("Password too long or too short!")
            return
        
        for character in password:
            if character not in self.allowed:
                print("Password contains invalid characters!")
                return
        
        checkResults = {"length":len(password),
                        "lowercase":self.countAll(self.lowercase, password),
                        "uppercase":self.countAll(self.uppercase, password),
                        "symbols":self.countAll(self.symbols, password),
                        "digits":self.countAll(self.digits, password),
                        "keyboard":self.checkQwerty(password),
                        "score":None}
                        
        score, messages = self.calculateScore(checkResults)  # Calculate a score
        
        checkResults["score"] = score
        
        if display:
            for message in messages:
                print(message)
        
        return checkResults
    
    def calculateScore(self, checkResults):
        """Calculate a strength score based on a set of criteria"""
        """Note: this function might need to be cleaned up a little"""
        score = checkResults["length"]  # Add length to score
        lowercase, uppercase, symbols, digits = False, False, False, False
        uppercaseAmount = checkResults["uppercase"]
        lowercaseAmount = checkResults["lowercase"]
        symbolAmount = checkResults["symbols"]
        digitAmount = checkResults["digits"]
        keyboard = checkResults["keyboard"]
        messages = []  # Temporary variables for storing info
        if uppercaseAmount >= 1:
            uppercase = True
            score += 5
            messages.append("You were awarded 5 points for having at least one uppercase character.")
        if lowercaseAmount >= 1:
            lowercase = True
            score += 5
            messages.append("You were awarded 5 points for having at least one lowercase character.")
        if digitAmount >= 1:
            digits = True
            score += 5
            messages.append("You were awarded 5 points for having at least one digit (0-9).")
        if symbolAmount >= 1:
            symbols = True
            score += 5
            messages.append("You were awarded 5 points for having at least one allowed symbol.")
        if uppercase and lowercase and digits and symbols:
            score += 10
            messages.append("You were awarded 10 points for having at least one uppercase character, one lowercase, one digit and one symbol.")
        if not digits:
            score -= 5
            messages.append("You were deducted 5 points for not having any digits.")
        if not symbols:
            score -= 5
            messages.append("You were deducted 5 points for not having any symbols.")
        if not lowercase:
            score -= 5
            messages.append("You were deducted 5 points for not having any lowercase characters.")
        if not uppercase:
            score -= 5
            messages.append("You were deducted 5 points for not having any uppercase characters.")
        if keyboard > 0:
            score -= keyboard*5
            messages.append("You were deducted {} points for having {} multiples of 3 consecutive keyboard letters.".format(keyboard, keyboard*5))
        return score, messages
        
    def formatData(self, checkResults):
        """Display check data in a nice human readable format"""
        print()
        print("Password length: {}".format(checkResults["length"]))
        print("Lowercase characters: {}".format(checkResults["lowercase"]))
        print("Uppercase characters: {}".format(checkResults["uppercase"]))
        print("Amount of symbols: {}".format(checkResults["symbols"]))
        print("Amount of digits (0-9): {}".format(checkResults["digits"]))
        print("Multiples of 3 of consecutive keyboard letters: {}".format(checkResults["keyboard"]))
        print()
        print("Security score: {}".format(checkResults["score"]))
        print()
        print("How well did you do?")
        print("Security score below 0: You need a much better password!")
        print("Security score between 0 and 20: Your password is okay but might need improvement.")
        print("Security score above 20: You're an expert at choosing passwords! Rock on!")
        print()
        if checkResults["length"] >= 12:
          print("Your password is quite long. Consider using a password manager to avoid forgetting your password.")
        print("Want to generate a secure password? Try using the password generator option.")

def main():
    print("PasswordToolkit 0.2 by Dylan Hamer\n")
    passwordGenerator = generator()  # Initialise the generator class
    passwordChecker = checker()  # Initialise the checker class
    chosen = False  # Temporary variable to loop until a vaild choice is selected
    while not chosen:
        print("\nWhat would you like to do?")
        print("1. Generate a secure password")
        print("2. Check if a password is secure")
        print("3. Quit")
        print()
        choice = input("Your choice: ")
        print()
        if choice == "1":
            chosen = True
            password, score = passwordGenerator.generate()
            print("Your secure password is: {}".format(password))
            print("It has a strength score of: {}".format(score))
        elif choice == "2":
            chosen = True
            password = input("Enter your password: ")
            print()
            checkResults = passwordChecker.check(password, True)
            if checkResults is not None:
                passwordChecker.formatData(checkResults)
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice.")
            

main()
