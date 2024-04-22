from django.db import transaction
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from journey.api.v1.serializers.obstacle_serializer import (
    ObstacleSerializer,
    UserChallengeQuestObstaclesSerializer,
)
from journey.api.v1.serializers.powerup_serializer import (
    PowerUpSerializer,
    UserChallengeQuestPowerupsSerializer,
)
from journey.models import (
    UserChallenges,
    Quests,
    QuestRequests,
    UserChallengeQuests,
    Obstacles,
    PowerUps,
    UserChallengeQuestObstacles,
    UserChallengeQuestPowerups,
)


class GetChallengeQueststSerializer(serializers.ModelSerializer):
    obstacles = serializers.SerializerMethodField()
    powerups = serializers.SerializerMethodField()

    class Meta:
        model = Quests
        fields = (
            "id",
            "label",
            "objective",
            "reward",
            "image",
            "desired_outcome",
            "success_rule",
            "obstacles",
            "powerups",
        )

    def get_obstacles(self, obj):
        user = self.context.get("user")
        q = Q(user__isnull=True) | Q(user=user)
        obstacles = obj.obstacles.all().filter(q)
        return ObstacleSerializer(obstacles, many=True).data

    def get_powerups(self, obj):
        user = self.context.get("user")
        q = Q(user__isnull=True) | Q(user=user)
        powerups = obj.powerups.all().filter(q)
        return PowerUpSerializer(powerups, many=True).data


class QuestsRequestSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_challenge = serializers.PrimaryKeyRelatedField(
        queryset=UserChallenges.objects.all(), required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        # Filter the queryset for primary key related field based on the current user if initializing through request

        if not request:
            self.fields["user_challenge"].queryset = UserChallenges.objects.all()
        else:
            self.user = request.user
            self.fields["user_challenge"].queryset = UserChallenges.objects.filter(
                user=self.user
            )

    class Meta:
        model = QuestRequests
        fields = ("id", "quest_info", "user_challenge", "user")


class SetQuestsSerializerWithSubData(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Quests.objects.filter(is_active=True)
    )
    obstacles = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=Obstacles.objects.filter(is_active=True)
        )
    )
    powerups = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=PowerUps.objects.filter(is_active=True)
        )
    )

    class Meta:
        model = Quests
        fields = ("id", "obstacles", "powerups")

    def validate(self, data):
        res = super(SetQuestsSerializerWithSubData, self).validate(data)
        quest = data.get("id")
        obstacles = data.get("obstacles")
        powerups = data.get("powerups")
        challenge_id = self.context.get("challenge_id")
        if challenge_id:
            if not quest.challenge_id == challenge_id:
                raise ValidationError("Invalid Quest.")

        quest_obstacles_ids = Obstacles.objects.filter(quest=quest).values_list(
            "id", flat=True
        )
        quest_powerUp_ids = PowerUps.objects.filter(quest=quest).values_list(
            "id", flat=True
        )

        for obstacle in obstacles:
            if obstacle.id not in quest_obstacles_ids:
                raise ValidationError("Invalid Obstacle Selected")
        for powerup in powerups:
            if powerup.id not in quest_powerUp_ids:
                raise ValidationError("Invalid Powerup Selected")

        return data


class AddUserQueststSerializer(serializers.ModelSerializer):
    user_challenge = serializers.PrimaryKeyRelatedField(
        queryset=UserChallenges.objects.all()
    )
    quests = SetQuestsSerializerWithSubData(many=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request:
            self.user = request.user
            self.fields["user_challenge"].queryset = UserChallenges.objects.filter(
                user=self.user
            )

    class Meta:
        model = UserChallengeQuests
        fields = ("user_challenge", "quests")

    def validate(self, data):
        res = super(AddUserQueststSerializer, self).validate(data)
        user_challenge = data.get("user_challenge")
        challenge_id = user_challenge.hero_challenge_id
        quests = data.get("quests")

        quests_ids = [di["id"].id for di in quests]
        before_len = len(quests_ids)
        after_len = len(list(set(quests_ids)))
        if not before_len == after_len:
            raise ValidationError("One Quest can not be selected more than once")
        q_serializer = SetQuestsSerializerWithSubData(
            data=quests, many=True, context={"challenge_id": challenge_id}
        )
        q_serializer.is_valid(raise_exception=True)
        return data

    def create(self, validated_data):
        with transaction.atomic():
            user_challenge = validated_data.get("user_challenge")
            quests = validated_data.get("quests")
            for quest_di in quests:
                quest = quest_di["id"]
                obstacles = quest_di.get("obstacles")
                obst_ids = [obstacle.id for obstacle in obstacles]
                obstacle_ids = list(set(obst_ids))
                powerups = quest_di.get("powerups")
                pow_ids = [powerup.id for powerup in powerups]
                powerups_ids = list(set(pow_ids))

                user_challenge_quest = UserChallengeQuests.objects.create(
                    user_challenge=user_challenge, quest=quest
                )
                for obst_id in obstacle_ids:
                    UserChallengeQuestObstacles.objects.create(
                        user_chellenge_quest=user_challenge_quest, obstacle_id=obst_id
                    )
                for pow_id in powerups_ids:
                    UserChallengeQuestPowerups.objects.create(
                        user_challenge_quest=user_challenge_quest, powerup_id=pow_id
                    )
        return user_challenge


class UserChallengeQuestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quests
        fields = ("id", "label", "objective", "reward", "image", "age_group", "types")


class UserChallengeQuestsSerializer(serializers.ModelSerializer):
    quest = UserChallengeQuestDetailsSerializer()
    quest_obstacles = serializers.SerializerMethodField()
    quest_powerups = serializers.SerializerMethodField()

    class Meta:
        model = UserChallengeQuests
        fields = (
            "id",
            "quest",
            "is_completed",
            "created_at",
            "quest_start_at",
            "quest_obstacles",
            "quest_powerups",
        )

    def get_quest_obstacles(self, obj):
        obstacles = UserChallengeQuestObstacles.objects.filter(user_chellenge_quest=obj)
        return UserChallengeQuestObstaclesSerializer(obstacles, many=True).data

    def get_quest_powerups(self, obj):
        powerups = UserChallengeQuestPowerups.objects.filter(user_challenge_quest=obj)
        return UserChallengeQuestPowerupsSerializer(powerups, many=True).data
