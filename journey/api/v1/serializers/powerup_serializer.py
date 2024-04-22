from django.db import transaction
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from journey.models import (
    PowerUps,
    UserChallengeQuestPowerups,
)


class PowerUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerUps
        fields = (
            "id",
            "label",
            "description",
            "powerup_type",
            "image",
            "is_custom",
            "quest",
        )


class CreateCustomPowerUpSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = Base64ImageField(required=True)

    class Meta:
        model = PowerUps
        fields = ("label", "description", "quest", "powerup_type", "image", "user")


class UserChallengeQuestPowerupsSerializer(serializers.ModelSerializer):
    powerup = PowerUpSerializer()

    class Meta:
        model = UserChallengeQuestPowerups
        fields = ("id", "powerup", "powerup_progress")
