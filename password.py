import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    # Define character sets based on complexity requirements
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets
    all_chars = uppercase_chars + lowercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        raise ValueError("At least one character set must be selected")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        # Get user input for password length and complexity
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        # Generate the password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

        # Print the generated password
        print(f"Your randomly generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")
