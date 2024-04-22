import uuid

from django.db import models

from journey.models import UserChallengeQuests
from users.models import User
from common.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


class Allies(BaseModel):
    class Meta:
        verbose_name = "Allies"
        verbose_name_plural = "Allies"

    invited_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="allies", null=True
    )
    invite_code = models.CharField(max_length=6)  # unique invite code to identify user
    name = models.CharField(max_length=250)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    superpower = models.CharField(300)
    relationship = models.CharField(250)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_ally_details",
    )
    invite_sent = models.BooleanField(default=False)
    invite_sent_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invite_code and not self.user:
            self.invite_code = uuid.uuid4().hex[:6].upper()
            while type(self).objects.filter(invite_code=self.invite_code):
                self.invite_code = uuid.uuid4().hex[:6].upper()
        super(Allies, self).save(*args, **kwargs)


class AlliesQuests(BaseModel):
    class Meta:
        verbose_name = "Allies Quests"
        verbose_name_plural = "Allies Quests"

    ally = models.ForeignKey(
        Allies, on_delete=models.CASCADE, related_name="allies_quests"
    )
    user_quests = models.ForeignKey(
        UserChallengeQuests, on_delete=models.CASCADE, related_name="quest_allies"
    )
