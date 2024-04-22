from django import forms
from django.contrib import admin
from discovery.models import (
    Media,
    MediaCredits,
    Characters,
    CharacterTraits,
    Places,
    Items,
    Themes,
    Topics,
    TimePeriods,
    Genres,
    Activity,
    CareerInterests,
    PurchaseOppurtunities,
    MediaIdentifier,
    AdditionalResource,
    Reviews,
    Quotes,
    GroupCategory,
    Groups,
    MediaCreditsReference,
    MediaCharacter,
    MediaPlace,
    MediaItem,
    MediaTheme,
    MediaTopic,
    MediaTimePeriod,
    MediaGenre,
    RelatedMedia,
    MediaActivity,
    MediaCareerInterest,
    MediaPurchaseOppurtunity,
    ActivityPlace,
    UserExperience,
)
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html, mark_safe
from .enums import GENRE_APPLICABLE_FORMAT_CHOICES
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


@admin.register(GroupCategory)
class GroupCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("-created_at",)
    search_fields = ("name",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Groups)
class GroupAdmin(TreeAdmin):
    form = movenodeform_factory(Groups)


@admin.register(CharacterTraits)
class CharacterTraitsAdmin(admin.ModelAdmin):
    list_display = ("label",)
    ordering = ("-created_at",)
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at")


class AdditionalResourceMediaInline(admin.StackedInline):
    verbose_name = "Media Additional Resource"
    verbose_name_plural = "Media Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "media_credit",
        "character",
        "place",
        "theme",
        "topic",
        "time_period",
        "genre",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "discovery_media"
    insert_after = "format"


class AdditionalResourceCreditInline(admin.StackedInline):
    verbose_name = "Media Credit Additional Resource"
    verbose_name_plural = "Media Credit Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "character",
        "place",
        "theme",
        "topic",
        "time_period",
        "genre",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "media_credit"


class AdditionalResourceCharacterInline(admin.StackedInline):
    verbose_name = "Media Character Additional Resource"
    verbose_name_plural = "Media Character Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "place",
        "theme",
        "topic",
        "time_period",
        "genre",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "character"


class AdditionalResourcePlaceInline(admin.StackedInline):
    verbose_name = "Media Place Additional Resource"
    verbose_name_plural = "Media Place Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "character",
        "theme",
        "topic",
        "time_period",
        "genre",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "place"


class AdditionalResourceThemeInline(admin.StackedInline):
    verbose_name = "Media Theme Additional Resource"
    verbose_name_plural = "Media Theme Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "character",
        "place",
        "topic",
        "time_period",
        "genre",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "theme"


class AdditionalResourceTopicInline(admin.StackedInline):
    verbose_name = "Media Topic Additional Resource"
    verbose_name_plural = "Media Topic Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "character",
        "place",
        "theme",
        "time_period",
        "genre",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "topic"


class AdditionalResourceTimePeriodInline(admin.StackedInline):
    verbose_name = "Media Time Period Additional Resource"
    verbose_name_plural = "Media Time Period Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "character",
        "place",
        "theme",
        "topic",
        "genre",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "time_period"


class AdditionalResourceGenreInline(admin.StackedInline):
    verbose_name = "Media Genre Additional Resource"
    verbose_name_plural = "Media Genre Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "character",
        "place",
        "theme",
        "topic",
        "time_period",
        "item",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "genre"


class AdditionalResourceItemInline(admin.StackedInline):
    verbose_name = "Media Item Additional Resource"
    verbose_name_plural = "Media Item Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "character",
        "place",
        "theme",
        "topic",
        "time_period",
        "genre",
        "career",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "item"


class AdditionalResourceCareerInline(admin.StackedInline):
    verbose_name = "Media Career Additional Resource"
    verbose_name_plural = "Media Career Additional Resource"
    exclude = (
        "created_by",
        "updated_by",
        "discovery_media",
        "media_credit",
        "character",
        "place",
        "theme",
        "topic",
        "time_period",
        "genre",
        "item",
    )
    model = AdditionalResource
    extra = 1
    fk_name = "career"


class MediaCreditsRefInline(admin.StackedInline):
    verbose_name = "Media Credits"
    verbose_name_plural = "Media Credits"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["media_credit"]
    model = MediaCreditsReference
    extra = 1
    fk_name = "discovery_media"
    insert_after = "link"


@admin.register(MediaCredits)
class MediaCreditsAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "media_linked")
    ordering = ("-created_at",)
    search_fields = ("name",)
    list_filter = ("role",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("image_preview", "media_linked", "created_at", "updated_at")
    inlines = [AdditionalResourceCreditInline]

    def media_linked(self, obj):
        titles = MediaCreditsReference.objects.filter(
            media_credit__in=[obj]
        ).values_list("discovery_media__title", flat=True)
        return ", ".join(titles)

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )


