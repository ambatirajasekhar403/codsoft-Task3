import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected. Please enable at least one.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    return use_uppercase, use_lowercase, use_digits, use_special

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    use_uppercase, use_lowercase, use_digits, use_special = get_user_preferences()

    while True:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        if password:
            print("Generated Password:", password)

        generate_more = input("Do you want to generate another password? (y/n): ").lower()
        if generate_more != 'y':
            break

        while True:
            try:
                length = int(input("Enter the new desired length of the password: "))
                if length > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        use_uppercase, use_lowercase, use_digits, use_special = get_user_preferences()

if __name__ == "__main__":
    main()
