from django.db import models
from django.contrib.postgres.fields import ArrayField
from treebeard.mp_tree import MP_Node
from common.models import BaseModel, AgeGroup
from .enums import (
    MEDIA_TYPE_CHOICES,
    MEDIA_FORMAT_CHOICES,
    MediaType,
    MEDIA_CREDIT_ROLE_CHOICES,
    SOURCE_TYPE_CHOICES,
    GENRE_APPLICABLE_FORMAT_CHOICES,
    MEDIA_O_TYPES_CHOICES,
    MEDIA_PROGRESS_CHOICES,
    MEDIA_STATUS_CHOICES,
    MEDIA_RATING_CHOICES,
)

# Create your models here.


class GroupCategory(BaseModel):
    class Meta:
        verbose_name = "Group Category"
        verbose_name_plural = "Group Categories"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Groups(MP_Node):
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        GroupCategory,
        on_delete=models.CASCADE,
        related_name="groups",
        null=True,
        blank=True,
    )

    node_order_by = ["name"]

    def __str__(self):
        return self.name


class CharacterTraits(BaseModel):
    class Meta:
        verbose_name = "Character Trait"
        verbose_name_plural = "Character Traits"

    label = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.label


class Characters(BaseModel):
    class Meta:
        verbose_name = "Characters"
        verbose_name_plural = "Characters"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    traits = models.ManyToManyField(
        CharacterTraits, related_name="media_characters", blank=True
    )
    image = models.ImageField(
        upload_to="discovery/media/characters/", null=True, blank=True
    )
    o_type = models.CharField(
        max_length=50,
        choices=MEDIA_O_TYPES_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this character real or fictional?",
    )
    groups = models.ManyToManyField(
        Groups, related_name="character_groups", null=True, blank=True
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Places(BaseModel):
    class Meta:
        verbose_name = "Places"
        verbose_name_plural = "Places"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/places/", null=True, blank=True
    )
    o_type = models.CharField(
        max_length=100,
        choices=MEDIA_O_TYPES_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this place real or fictional?",
    )
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    groups = models.ManyToManyField(
        Groups, related_name="place_groups", null=True, blank=True
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Items(BaseModel):
    class Meta:
        verbose_name = "Items"
        verbose_name_plural = "Items"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="discovery/media/items/", null=True, blank=True)
    o_type = models.CharField(
        max_length=50,
        choices=MEDIA_O_TYPES_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this item real or fictional?",
    )
    groups = models.ManyToManyField(
        Groups, related_name="item_groups", null=True, blank=True
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Themes(BaseModel):
    class Meta:
        verbose_name = "Themes"
        verbose_name_plural = "Themes"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/themes/", null=True, blank=True
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Topics(BaseModel):
    class Meta:
        verbose_name = "Topics"
        verbose_name_plural = "Topics"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/topics/", null=True, blank=True
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class TimePeriods(BaseModel):
    class Meta:
        verbose_name = "Time Periods"
        verbose_name_plural = "Time Periods"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/time_periods/", null=True, blank=True
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Genres(BaseModel):
    class Meta:
        verbose_name = "Genres"
        verbose_name_plural = "Genres"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/genres/", null=True, blank=True
    )
    applicable_formats = ArrayField(
        models.CharField(max_length=50, choices=GENRE_APPLICABLE_FORMAT_CHOICES),
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Activity(BaseModel):
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activity"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/activity/", null=True, blank=True
    )
    no_of_participants = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class ActivityPlace(BaseModel):
    class Meta:
        verbose_name = "Activity Place"
        verbose_name_plural = "Activity Places"

    place_activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="activity_places"
    )
    place = models.ForeignKey(
        Places, on_delete=models.CASCADE, related_name="activity_places"
    )

    def __str__(self):
        return f"{self.place_activity.name}, {self.place.name}"


