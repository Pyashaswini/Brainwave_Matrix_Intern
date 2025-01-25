import re

def check_password_strength(password):
    """Check the strength of the provided password."""
    
    # Initialize criteria
    length_score = 0
    complexity_score = 0
    uniqueness_score = 0
    
    # Length criteria
    if len(password) < 8:
        length_score = 1
    elif len(password) <= 12:
        length_score = 2
    elif len(password) <= 16:
        length_score = 3
    elif len(password) <= 20:
        length_score = 4
    else:
        length_score = 5

    # Complexity criteria
    complexity_criteria = [
        bool(re.search(r'[A-Z]', password)),  # At least one uppercase letter
        bool(re.search(r'[a-z]', password)),  # At least one lowercase letter
        bool(re.search(r'[0-9]', password)),  # At least one digit
        bool(re.search(r'[\W_]', password))    # At least one special character
    ]
    
    complexity_score = sum(complexity_criteria)
    
    # Check for uniqueness against a common passwords list
    common_passwords = set([
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "qwerty", "abc123", "football", "monkey",
        "letmein", "iloveyou", "admin", "welcome", "123123",
        "1q2w3e4r", "sunshine", "qwertyuiop"
    ])
    
    uniqueness_score = 0 if password in common_passwords else 1
    
    # Calculate overall strength score (1 to 5)
    total_score = length_score + complexity_score + uniqueness_score
    
    # Determine strength level (1 to 5)
    if total_score <= 2:
        strength = 1  # Weak
    elif total_score <= 4:
        strength = 2  # Fair
    elif total_score <= 6:
        strength = 3  # Good
    elif total_score <= 8:
        strength = 4  # Strong
    else:
        strength = 5  # Very Strong
    
    return {
        'strength': strength,
        'length_score': length_score,
        'complexity_score': complexity_score,
        'uniqueness_score': uniqueness_score
    }

# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    result = check_password_strength(user_password)
    
    print(f"Password Strength Level: {result['strength']} (1=Weak, 5=Very Strong)")
    print(f"Length Score: {result['length_score']}")
    print(f"Complexity Score: {result['complexity_score']}")
    print(f"Uniqueness Score: {result['uniqueness_score']}")
