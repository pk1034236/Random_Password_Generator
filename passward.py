import random
import string

def generate_random_password(length):
    if length <= 0:
        return "Password length must be greater than 0."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the length of the password: "))
        random_password = generate_random_password(password_length)
        print(f"Generated Password: {random_password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