class CareerInterests(BaseModel):
    class Meta:
        verbose_name = "Career Interest"
        verbose_name_plural = "Career Interests"

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/career/", null=True, blank=True
    )
    link = models.URLField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class PurchaseOppurtunities(BaseModel):
    class Meta:
        verbose_name = "Purchase Oppurtunity"
        verbose_name_plural = "Purchase Oppurtunities"

    name = models.CharField(max_length=200)
    link = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/purchase/", null=True, blank=True
    )
    active = models.BooleanField(default=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class MediaCredits(BaseModel):
    class Meta:
        verbose_name = "Media Credits"
        verbose_name_plural = "Media Credits"

    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, choices=MEDIA_CREDIT_ROLE_CHOICES)
    summary = models.TextField(null=True, blank=True)
    summary_link = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        upload_to="discovery/media/credits/", null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}, {self.role}"


class Media(BaseModel):
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

    media_type = models.CharField(
        choices=MEDIA_TYPE_CHOICES, max_length=50, default=MediaType.book.value
    )
    o_type = models.CharField(
        max_length=50,
        choices=MEDIA_O_TYPES_CHOICES,
        null=True,
        blank=True,
        verbose_name="Fiction or Non-fiction?",
    )
    stub = models.BooleanField(default=False)
    title = models.CharField(max_length=500)
    summary = models.TextField(null=True, blank=True)
    summary_link = models.URLField(max_length=500, null=True, blank=True)
    origin = models.IntegerField(blank=True, null=True)
    target_audience = models.ManyToManyField(
        AgeGroup, related_name="media_target_audience", blank=True
    )
    active = models.BooleanField(default=False)
    link = models.URLField(max_length=500, null=True, blank=True)
    cover_image = models.ImageField(upload_to="discovery/media/", null=True, blank=True)
    format = models.CharField(
        max_length=50, choices=MEDIA_FORMAT_CHOICES, null=True, blank=True
    )
    groups = models.ManyToManyField(Groups, related_name="media_groups", blank=True)
    mongo_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class MediaPurchaseOppurtunity(BaseModel):
    class Meta:
        verbose_name = "Media Purchase Oppurtunity"
        verbose_name_plural = "Media Purchase Oppurtunities"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_purchase_oppurtunities"
    )
    purchase_oppurtunity = models.ForeignKey(
        PurchaseOppurtunities,
        on_delete=models.CASCADE,
        related_name="media_purchase_oppurtunities",
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.purchase_oppurtunity.name}"


class MediaCareerInterest(BaseModel):
    class Meta:
        verbose_name = "Media Career Interest"
        verbose_name_plural = "Media Career Interests"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_career_interests"
    )
    career_interest = models.ForeignKey(
        CareerInterests, on_delete=models.CASCADE, related_name="media_career_interests"
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.career_interest.name}"


class MediaActivity(BaseModel):
    class Meta:
        verbose_name = "Media Activity"
        verbose_name_plural = "Media Activities"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_activities"
    )
    media_activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="media_activities"
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.media_activity.name}"


class RelatedMedia(BaseModel):
    class Meta:
        verbose_name = "Related Media"
        verbose_name_plural = "Related Media"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="discovery_related_media"
    )
    related_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="related_media"
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.related_media.title}"


class MediaGenre(BaseModel):
    class Meta:
        verbose_name = "Media Genre"
        verbose_name_plural = "Media Genres"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_genres"
    )
    genre = models.ForeignKey(
        Genres, on_delete=models.CASCADE, related_name="media_genres"
    )
    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this genre mentioned in this media or native to this media?",
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.genre.name}"


class MediaTimePeriod(BaseModel):
    class Meta:
        verbose_name = "Media Time Period"
        verbose_name_plural = "Media Time Periods"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_time_periods"
    )
    time_period = models.ForeignKey(
        TimePeriods, on_delete=models.CASCADE, related_name="media_time_periods"
    )
    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this time period mentioned in this media or native to this media?",
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.time_period.name}"


