from django.conf import settings
from django.utils import timezone

from common.services.send_email import send_email


def send_invite_email_to_ally(ally):
    try:
        from_email = settings.FROM_EMAIL
        subject = "Ally Request for Journey App"
        to_email = ally.email
        invited_by = ally.invited_by.email
        content = ""
        html_content = (
            f"<strong>Hello {ally.name}</strong>, <br> <br>"
            f"You've been invited by your friend, {invited_by}, to join the Journey app. "
            f"He's counting on your support as we embark on thrilling quests and challenges together."
            f"Let's unite forces and achieve greatness! Join us on the app using the code <b>{ally.invite_code}</b><br>"
            f"Vast Journey Team."
        )
        send_email(from_email, to_email, subject, content, html_content)
        now = timezone.now()
        ally.invite_sent = True
        ally.invite_sent_at = now
        ally.save()
        return True
    except Exception as e:
        return False
