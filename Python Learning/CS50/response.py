from validator_collection import validators

mail = input("What's your email address?")
try:
    is_valid = validators.email(mail)
    print("Valid")
except:
    print("Invalid")
