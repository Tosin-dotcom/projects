import re


print("Welcome. \nThis is a password validator software.")
print("This software validate your password with some certain rules")

valid_password = False
while valid_password is False:
    password = input("Enter your password here: ")
    if (
        4 < len(password) < 11
        and re.search("[A-Z]", password)
        and re.search("[0-9]", password)
        and re.search('[!"£$%^&*_+~#<>/?@`¬()={}]', password)
    ):
        print("Valid password")
        valid_password = True
    else:
        if len(password) < 5:
            print("Minimum of 5")
        if len(password) > 10:
            print("Maximum of 10")
        if not re.search("[A-Z]", password):
            print("Must contain Capital letter")
        if not re.search("[0-9]", password):
            print("Must contain at least one number")
        if not re.search('[!"£$%^&*_+~#<>/?@`¬()={}]', password):
            print("Must contain at least one symbol")
