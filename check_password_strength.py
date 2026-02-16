import re, pyperclip

# Check length (at least 8 characters)
length_pattern = r'^.{8,}$'

# Check for at least one uppercase letter
uppercase_pattern = r'[A-Z]'

# Check for at least one lowercase letter
lowercase_pattern = r'[a-z]'

# Check for at least one digit
digit_pattern = r'\d'

def check_password_separate():
    password = pyperclip.paste()
    """Check password using separate regex patterns"""
    if not re.search(length_pattern, password):
        print("Password must be at least 8 characters long")
    if not re.search(uppercase_pattern, password):
        print("Password must contain at least one uppercase letter")
    if not re.search(lowercase_pattern, password):
        print("Password must contain at least one lowercase letter")
    if not re.search(digit_pattern, password):
        print("Password must contain at least one digit")
    if re.search(length_pattern, password) and re.search(uppercase_pattern, password) and re.search(lowercase_pattern, password) and re.search(digit_pattern, password):
        print("\"" + password + "\"", "is a strong password")
    input()

check_password_separate()

# 123456789wQ