class MediaCharacterInline(admin.StackedInline):
    verbose_name = "Media Character"
    verbose_name_plural = "Media Characters"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["character"]
    model = MediaCharacter
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class MediaPlaceInline(admin.StackedInline):
    verbose_name = "Media Place"
    verbose_name_plural = "Media Places"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["place"]
    model = MediaPlace
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class MediaItemInline(admin.StackedInline):
    verbose_name = "Media Item"
    verbose_name_plural = "Media Items"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["item"]
    model = MediaItem
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class MediaThemeInline(admin.StackedInline):
    verbose_name = "Media Theme"
    verbose_name_plural = "Media Themes"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["theme"]
    model = MediaTheme
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class MediaTopicInline(admin.StackedInline):
    verbose_name = "Media Topic"
    verbose_name_plural = "Media Topics"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["topic"]
    model = MediaTopic
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class MediaTimePeriodInline(admin.StackedInline):
    verbose_name = "Media Time Period"
    verbose_name_plural = "Media Time Periods"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["time_period"]
    model = MediaTimePeriod
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class MediaGenreInline(admin.StackedInline):
    verbose_name = "Media Genre"
    verbose_name_plural = "Media Genres"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["genre"]
    model = MediaGenre
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class RelatedMediaInline(admin.StackedInline):
    verbose_name = "Related Media"
    verbose_name_plural = "Related Media"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["related_media"]
    model = RelatedMedia
    extra = 1
    fk_name = "discovery_media"
    insert_after = "describe_label"


class MediaActivityInline(admin.StackedInline):
    verbose_name = "Media Activity"
    verbose_name_plural = "Media Activities"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["media_activity"]
    model = MediaActivity
    extra = 1
    fk_name = "discovery_media"
    insert_after = "enhance_label"


class MediaCareerInterestInline(admin.StackedInline):
    verbose_name = "Media Career Interest"
    verbose_name_plural = "Media Career Interests"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["career_interest"]
    model = MediaCareerInterest
    extra = 1
    fk_name = "discovery_media"
    insert_after = "enhance_label"


class MediaPurchaseOpputunitesInline(admin.StackedInline):
    verbose_name = "Media Purchase Oppurtunity"
    verbose_name_plural = "Media Purchase Oppurtunities"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["purchase_oppurtunity"]
    model = MediaPurchaseOppurtunity
    extra = 1
    fk_name = "discovery_media"
    insert_after = "enhance_label"


class MediaIdentifierInline(admin.TabularInline):
    exclude = ("created_by", "updated_by")
    model = MediaIdentifier
    extra = 1
    fk_name = "discovery_media"
    insert_after = "title"


@admin.register(Media)
class DiscoveryMediaAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "created_at", "active")
    ordering = ("-created_at",)
    list_filter = (
        "active",
        "media_type",
    )
    search_fields = ("title", "mongo_id")
    filter_horizontal = (
        "target_audience",
        "groups",
    )
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
        "cover_image_preview",
        "describe_label",
        "enhance_label",
    )
    inlines = [
        MediaCreditsRefInline,
        MediaIdentifierInline,
        MediaCharacterInline,
        MediaPlaceInline,
        MediaItemInline,
        MediaThemeInline,
        MediaTopicInline,
        MediaTimePeriodInline,
        MediaGenreInline,
        RelatedMediaInline,
        MediaActivityInline,
        MediaCareerInterestInline,
        MediaPurchaseOpputunitesInline,
        AdditionalResourceMediaInline,
    ]
    fieldsets = (
        (
            None,
            {"fields": ("id", "media_type", "active", "stub")},
        ),
        (
            _("Identify"),
            {
                "fields": (
                    "title",
                    "o_type",
                    "summary",
                    "summary_link",
                    "origin",
                    "target_audience",
                    "link",
                    "cover_image",
                    "cover_image_preview",
                    "format",
                    "created_at",
                    "updated_at",
                )
            },
        ),
        (
            _("Describe"),
            {"fields": ("describe_label",)},
        ),
        (
            _("Enhance"),
            {"fields": ("enhance_label",)},
        ),
        (
            _("Group"),
            {"fields": ("groups",)},
        ),
    )
    change_form_template = "admin/custom/change_form.html"

    class Media:
        js = ("discovery/js/media_admin.js",)
        css = {"all": ("discovery/css/admin.css",)}

    def describe_label(self, obj):
        return "Describe"

    def enhance_label(self, obj):
        return "Enhance"

    def cover_image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.cover_image.url)
        )


