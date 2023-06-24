import re
import datetime
import random
from datetime import timedelta

PASSWORD_EXPIRATION_DAYS = 14

def generate_otp():
    """Generate a randomized 3-digit OTP."""
    return str(random.randint(200, 999))


def is_password_expired(password_date):
    """Check if the password has expired based on the provided date."""
    expiration_date = password_date + timedelta(days=PASSWORD_EXPIRATION_DAYS)
    return datetime.now() > expiration_date


def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print(strength)

    generated_otp = generate_otp()
    print("Generated OTP:", generated_otp)

    otp = input("Enter the one-time password (OTP): ")
    if otp == generated_otp:
        print("OTP verified. Access granted.")

        password_date_str = input("Enter the date the password was last changed (YYYY-MM-DD): ")
        password_date = datetime.strptime(password_date_str, "%Y-%m-%d")
        if is_password_expired(password_date):
            print("Password has expired. Access denied.")
        else:
            print("Password is valid. Access granted.")
    else:
        print("Invalid OTP. Access denied.")



def check_password_strength(password):
    """
    Check if password is strong enough.
    Returns True if password is strong, False otherwise.
    """
    # Check password is at least 8 characters long, if not return password is weak
    if len(password) < 8:
        return False
    
    # Check password must contain at least one uppercase letter, if not return password is weak
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check password must contain at least one lowercase letter, if not return password is weak
    if not re.search(r'[a-z]', password):
        return False
    
    # Check password must contain at least one digit, if not return password is weak
    if not re.search(r'\d', password):
        return False
    
    # Password is strong
    return True

if __name__ == "__main__":
    main()
