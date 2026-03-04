"""
utils.py
"""

# ============================================================
# IMPORTS
# ============================================================

import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password


# ============================================================
# OTP UTILITIES
# ============================================================

def generate_otp():
    return str(random.randint(100000, 999999))

def hash_otp(otp):
    return make_password(otp)

def send_otp_email(email, otp):
    subject = "Email Verification OTP"
    message = f"Your OTP is {otp}. It expires in 10 minutes."
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
This module provides OTP (One-Time Password) utility functions
for email verification.

It handles:
    - Generating a 6-digit OTP
    - Hashing the OTP for secure storage
    - Sending the OTP to the user via email


IMPORTS
-------
- random            : Used to generate a random 6-digit number.
- send_mail         : Django utility for sending emails.
- settings          : Accesses project-level settings like EMAIL_HOST_USER.
- make_password     : Hashes the OTP before storing it securely.


FUNCTION: generate_otp()
-------------------------
Generates a random 6-digit OTP as a string.
Range: 100000 to 999999 ensures it is always 6 digits.


FUNCTION: hash_otp(otp)
------------------------
Hashes the OTP using Django's make_password.
Store this hash in the database, never the raw OTP.


FUNCTION: send_otp_email(email, otp)
-------------------------------------
Sends the raw OTP to the user's email address.

Subject : "Email Verification OTP"
Message : Includes OTP and expiry notice (10 minutes).
Sender  : Pulled from settings.EMAIL_HOST_USER.
Receiver: The email address passed as argument.
fail_silently=False: Raises an error if email sending fails.


IMPORTANT POINTS TO REMEMBER
------------------------------
1. Always store the HASHED OTP in the database.
   Never store the raw OTP.

2. Always set an expiry time for OTPs.
   Store the creation timestamp alongside the hash.

3. fail_silently=False is recommended during development.
   For production, handle email errors gracefully.

4. Ensure EMAIL_HOST_USER and email backend settings
   are properly configured in settings.py.

5. For production systems:
   Consider using Celery to send emails asynchronously
   so the user is not kept waiting.
"""