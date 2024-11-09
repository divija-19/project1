import random


class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars
        
        # Define character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase if self.use_uppercase else ''
        self.numbers = string.digits if self.use_numbers else ''
        self.special_chars = string.punctuation if self.use_special_chars else ''
        
        # Combine all selected character sets
        self.all_characters = self.lowercase + self.uppercase + self.numbers + self.special_chars

    def generate_password(self):
        if len(self.all_characters) == 0:
            raise ValueError("At least one character set must be selected")

        # Generate a random password
        password = ''.join(random.choice(self.all_characters) for _ in range(self.length))
        return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    
    # Create a PasswordGenerator instance
    generator = PasswordGenerator(length=length)
    generated_password = generator.generate_password()
    
    print(f"Generated Password: {generated_password}")
