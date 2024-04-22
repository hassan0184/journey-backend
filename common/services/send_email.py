from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def send_email(from_email, to_email, subject, content, html_content):
    if settings.DISABLE_OTP:
        return True
    try:
        email = EmailMultiAlternatives(subject, content, from_email, [to_email])
        email.attach_alternative(html_content, "text/html")
        email.send()
        return True
    except Exception as e:
        return False
