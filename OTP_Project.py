import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time

def generate_otp():
    """Generates a random 6-digit OTP."""
    return random.randint(100000, 999999)

def send_otp(email_recipient, otp):
    """
    Simulates sending an OTP to the user's email.
    Connects to the email server and sends the OTP.
    """
    sender_email = "bb5037414@gmail.com"
    sender_password = "rqza ziai goqi wggr"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}. Please use this to verify your access."

    # Setting up the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email_recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("OTP sent successfully to the email!")
    except Exception as e:
        print(f"Failed to send OTP: {e}")
    finally:
        server.quit()

def get_user_otp_input():
    """Prompts the user to enter the OTP."""
    return input("Enter the OTP sent to your email: ").strip()

def validate_otp(generated_otp, entered_otp, retries=3):
    """
    Validates the OTP entered by the user.
    Allows the user to retry up to 'retries' times if the input is incorrect.
    """
    while retries > 0:
        if entered_otp == str(generated_otp):
            print("Access granted! OTP verified successfully.")
            return True
        else:
            retries -= 1
            if retries > 0:
                print(f"Incorrect OTP. You have {retries} attempts left.")
                entered_otp = get_user_otp_input()
            else:
                print("Access denied! Too many incorrect attempts.")
                return False

if _name_ == "_main_":
    print("Welcome to the OTP Verification System")

    # Step 1: Generate OTP
    otp = generate_otp()

    # Step 2: Send OTP
    recipient_email = input("Enter your email address: ").strip()
    send_otp(recipient_email, otp)

    # Step 3: Prompt user for OTP entry
    entered_otp = get_user_otp_input()

    # Step 4: Validate OTP
    validate_otp(otp, entered_otp)