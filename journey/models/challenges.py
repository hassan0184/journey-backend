from django.db import models

from discovery.models import Items
from journey.enums import (
    OBSTACLE_THREAT_TYPE_CHOICES,
    OBSTACLE_THREAT_LEVEL_CHOICES,
    POWER_UPS_TYPE_CHOICES,
    QUEST_CHALLENGE_REQUESTS_STATUS,
    QuestChallendeRequestStatus,
)
from journey.models.media import JourneyMedia
from users.models import User

# Create your models here.
from common.models import BaseModel, Ethnicity, Gender, AgeGroup
from journey.models import (
    RoleType,
    HeroTypes,
    RecommendationType,
)


class Challenges(BaseModel):
    class Meta:
        verbose_name = "Challenges"
        verbose_name_plural = "Challenges"

    label = models.CharField(max_length=50, unique=True)
    card_title = models.CharField(max_length=300, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    age_group = models.ManyToManyField(
        AgeGroup, related_name="age_group_challenges", blank=True
    )
    ethnicity = models.ManyToManyField(
        Ethnicity, related_name="ethnicity_challenges", blank=True
    )

    def __str__(self):
        return self.label


class ChallengeRequest(BaseModel):
    class Meta:
        verbose_name = "Challenge Request"
        verbose_name_plural = "Challenge Requests"

    challenge_info = models.CharField(max_length=150)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="challenge_requests",
        null=True,
        blank=True,
    )  # depricated
    email = models.EmailField(null=True, blank=True)
    is_attended = models.BooleanField(default=False)
    request_status = models.CharField(
        choices=QUEST_CHALLENGE_REQUESTS_STATUS,
        default=QuestChallendeRequestStatus.pending.value,
    )
    is_request_closed = models.BooleanField(default=False)


class UserChallenges(BaseModel):
    class Meta:
        verbose_name = "User Challenges"
        verbose_name_plural = "User Challenges"

    role_type = models.ForeignKey(
        RoleType, on_delete=models.PROTECT, related_name="role_challenge", null=True
    )
    hero_type = models.ForeignKey(
        HeroTypes,
        on_delete=models.PROTECT,
        related_name="hero_challenges",
        null=True,
        blank=True,
    )
    hero_age = models.IntegerField()
    hero_gender = models.ForeignKey(
        Gender, on_delete=models.PROTECT, related_name="hero_gender"
    )
    hero_ethnicity = models.ForeignKey(
        Ethnicity, on_delete=models.PROTECT, related_name="hero_ethnicity"
    )
    hero_extra_info = models.CharField(max_length=300, null=True, blank=True)
    hero_challenge = models.ForeignKey(
        Challenges, on_delete=models.PROTECT, related_name="hero_challenge"
    )
    is_challenge_achieved = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_challenges"
    )

    def __str__(self):
        return f"{self.user.email}, {self.hero_challenge.label}"


class OutcomeItems(BaseModel):
    class Meta:
        verbose_name = "Outcome Items"
        verbose_name_plural = "Outcome Items"

    label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class QuestTypes(BaseModel):
    class Meta:
        verbose_name = "Quest Types"
        verbose_name_plural = "Quest Types"

    label = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class QuestTraits(BaseModel):
    class Meta:
        verbose_name = "Quest Traits"
        verbose_name_plural = "Quest Traits"

    virtue = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.virtue}, {self.strength}"


class Quests(BaseModel):
    class Meta:
        verbose_name = "Quests"
        verbose_name_plural = "Quests"

    label = models.CharField(max_length=100)
    objective = models.CharField(max_length=300)
    reward = models.CharField(max_length=300)
    image = models.ImageField(upload_to="quests/")
    is_active = models.BooleanField(default=True)
    challenge = models.ForeignKey(
        Challenges, on_delete=models.CASCADE, related_name="quests"
    )
    age_group = models.ManyToManyField(
        AgeGroup, related_name="age_group_quests", blank=True
    )
    types = models.ManyToManyField(QuestTypes, related_name="quest_types", blank=True)
    media = models.ManyToManyField(
        JourneyMedia, related_name="journey_media_quests", blank=True
    )
    items_required = models.ManyToManyField(
        Items, related_name="quest_items_required", blank=True
    )
    desired_outcome = models.TextField(null=True, blank=True)
    traits = models.ManyToManyField(
        QuestTraits, related_name="quest_traits", blank=True
    )
    success_rule = models.TextField(null=True)
    items_to_be_used = models.ManyToManyField(OutcomeItems, blank=True)
    adult_content = models.BooleanField(default=False)
    # locations = models.CharField(max_length=100) # to be discussed
    is_custom = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="custom_quests",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.label


