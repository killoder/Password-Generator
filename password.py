import random
import string

def generate_password(length=12, use_special_chars=True, use_uppercase=True, use_digits=True):
    """
    Generates a random password with specified criteria.
    :param length: Length of the password (default is 12 characters)
    :param use_special_chars: Include special characters (default is True)
    :param use_uppercase: Include uppercase letters (default is True)
    :param use_digits: Include digits (default is True)
    :return: Randomly generated password
    """
    chars = string.ascii_lowercase
    if use_special_chars:
        chars += string.punctuation
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example usage:
generated_password = generate_password(length=16, use_special_chars=True, use_uppercase=True, use_digits=True)
print(f"Generated Password: {generated_password}")
