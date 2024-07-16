import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    # Define character sets based on the user's preferences
    character_sets = []
    if include_uppercase:
        character_sets.append(string.ascii_uppercase)
    if include_lowercase:
        character_sets.append(string.ascii_lowercase)
    if include_digits:
        character_sets.append(string.digits)
    if include_special:
        character_sets.append(string.punctuation)

    # Combine all the character sets into one string
    all_characters = ''.join(character_sets)

    # Generate a random password
    if len(all_characters) == 0:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    password = generate_password()
    print(f"Generated password: {password}")
