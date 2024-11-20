import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        return "Please select at least one character type."
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

# User input
length = int(input("Enter the desired password length: "))
use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

# Generate and display password
print("Generated Password:", generate_password(length, use_letters, use_numbers, use_symbols))
