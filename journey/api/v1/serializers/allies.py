from django.db import transaction
from phonenumber_field.phonenumber import to_python
from phonenumber_field.validators import validate_international_phonenumber
from rest_framework import serializers

from common.messages import (
    PHONE_OR_EMAIL_REQUIRED,
    ALLY_INVITATION_ALREADY_SENT_PHONE,
    ALLY_INVITATION_ALREADY_SENT_EMAIL,
)
from journey.api.v1.serializers.quests_serializer import UserChallengeQuestsSerializer
from journey.models import UserChallengeQuests
from journey.models.allies import Allies, AlliesQuests


class InviteAllySerializer(serializers.ModelSerializer):
    invited_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    phone_number = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    user_challenge_quests = serializers.PrimaryKeyRelatedField(
        queryset=UserChallengeQuests.objects.all(), many=True
    )

    class Meta:
        model = Allies
        fields = (
            "id",
            "name",
            "email",
            "phone_number",
            "superpower",
            "relationship",
            "user_challenge_quests",
            "invited_by",
        )

    def validate(self, attrs):
        res = super(InviteAllySerializer, self).validate(attrs)
        email = attrs.get("email")
        invited_by = attrs.get("invited_by")
        phone_number = attrs.get("phone_number")
        user_quests = attrs.get("user_challenge_quests")

        if not email:
            if phone_number:
                validate_international_phonenumber(phone_number)
                phone_number_with_countrycode = to_python(phone_number)
                if Allies.objects.filter(
                    phone_number=phone_number_with_countrycode, invited_by=invited_by
                ).exists():
                    raise serializers.ValidationError(
                        ALLY_INVITATION_ALREADY_SENT_PHONE
                    )
            else:
                raise serializers.ValidationError(PHONE_OR_EMAIL_REQUIRED)
        else:
            ally = Allies.objects.filter(email=email, invited_by=invited_by)
            if (
                ally.exists()
                and AlliesQuests.objects.filter(user_quests__in=user_quests).exists()
            ):
                raise serializers.ValidationError(ALLY_INVITATION_ALREADY_SENT_EMAIL)
        return attrs

    def create(self, validated_data):
        user_quests = validated_data.pop("user_challenge_quests")
        with transaction.atomic():
            invite = super(InviteAllySerializer, self).create(validated_data)

            for u_quests in user_quests:
                if not AlliesQuests.objects.filter(
                    ally=invite,
                    user_quests=u_quests,
                ).exists():
                    AlliesQuests.objects.create(ally=invite, user_quests=u_quests)

        return invite


class AllyQuestsSerializer(serializers.ModelSerializer):
    invited_by = serializers.SerializerMethodField()
    user_quests = UserChallengeQuestsSerializer()

    class Meta:
        model = AlliesQuests
        fields = ("id", "invited_by", "user_quests")

    def get_invited_by(self, obj):
        return obj.ally.invited_by.full_name
