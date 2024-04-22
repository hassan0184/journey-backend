from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


from journey.models import (
    Obstacles,
    UserChallenges,
    Quests,
    QuestRequests,
    UserChallengeQuestObstacles,
)


class ObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacles
        fields = (
            "id",
            "label",
            "description",
            "threat_type",
            "threat_level",
            "image",
            "is_custom",
        )


class CreateCustomObstacleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = Base64ImageField(required=True)

    class Meta:
        model = Obstacles
        fields = (
            "label",
            "description",
            "quest",
            "threat_type",
            "threat_level",
            "image",
            "user",
        )


class UserChallengeQuestObstaclesSerializer(serializers.ModelSerializer):
    obstacle = ObstacleSerializer()

    class Meta:
        model = UserChallengeQuestObstacles
        fields = ("id", "obstacle", "obstacle_progress")
