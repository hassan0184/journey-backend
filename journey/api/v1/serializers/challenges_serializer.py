from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from journey.api.v1.serializers.quests_serializer import UserChallengeQuestsSerializer
from journey.models import (
    Challenges,
    UserChallenges,
    ChallengeRequest,
    UserChallengeRecommendationType,
    RecommendationType,
    RoleType,
)
from users.enums import HeroType


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = ("id", "label")


class ChallengeRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = ChallengeRequest
        fields = ("id", "challenge_info", "email")


class CreateUserChallengeSerializer(serializers.ModelSerializer):
    role_type = serializers.PrimaryKeyRelatedField(
        queryset=RoleType.objects.all(), required=True
    )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    recommendation_type = serializers.PrimaryKeyRelatedField(
        many=True, queryset=RecommendationType.objects.filter(is_active=True)
    )

    class Meta:
        model = UserChallenges
        exclude = ("created_by", "updated_by", "is_challenge_achieved")

    def validate(self, data):
        res = super(CreateUserChallengeSerializer, self).validate(data)
        role_type = data.get("role_type")
        hero_type = data.get("hero_type", None)
        if role_type.type == HeroType.mentor.value:
            if not hero_type or hero_type is None or hero_type == "":
                raise ValidationError("hero_type field can not be empty")
        return data

    def create(self, validated_data):
        recommendation_category = validated_data.pop("recommendation_type", [])
        role_type = validated_data.get("role_type")
        if role_type.type == HeroType.self.value:
            validated_data["hero_type"] = None
        with transaction.atomic():
            user_challenge = super(CreateUserChallengeSerializer, self).create(
                validated_data
            )

            for obj in recommendation_category:
                if not UserChallengeRecommendationType.objects.filter(
                    recommendation_type=obj,
                    user=self.context["request"].user,
                    user_challenge=user_challenge,
                ).exists():
                    UserChallengeRecommendationType.objects.create(
                        recommendation_type=obj,
                        user=self.context["request"].user,
                        user_challenge=user_challenge,
                    )
        return user_challenge


class UserChallengeSerializer(serializers.ModelSerializer):
    role_type = serializers.CharField(source="role_type.type")
    hero_type = serializers.SerializerMethodField()
    hero_gender = serializers.CharField(source="hero_gender.label")
    hero_ethnicity = serializers.CharField(source="hero_ethnicity.label")
    hero_challenge = serializers.CharField(source="hero_challenge.label")
    user = serializers.CharField(source="user.username")
    recommendation_type = serializers.SerializerMethodField()
    user_quests = serializers.SerializerMethodField()

    class Meta:
        model = UserChallenges
        exclude = ("created_by", "updated_by")

    def get_hero_type(self, obj):
        if obj.hero_type is not None:
            return obj.hero_type.label

    def get_recommendation_type(self, obj) -> list[str]:
        return UserChallengeRecommendationType.objects.filter(
            user=obj.user, user_challenge=obj
        ).values_list("recommendation_type__label", flat=True)

    def get_user_quests(self, obj):
        user_quests = obj.user_challenge_quests.all()
        quests_serializer = UserChallengeQuestsSerializer(user_quests, many=True)

        return quests_serializer.data
