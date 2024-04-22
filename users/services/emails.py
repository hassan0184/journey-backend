import math
import random
from django.conf import settings
from django.utils import timezone

from users.models import User, UserOTPVerification
from common.services.send_email import send_email


def generate_random_otp():
    if settings.DISABLE_OTP:
        return "0000"
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(4):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str


def send_acc_verification_email(user):
    try:
        from_email = settings.FROM_EMAIL
        subject = "Account Activation Email"
        to_email = user.email
        name = "Hello Journey Member"
        content = ""
        otp = generate_random_otp()
        html_content = (
            f"<strong>{name}</strong>, <br> <br>"
            f"Thank you for signing up with Journey App.<br>"
            f"In order to activate your account, please use OTP <b>{otp}</b>  <br> <br>"
            f"Vast Journey Team."
        )
        now = timezone.now()
        if not hasattr(user, "account_verification_details"):
            UserOTPVerification.objects.create(
                email_otp=otp, email_otp_created_at=now, user=user
            )
        else:
            account_verification_details = user.account_verification_details
            account_verification_details.email_otp = otp
            account_verification_details.email_otp_created_at = now
            account_verification_details.save()
        send_email(from_email, to_email, subject, content, html_content)
        return True
    except Exception as e:
        return False


def send_email_for_forgot_password(user):
    try:
        from_email = settings.FROM_EMAIL
        subject = "Password Reset Request"
        to_email = user.email
        name = "Hello Journey Member"
        content = ""
        otp = generate_random_otp()
        html_content = (
            f"<strong>{name}</strong>, <br> <br>"
            f"We received a request to reset the password associated with this Email address."
            f"You can reset your password using the code <b>{otp}</b><br>"
            f"If you did not request to have your password reset, you can safely ignore this email.<br><br>"
            f"Vast Journey Team."
        )
        now = timezone.now()

        if not hasattr(user, "account_verification_details"):
            UserOTPVerification.objects.update(
                email_otp=otp, email_otp_created_at=now, user=user
            )
        else:
            account_verification_details = user.account_verification_details
            account_verification_details.email_otp = otp
            account_verification_details.email_otp_created_at = now
            account_verification_details.email_otp_verified_at = None
            account_verification_details.save()
        send_email(from_email, to_email, subject, content, html_content)
        return True
    except Exception as e:
        return False