class MediaTopic(BaseModel):
    class Meta:
        verbose_name = "Media Topic"
        verbose_name_plural = "Media Topics"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_topics"
    )
    topic = models.ForeignKey(
        Topics, on_delete=models.CASCADE, related_name="media_topics"
    )
    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this topic mentioned in this media or native to this media?",
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.topic.name}"


class MediaTheme(BaseModel):
    class Meta:
        verbose_name = "Media Theme"
        verbose_name_plural = "Media Themes"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_themes"
    )
    theme = models.ForeignKey(
        Themes, on_delete=models.CASCADE, related_name="media_themes"
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.theme.name}"


class MediaItem(BaseModel):
    class Meta:
        verbose_name = "Media Item"
        verbose_name_plural = "Media Items"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_items"
    )
    item = models.ForeignKey(
        Items, on_delete=models.CASCADE, related_name="media_items"
    )
    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this item mentioned in this media or native to this media?",
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.item.name}"


class MediaPlace(BaseModel):
    class Meta:
        verbose_name = "Media Place"
        verbose_name_plural = "Media Places"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_places"
    )
    place = models.ForeignKey(
        Places, on_delete=models.CASCADE, related_name="media_places"
    )
    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this place mentioned in this media or native to this media?",
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.place.name}"


class MediaCharacter(BaseModel):
    class Meta:
        verbose_name = "Media Character"
        verbose_name_plural = "Media Characters"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_characters"
    )
    character = models.ForeignKey(
        Characters, on_delete=models.CASCADE, related_name="media_characters"
    )
    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name="Is this character mentioned in this media or native to this media?",
    )

    def __str__(self):
        return f"{self.discovery_media.title}, {self.character.name}"


class MediaCreditsReference(BaseModel):
    class Meta:
        verbose_name = "Media Credits Reference"
        verbose_name_plural = "Media Credits References"

    media_credit = models.ForeignKey(
        MediaCredits, on_delete=models.CASCADE, related_name="media_credits"
    )
    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_credits"
    )

    def __str__(self):
        return f"{self.media_credit.name}, {self.discovery_media.title}"


class Reviews(BaseModel):
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    review = models.TextField(null=True, blank=True)
    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_reviews"
    )


class Quotes(BaseModel):
    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    quote = models.TextField(null=True, blank=True)
    said_by = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_quotes"
    )


class MediaIdentifier(BaseModel):
    class Meta:
        verbose_name = "Media Identifier"
        verbose_name_plural = "Media Identifiers"

    identifier = models.CharField(max_length=200, unique=True)
    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media_identifiers"
    )

    def __str__(self):
        return self.identifier


class AdditionalResource(BaseModel):
    class Meta:
        verbose_name = "Additional Resource"
        verbose_name_plural = "Additional Resources"

    link = models.URLField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    discovery_media = models.ForeignKey(
        Media,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    media_credit = models.ForeignKey(
        MediaCredits,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    character = models.ForeignKey(
        Characters,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    place = models.ForeignKey(
        Places,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    theme = models.ForeignKey(
        Themes,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    topic = models.ForeignKey(
        Topics,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    time_period = models.ForeignKey(
        TimePeriods,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    genre = models.ForeignKey(
        Genres,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    item = models.ForeignKey(
        Items,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )
    career = models.ForeignKey(
        CareerInterests,
        on_delete=models.CASCADE,
        related_name="additional_resources",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.link


class UserExperience(BaseModel):
    class Meta:
        verbose_name = "User Experience"
        verbose_name_plural = "User Experiences"

    discovery_media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="user_experiences"
    )
    progress = models.CharField(
        max_length=100, choices=MEDIA_PROGRESS_CHOICES, null=True, blank=True
    )
    status = models.CharField(
        max_length=100, choices=MEDIA_STATUS_CHOICES, null=True, blank=True
    )
    rating = models.CharField(
        max_length=1, choices=MEDIA_RATING_CHOICES, null=True, blank=True
    )
    can_lend = models.BooleanField(default=False)
