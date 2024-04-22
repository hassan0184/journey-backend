import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from users.enums import HERO_TYPE_CHOICES


class User(AbstractUser):
    """
    Custom User Models
    """

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    ref_code = models.CharField(max_length=6, null=True, blank=True)
    ref_by = models.CharField(max_length=6, null=True, blank=True)
    terms_and_conditions_accepted = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    is_ally = models.BooleanField(default=False)
    onboarding_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.ref_code:
            self.ref_code = uuid.uuid4().hex[:6].upper()
            while type(self).objects.filter(ref_code=self.ref_code):
                self.ref_code = uuid.uuid4().hex[:6].upper()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class UserOTPVerification(models.Model):
    class Meta:
        verbose_name = "User OTP Verification"
        verbose_name_plural = "User OTP Verification"

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="account_verification_details"
    )
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    email_otp_created_at = models.DateTimeField(null=True, blank=True)
    email_otp_verified_at = models.DateTimeField(null=True, blank=True)
