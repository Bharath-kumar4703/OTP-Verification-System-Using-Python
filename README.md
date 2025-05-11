# OTP Verification System Using Python
Overview
The OTP Verification System is a Python-based application that generates and verifies One-Time Passwords (OTPs) sent via email. It features a simple graphical user interface (GUI) built using Tkinter, making it user-friendly and easy to navigate.

Features
OTP Generation: Generates a 6-digit OTP for verification.
Email Notification: Sends the OTP to the user's email address.
OTP Verification: Allows users to verify the OTP with limited attempts.
User-Friendly GUI: Built with Tkinter for an intuitive user experience.
Requirements
Python 3.x
Tkinter (comes pre-installed with Python)
Access to an SMTP server (e.g., Gmail)
Installation
Clone the repository:

git clone https://github.com/yourusername/otp-verification-system.git
cd otp-verification-system
Ensure you have the required libraries. You can install any missing libraries using pip:

pip install smtplib
Usage
Open a terminal and navigate to the project directory.
Run the application:
python otp_verification.py
Enter your email address and click "Send OTP" to receive the OTP.
Enter the received OTP in the provided field and click "Verify OTP".
Code Explanation
Generating OTP
The generate_otp function creates a random 6-digit OTP.

Sending OTP
The send_otp function sends the generated OTP to the specified email address using SMTP.

User Interface
The OTPApp class defines the GUI for the application. It includes:

Input fields for email and OTP.
Buttons to send and verify the OTP.
Verification Logic
Users have three attempts to enter the correct OTP. If the OTP is verified successfully, access is granted; otherwise, the user is informed of the remaining attempts.

Important Notes
Replace sender_email and sender_password in the send_otp function with your own email credentials.
Ensure that "Allow less secure apps" is enabled in your Gmail account settings to send emails.
Acknowledgments
Thanks to the Python community for their resources and support.
