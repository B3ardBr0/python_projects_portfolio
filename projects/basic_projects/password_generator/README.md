# Password Generator

A secure password generator with customizable options for creating strong, cryptographically secure passwords.

## Features

- **Secure Generation**: Uses Python's `secrets` module for cryptographically secure randomness
- **Customizable Options**: 
  - Adjustable password length (4-128 characters)
  - Toggle uppercase/lowercase letters, numbers, and symbols
  - Option to exclude ambiguous characters (0, O, l, 1, etc.)
- **Password Strength Analysis**: Built-in password strength checker with feedback
- **Multiple Password Generation**: Generate multiple passwords at once
- **Interactive Menu**: Easy-to-use command-line interface

## Usage

### Basic Usage

```bash
python password_generator.py
```

### Menu Options

1. **Generate a single password** - Quick password generation with default settings
2. **Generate multiple passwords** - Create multiple passwords (up to 20)
3. **Check password strength** - Analyze any password for strength and get improvement suggestions
4. **Custom password generation** - Full customization of password criteria
5. **Exit** - Close the program

### Example Password Generation

Default password (12 characters, all character types):
```
Generated Password: K#9mP$2nQ!vX
Password Strength: Very Strong (6/6)
```

Custom password with specific requirements:
```
Password length: 16
Include symbols: No
Generated Password: B7kD9mL2nP4qR8sT
```

## Password Strength Criteria

The strength checker evaluates passwords based on:
- **Length**: 8+ characters (good), 12+ characters (excellent)
- **Character Variety**: Uppercase, lowercase, numbers, symbols
- **Overall Score**: 0-6 scale

**Strength Levels**:
- Very Strong (6/6): All criteria met
- Strong (4-5/6): Most criteria met
- Moderate (2-3/6): Basic requirements
- Weak (0-1/6): Insufficient complexity

## Security Features

- Uses `secrets.SystemRandom()` for cryptographically secure random generation
- Ensures at least one character from each selected character set
- Shuffles password characters to avoid predictable patterns
- No password storage or logging

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Example Output

```
==================================================
         SECURE PASSWORD GENERATOR
==================================================

Generated Password: 9$kL#mN2pQ!vX8
Password Strength: Very Strong (6/6)

Password Analysis:
Strength: Very Strong (6/6)
Length: 13 characters
Contains lowercase: ✓
Contains uppercase: ✓
Contains digits: ✓
Contains symbols: ✓
```