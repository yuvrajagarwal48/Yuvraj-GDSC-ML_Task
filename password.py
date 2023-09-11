import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):

    uppercase = string.ascii_uppercase if use_uppercase else ''
    lowercase = string.ascii_lowercase if use_lowercase else ''
    digit = string.digits if use_digits else ''
    special = string.punctuation if use_special_chars else ''


    all = uppercase + lowercase + digit + special

    if not all:
        raise ValueError("At least one character set must be selected")


    password = ''.join(random.choice(all) for _ in range(length))

    return password

try:

    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

    print(f"Your randomly generated password is: {password}")
except ValueError as e:
    print(f"Error: {e}")
