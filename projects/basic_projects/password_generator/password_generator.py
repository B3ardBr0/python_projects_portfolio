#!/usr/bin/env python3
"""
Password Generator
A secure password generator with customizable options for length and character sets.
"""

import random
import string
import secrets
from typing import List


class PasswordGenerator:
    """A secure password generator with various customization options."""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.punctuation = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
    def generate_password(self, length: int = 12, use_uppercase: bool = True, 
                         use_lowercase: bool = True, use_digits: bool = True, 
                         use_symbols: bool = True, exclude_ambiguous: bool = False) -> str:
        """
        Generate a secure password with specified criteria.
        
        Args:
            length: Password length (default: 12)
            use_uppercase: Include uppercase letters
            use_lowercase: Include lowercase letters
            use_digits: Include numbers
            use_symbols: Include special symbols
            exclude_ambiguous: Exclude ambiguous characters (0, O, l, 1, etc.)
            
        Returns:
            Generated password string
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
            
        character_pool = ""
        required_chars = []
        
        # Build character pool and ensure at least one of each required type
        if use_lowercase:
            chars = self.lowercase
            if exclude_ambiguous:
                chars = chars.replace('l', '').replace('o', '')
            character_pool += chars
            required_chars.append(secrets.choice(chars))
            
        if use_uppercase:
            chars = self.uppercase
            if exclude_ambiguous:
                chars = chars.replace('I', '').replace('O', '')
            character_pool += chars
            required_chars.append(secrets.choice(chars))
            
        if use_digits:
            chars = self.digits
            if exclude_ambiguous:
                chars = chars.replace('0', '').replace('1', '')
            character_pool += chars
            required_chars.append(secrets.choice(chars))
            
        if use_symbols:
            character_pool += self.punctuation
            required_chars.append(secrets.choice(self.punctuation))
            
        if not character_pool:
            raise ValueError("At least one character type must be selected")
            
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        password_chars = required_chars + [secrets.choice(character_pool) for _ in range(remaining_length)]
        
        # Shuffle the password to avoid predictable patterns
        secrets.SystemRandom().shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def generate_multiple_passwords(self, count: int = 5, **kwargs) -> List[str]:
        """Generate multiple passwords with the same criteria."""
        return [self.generate_password(**kwargs) for _ in range(count)]
    
    def check_password_strength(self, password: str) -> dict:
        """
        Analyze password strength and provide feedback.
        
        Returns:
            Dictionary with strength analysis
        """
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long")
            
        # Character variety checks
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in self.punctuation for c in password)
        
        variety_count = sum([has_lower, has_upper, has_digit, has_symbol])
        score += variety_count
        
        if not has_lower:
            feedback.append("Add lowercase letters")
        if not has_upper:
            feedback.append("Add uppercase letters")
        if not has_digit:
            feedback.append("Add numbers")
        if not has_symbol:
            feedback.append("Add special symbols")
            
        # Determine strength level
        if score >= 6:
            strength = "Very Strong"
        elif score >= 4:
            strength = "Strong"
        elif score >= 2:
            strength = "Moderate"
        else:
            strength = "Weak"
            
        return {
            'strength': strength,
            'score': score,
            'max_score': 6,
            'feedback': feedback,
            'length': len(password),
            'has_lowercase': has_lower,
            'has_uppercase': has_upper,
            'has_digits': has_digit,
            'has_symbols': has_symbol
        }


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("         SECURE PASSWORD GENERATOR")
    print("="*50)
    print("1. Generate a single password")
    print("2. Generate multiple passwords")
    print("3. Check password strength")
    print("4. Custom password generation")
    print("5. Exit")
    print("="*50)


def get_password_preferences():
    """Get user preferences for password generation."""
    print("\nPassword Generation Options:")
    
    while True:
        try:
            length = int(input("Password length (4-128, default 12): ") or "12")
            if 4 <= length <= 128:
                break
            else:
                print("Length must be between 4 and 128")
        except ValueError:
            print("Please enter a valid number")
    
    use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
    use_lowercase = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
    use_digits = input("Include numbers? (y/n, default y): ").lower() != 'n'
    use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
    exclude_ambiguous = input("Exclude ambiguous characters (0, O, l, 1)? (y/n, default n): ").lower() == 'y'
    
    return {
        'length': length,
        'use_uppercase': use_uppercase,
        'use_lowercase': use_lowercase,
        'use_digits': use_digits,
        'use_symbols': use_symbols,
        'exclude_ambiguous': exclude_ambiguous
    }


def main():
    """Main program loop."""
    generator = PasswordGenerator()
    
    print("Welcome to the Secure Password Generator!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                password = generator.generate_password()
                print(f"\nGenerated Password: {password}")
                
                # Show strength analysis
                strength = generator.check_password_strength(password)
                print(f"Password Strength: {strength['strength']} ({strength['score']}/{strength['max_score']})")
                
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            try:
                count = int(input("How many passwords to generate (1-20, default 5): ") or "5")
                if not 1 <= count <= 20:
                    print("Count must be between 1 and 20")
                    continue
                    
                passwords = generator.generate_multiple_passwords(count)
                print(f"\n{count} Generated Passwords:")
                for i, pwd in enumerate(passwords, 1):
                    print(f"{i:2d}. {pwd}")
                    
            except ValueError:
                print("Please enter a valid number")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            password = input("Enter password to check: ")
            if password:
                strength = generator.check_password_strength(password)
                print(f"\nPassword Analysis:")
                print(f"Strength: {strength['strength']} ({strength['score']}/{strength['max_score']})")
                print(f"Length: {strength['length']} characters")
                print(f"Contains lowercase: {'✓' if strength['has_lowercase'] else '✗'}")
                print(f"Contains uppercase: {'✓' if strength['has_uppercase'] else '✗'}")
                print(f"Contains digits: {'✓' if strength['has_digits'] else '✗'}")
                print(f"Contains symbols: {'✓' if strength['has_symbols'] else '✗'}")
                
                if strength['feedback']:
                    print("\nSuggestions for improvement:")
                    for suggestion in strength['feedback']:
                        print(f"• {suggestion}")
            else:
                print("No password entered")
                
        elif choice == '4':
            try:
                preferences = get_password_preferences()
                password = generator.generate_password(**preferences)
                print(f"\nCustom Generated Password: {password}")
                
                strength = generator.check_password_strength(password)
                print(f"Password Strength: {strength['strength']} ({strength['score']}/{strength['max_score']})")
                
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '5':
            print("\nThank you for using the Secure Password Generator!")
            print("Stay secure! 🔒")
            break
            
        else:
            print("Invalid choice. Please select 1-5.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()