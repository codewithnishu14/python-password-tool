import random
import string

def generate_password(length):
    # Characters list: uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters of the given length
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Program start here
print("=== Welcome to Python Password Tool ===")
user_length = int(input("Enter password length (e.g., 8, 12, 16): "))

if user_length < 6:
    print("Password is too short! Please choose at least 6 characters.")
else:
    new_password = generate_password(user_length)
    print(f"Your Generated Secure Password is: {new_password}")

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    # Score count karne ke liye
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if length >= 8 and score >= 3:
        return "Strong 💪"
    elif length >= 6 and score >= 2:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

# Program start here
print("=== Welcome to Python Password Tool ===")
print("1. Generate a Password")
print("2. Check Password Strength")

choice = input("Choose an option (1 or 2): ")

if choice == '1':
    user_length = int(input("Enter password length (e.g., 8, 12, 16): "))
    if user_length < 6:
        print("Password is too short! Please choose at least 6 characters.")
    else:
        new_password = generate_password(user_length)
        print(f"Your Generated Secure Password is: {new_password}")

elif choice == '2':
    user_password = input("Enter a password to check its strength: ")
    result = check_strength(user_password)
    print(f"Password Strength: {result}")

else:
    print("Invalid choice! Please run the program again and select 1 or 2.")

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if length >= 8 and score >= 3:
        return "Strong 💪"
    elif length >= 6 and score >= 2:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

# Loop start here so the program keeps running until the user exits
while True:
    print("\n=== Python Password Tool ===")
    print("1. Generate a Password")
    print("2. Check Password Strength")
    print("3. Exit")
    
    choice = input("Choose an option (1, 2, or 3): ")
    
    if choice == '1':
        try:
            user_length = int(input("Enter password length (e.g., 8, 12, 16): "))
            if user_length < 6:
                print("Password is too short! Please choose at least 6 characters.")
            else:
                new_password = generate_password(user_length)
                print(f"Your Generated Secure Password is: {new_password}")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == '2':
        user_password = input("Enter a password to check its strength: ")
        result = check_strength(user_password)
        print(f"Password Strength: {result}")

    elif choice == '3':
        print("Thank you for using Password Tool! Goodbye 👋")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