@admin.register(Characters)
class MediaCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    ordering = ("-created_at",)
    exclude = ("created_by", "updated_by", "mongo_id")
    search_fields = ("name", "mongo_id")
    filter_horizontal = ("traits", "groups")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")
    inlines = [AdditionalResourceCharacterInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaCharacter.objects.filter(character__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)


@admin.register(Places)
class MediaPlacesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "o_type", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview",
        "media_linked",
        "activity_linked",
    )
    filter_horizontal = ("groups",)
    inlines = [AdditionalResourcePlaceInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaPlace.objects.filter(place__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)

    def activity_linked(self, obj):
        titles = ActivityPlace.objects.filter(place__in=[obj]).values_list(
            "place_activity__name", flat=True
        )
        return ", ".join(titles)


@admin.register(Items)
class MediaItemsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    filter_horizontal = ("groups",)
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")
    inlines = [AdditionalResourceItemInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaItem.objects.filter(item__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)


@admin.register(Themes)
class MediaThemesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")
    inlines = [AdditionalResourceThemeInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaTheme.objects.filter(theme__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)


@admin.register(Topics)
class MediaTopicsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")
    inlines = [AdditionalResourceTopicInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaTopic.objects.filter(topic__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)


@admin.register(TimePeriods)
class MediaTimePeriodsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")
    inlines = [AdditionalResourceTimePeriodInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaTimePeriod.objects.filter(time_period__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)


class GenreAdminForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = "__all__"
        widgets = {
            "applicable_formats": forms.SelectMultiple(
                choices=GENRE_APPLICABLE_FORMAT_CHOICES
            ),
        }


@admin.register(Genres)
class MediaGenresAdmin(admin.ModelAdmin):
    form = GenreAdminForm
    list_display = ("name", "description", "applicable_formats", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")
    inlines = [AdditionalResourceGenreInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaGenre.objects.filter(genre__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)


class ActivityPlaceInline(admin.StackedInline):
    verbose_name = "Activity Place"
    verbose_name_plural = "Activity Places"
    exclude = (
        "created_by",
        "updated_by",
    )
    autocomplete_fields = ["place"]
    model = ActivityPlace
    extra = 1
    fk_name = "place_activity"


@admin.register(Activity)
class MediaActivityAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    inlines = [ActivityPlaceInline]
    search_fields = ("name", "mongo_id")
    ordering = ("-created_at",)
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaActivity.objects.filter(media_activity__in=[obj]).values_list(
            "discovery_media__title", flat=True
        )
        return ", ".join(titles)


@admin.register(CareerInterests)
class MediaCareerInterestsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")
    inlines = [AdditionalResourceCareerInline]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaCareerInterest.objects.filter(
            career_interest__in=[obj]
        ).values_list("discovery_media__title", flat=True)
        return ", ".join(titles)


@admin.register(PurchaseOppurtunities)
class MediaPurchaseOppurtunitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "mongo_id")
    exclude = ("created_by", "updated_by", "mongo_id")
    readonly_fields = ("created_at", "updated_at", "image_preview", "media_linked")

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{}" width="200" height="200" />'.format(obj.image.url)
        )

    def media_linked(self, obj):
        titles = MediaPurchaseOppurtunity.objects.filter(
            purchase_oppurtunity__in=[obj]
        ).values_list("discovery_media__title", flat=True)
        return ", ".join(titles)


@admin.register(AdditionalResource)
class MediaAddtionalResourceAdmin(admin.ModelAdmin):
    list_display = ("link", "description", "created_at")
    ordering = ("-created_at",)
    search_fields = ("link",)
    exclude = ("created_by", "updated_by")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Reviews)
class MediaReviewsAdmin(admin.ModelAdmin):
    list_display = ("discovery_media", "created_by", "created_at")
    autocomplete_fields = ("discovery_media", "created_by")
    ordering = ("-created_at",)
    search_fields = ("discovery_media__title",)
    exclude = ("updated_by",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Quotes)
class MediaQuotesAdmin(admin.ModelAdmin):
    list_display = ("discovery_media", "created_by", "created_at")
    autocomplete_fields = ("discovery_media", "created_by")
    ordering = ("-created_at",)
    search_fields = ("discovery_media__title",)
    exclude = ("updated_by",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(UserExperience)
class MediaExperienceAdmin(admin.ModelAdmin):
    list_display = ("discovery_media", "created_by", "created_at")
    autocomplete_fields = ("discovery_media", "created_by")
    ordering = ("-created_at",)
    search_fields = ("discovery_media__title",)
    exclude = ("updated_by",)
    readonly_fields = ("created_at", "updated_at")
