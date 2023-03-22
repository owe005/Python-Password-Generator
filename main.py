import random
import string

# A simple Python to generate a random password based on criteria.
# Author: owe005

def generate_password(length, uppercase, lowercase, numbers, special_characters):
    char = ""
    if uppercase:
        char += string.ascii_uppercase
    if lowercase:
        char += string.ascii_lowercase
    if numbers:
        char += string.digits
    if special_characters:
        char += string.punctuation
    
    password = ""
    for i in range(length):
        password += random.choice(char)

    return password

print("How many characters? (int)\n")
length = int(input("> "))
print("\nDo you want to include uppercase letters? (y/n)\n")
uppercase = (input("> ")).lower() == "y"
print("\nDo you want to include lowercase letters? (y/n)\n")
lowercase = (input("> ")).lower() == "y"
print("\nDo you want to include special characters? (y/n)\n")
special_characters = (input("> ")).lower() == "y"
print("\nDo you want to include numbers? (y/n)\n")
numbers = (input("> ")).lower() == "y"

password = generate_password(length,uppercase,lowercase,numbers,special_characters)
print(f"\nYour randomly generated password is: {password} ")

