'''
import string
def checkForNumber(inputstr : str) -> bool:
    for x in inputstr:
        if x.isdigit():
            return True
    return False

def checkCaps(inputstr : str) -> bool:
    for y in inputstr:
        if y.isupper():
            return True
    return False
        
passcodeAttempt = input("Enter in a passcode for your new account: ")
uppercase = list(string.ascii_uppercase)

if checkForNumber(passcodeAttempt) == True and checkCaps(passcodeAttempt) == True and len(passcodeAttempt) >= 5:
    print("Your passcode is valid. Please continue.")
else:
    print("Passcode is invalid: Please check the statements below:")
    if checkForNumber(passcodeAttempt) == False:
        print("You do not have an integer in your passcode.")
    if checkCaps(passcodeAttempt) == False:
        print("You need one capital letter in your passcode.")
    if len(passcodeAttempt) < 5:
        print("Your passcode must be 5 characters or longer.")
'''










