import re

def password_checker(password):
    # Initialize strength criteria
    length_check = len(password) >= 8
    ucase_include = re.search(r'[A-Z]', password) is not None
    lcase_include = re.search(r'[a-z]', password) is not None
    number_check = re.search(r'\d', password) is not None
    specialchar_include = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate strength score
    score = sum([length_check, ucase_include, lcase_include, number_check, specialchar_include])

    # Feedback based on score
    if score == 5:
        return "Strong", score
    elif score == 4:
        return "Moderate", score
    elif score == 3:
        return "Weak", score
    else:
        return "Very Weak", score

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")
    
    strength, score = password_checker(password)
    
    print(f"Password Strength: {strength}")
    print(f"Score: {score}/5")
    
    # Detailed feedback
    print("\nDetailed Feedback:")
    if len(password) < 8:
        print("- Password is too short. Consider using at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        print("- Add uppercase letters to increase strength.")
    if not re.search(r'[a-z]', password):
        print("- Add lowercase letters to increase strength.")
    if not re.search(r'\d', password):
        print("- Add numbers to increase strength.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("- Add special characters to increase strength.")

if __name__ == "__main__":
    main()
