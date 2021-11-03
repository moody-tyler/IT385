#!/usr/bin/python3
password = input("Choose a password to be evaluated: ")

#Setting Variables
lowercase = False
uppercase = False
number = False
specialChar = False
passLength = False

#Evaluating password characteristics
for letter in password:
    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True
    elif letter in "abcdefhijklmnopqrstuvwxyz":
        lowercase = True
    elif letter in "0123456789":
        number = True
    elif letter in "!@#$%^*()_<>?":
        specialChar = True
    
if len(password) >= 8:
        passLength = True

#User feedback messages
if lowercase == True:
    print("You've met the requirement for lowercase letters")
elif lowercase == False:
    print("Please include at least one lowercase letter")

if uppercase == True:
    print("You've met the requirement for a capital letter")
elif uppercase == False:
    print("Please include at least one capital letter")

if number == True:
    print("You've met the requirements for numbers")
elif number == False:
    print("Please include at least one number")

if specialChar == True:
    print("You've met the requirement for special characters")
elif specialChar == False:
    print("Please include at least one special character")

if passLength == True:
    print("You've met the requirement for password length")
elif passLength == False:
    print("Please make password at least 8 characters")
