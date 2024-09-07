import random
import string


def generate_password(length):
    # Define the characters that will be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    # Prompt the user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                raise ValueError("Length must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