class QuestRequests(BaseModel):
    class Meta:
        verbose_name = "Quest RequestS"
        verbose_name_plural = "Quest Requests"

    quest_info = models.CharField(max_length=500)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="quests_requests"
    )
    user_challenge = models.ForeignKey(
        UserChallenges,
        on_delete=models.CASCADE,
        null=True,
        related_name="custom_quest_requests",
    )
    is_attended = models.BooleanField(default=False)
    request_status = models.CharField(
        choices=QUEST_CHALLENGE_REQUESTS_STATUS,
        default=QuestChallendeRequestStatus.pending.value,
    )
    is_request_closed = models.BooleanField(default=False)


class Obstacles(BaseModel):
    class Meta:
        verbose_name = "Obstacles"
        verbose_name_plural = "Obstacles"

    label = models.CharField(max_length=300)
    # name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    threat_type = models.CharField(choices=OBSTACLE_THREAT_TYPE_CHOICES, max_length=20)
    threat_level = models.IntegerField(
        choices=OBSTACLE_THREAT_LEVEL_CHOICES
    )  # difficulty
    image = models.ImageField(upload_to="obstacles/")
    is_active = models.BooleanField(default=True)
    quest = models.ForeignKey(
        Quests, on_delete=models.CASCADE, related_name="obstacles"
    )
    is_custom = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="custom_obstacles",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.label


class PowerUps(BaseModel):
    class Meta:
        verbose_name = "Power-Ups"
        verbose_name_plural = "Power-Ups"

    label = models.CharField(max_length=300)
    # name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    powerup_type = models.CharField(choices=POWER_UPS_TYPE_CHOICES, max_length=20)
    image = models.ImageField(upload_to="powerups/")
    is_active = models.BooleanField(default=True)
    quest = models.ForeignKey(Quests, on_delete=models.CASCADE, related_name="powerups")
    is_custom = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="custom_powerups",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.label


class UserChallengeRecommendationType(BaseModel):
    class Meta:
        verbose_name = "User Challenge Recommendation Types"
        verbose_name_plural = "User Challenge Recommendation Types"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_challenge_recommendation_types",
    )
    user_challenge = models.ForeignKey(
        UserChallenges,
        on_delete=models.CASCADE,
        related_name="challenge_recommendation_types",
    )
    recommendation_type = models.ForeignKey(
        RecommendationType,
        on_delete=models.CASCADE,
        related_name="recommendation_types",
    )


class UserChallengeQuests(BaseModel):
    class Meta:
        verbose_name = "User-Challenge Quests"
        verbose_name_plural = "User-Challenge Quests"
        unique_together = ["user_challenge", "quest"]

    user_challenge = models.ForeignKey(
        UserChallenges, on_delete=models.CASCADE, related_name="user_challenge_quests"
    )
    quest = models.ForeignKey(
        Quests, on_delete=models.CASCADE, related_name="user_challenge_quests"
    )
    is_completed = models.BooleanField(default=False)
    quest_start_at = models.DateTimeField(null=True)


class UserChallengeQuestObstacles(BaseModel):
    class Meta:
        verbose_name = "User-Challenge-Quests Obstacles"
        verbose_name_plural = "User-Challenge-Quests Obstacles"
        unique_together = ["user_chellenge_quest", "obstacle"]

    user_chellenge_quest = models.ForeignKey(
        UserChallengeQuests,
        on_delete=models.CASCADE,
        related_name="user_chellange_quest_obstacles",
    )
    obstacle = models.ForeignKey(
        Obstacles, on_delete=models.CASCADE, related_name="user_chellange_obstacles"
    )
    obstacle_progress = models.CharField(max_length=300, null=True)


class UserChallengeQuestPowerups(BaseModel):
    class Meta:
        verbose_name = "User-Challenge-Quests Powerups"
        verbose_name_plural = "User-Challenge-Quests Powerups"
        unique_together = ["user_challenge_quest", "powerup"]

    user_challenge_quest = models.ForeignKey(
        UserChallengeQuests,
        on_delete=models.CASCADE,
        related_name="user_chellange_quest_powerup",
    )
    powerup = models.ForeignKey(
        PowerUps, on_delete=models.CASCADE, related_name="user_chellange_powerup"
    )
    powerup_progress = models.CharField(max_length=300, null=True)
