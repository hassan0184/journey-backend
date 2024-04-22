from django.contrib import admin
from journey.models import *

# Register your models here.


@admin.register(RoleType)
class RoleTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(HeroTypes)
class HeroTypesTypesAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "role_type", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(RecommendationType)
class RecommendationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Challenges)
class ChallengesAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("age_group", "ethnicity")


@admin.register(ChallengeRequest)
class ChallengeRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "challenge_info", "is_attended", "user")
    ordering = ("-created_at",)
    list_filter = ("is_attended",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(UserChallenges)
class UserChallengesAdmin(admin.ModelAdmin):
    list_display = ("id", "role_type", "hero_age", "user")
    ordering = ("-created_at",)
    list_filter = ("is_challenge_achieved",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(OutcomeItems)
class OutcomeItemsAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(QuestTypes)
class QuestTypesAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(QuestTraits)
class QuestTraitsAdmin(admin.ModelAdmin):
    list_display = ("id", "virtue", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(QuestRequests)
class QuestRequestsAdmin(admin.ModelAdmin):
    list_display = ("id", "quest_info", "is_attended", "user")
    ordering = ("-created_at",)
    list_filter = ("is_attended",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


class ObstacleInline(admin.StackedInline):
    model = Obstacles
    fk_name = "quest"
    extra = 1
    min_num = 1
    readonly_fields = ("created_by", "updated_by", "is_custom", "user")
    # exclude = ("created_by", "updated_by", "is_custom", "user")


class PowerupInline(admin.StackedInline):
    model = PowerUps
    fk_name = "quest"
    extra = 1
    min_num = 1
    readonly_fields = ("created_by", "updated_by", "is_custom", "user")


@admin.register(Obstacles)
class ObstaclesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "label",
        "threat_type",
        "threat_level",
        "quest",
        "is_custom",
    )
    ordering = ("-created_at",)
    list_filter = ("threat_type", "threat_level", "is_custom", "quest")
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(PowerUps)
class PowerUpsAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "powerup_type", "quest", "is_custom")
    ordering = ("-created_at",)
    list_filter = ("powerup_type", "is_custom", "quest")
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Quests)
class QuestsAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active", "is_custom", "challenge")
    ordering = ("-created_at",)
    list_filter = ("is_active", "is_custom")
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")
    inlines = [ObstacleInline, PowerupInline]


@admin.register(UserChallengeRecommendationType)
class UserChallengeRecommendationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "user_challenge", "recommendation_type")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")


@admin.register(JourneyMedia)
class JourneyMediaAdmin(admin.ModelAdmin):
    list_display = ("id", "media_type", "title")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")


@admin.register(Allies)
class AlliesAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "invited_by")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")


@admin.register(AlliesQuests)
class AlliesQuestsAdmin(admin.ModelAdmin):
    list_display = ("id", "ally", "user_quests")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")
