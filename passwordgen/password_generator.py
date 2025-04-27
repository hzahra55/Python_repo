import random
import string

def generate_password(min_lenght, numbers=True, special_characters="True"):
    
    letters = string.ascii_letters
    digits = string.digits
    specialchar = string.punctuation

    characters = letters   #always will have characters
    if numbers:             #add to letters
        characters += digits
    if special_characters:      #ada to characters
        characters += specialchar

    #every iteration add character to random password until meet criteria is true or desired length is achieved
    pwd = ""    #password stored here
    meets_criteria = False  #true once pwd set
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char
    #do this way or other way i sthat once whole password is generated then check if it has all characters this is more efficient way
    if new_char in digits:
        has_number = True
    elif new_char in specialchar:
        has_special = True
    
    #now you have true for these but have to set these two for meet_criteria too
    meets_criteria = True
    if numbers:
        meets_criteria = has_numbers
    if special_characters:  #rewriting here and "and" here because must have numbers
        meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("enter minimum length: "))
has_number = input("do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length,has_number,has_special)
print ("generated password is "+pwd)
    





