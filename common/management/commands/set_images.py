from django.core.management.base import BaseCommand
from django.conf import settings
from .images import (
    GENRES_IMAGES,
    ITEMS_IMAGES,
    PLACES_IMAGES,
    PURCHASE_IMAGES,
    THEMES_IMAGES,
    TIME_PERIOID_IMAGES,
    TOPICS_IMAGES,
    CAREER_INTERESTS_IMAGES,
    ACTIVITY_IMAGES,
    CHARACTER_IMAGES,
    MEDIA_IMAGES,
)
from discovery.models import (
    Genres,
    Items,
    Places,
    PurchaseOppurtunities,
    Themes,
    TimePeriods,
    Topics,
    CareerInterests,
    Activity,
    Characters,
    Media,
)


def set_genres():
    path = "discovery/media/genres/"
    for key, value in GENRES_IMAGES.items():
        genre = Genres.objects.get(mongo_id=key)
        genre.image = path + value
        genre.save()


def set_items():
    path = "discovery/media/items/"
    for key, value in ITEMS_IMAGES.items():
        item = Items.objects.get(mongo_id=key)
        item.image = path + value
        item.save()


def set_places():
    path = "discovery/media/places/"
    for key, value in PLACES_IMAGES.items():
        place = Places.objects.get(mongo_id=key)
        place.image = path + value
        place.save()


def set_purchase():
    path = "discovery/media/purchase/"
    for key, value in PURCHASE_IMAGES.items():
        purchase = PurchaseOppurtunities.objects.get(mongo_id=key)
        purchase.image = path + value
        purchase.save()


def set_themes():
    path = "discovery/media/themes/"
    for key, value in THEMES_IMAGES.items():
        theme = Themes.objects.get(mongo_id=key)
        theme.image = path + value
        theme.save()


def set_time_periods():
    path = "discovery/media/time_periods/"
    for key, value in TIME_PERIOID_IMAGES.items():
        time_period = TimePeriods.objects.get(mongo_id=key)
        time_period.image = path + value
        time_period.save()


def set_topics():
    path = "discovery/media/topics/"
    for key, value in TOPICS_IMAGES.items():
        topic = Topics.objects.get(mongo_id=key)
        topic.image = path + value
        topic.save()


def set_career_interests():
    path = "discovery/media/career/"
    for key, value in CAREER_INTERESTS_IMAGES.items():
        career_interest = CareerInterests.objects.get(mongo_id=key)
        career_interest.image = path + value
        career_interest.save()


def set_activity():
    path = "discovery/media/activity/"
    for key, value in ACTIVITY_IMAGES.items():
        activity = Activity.objects.get(mongo_id=key)
        activity.image = path + value
        activity.save()


def set_characters():
    path = "discovery/media/characters/"
    for key, value in CHARACTER_IMAGES.items():
        character = Characters.objects.get(mongo_id=key)
        character.image = path + value
        character.save()


def set_media():
    path = "discovery/media/"
    for key, value in MEDIA_IMAGES.items():
        media = Media.objects.get(mongo_id=key)
        media.cover_image = path + value
        media.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        set_genres()
        print("Genres images set")
        set_items()
        print("Items images set")
        set_places()
        print("Places images set")
        set_purchase()
        print("Purchase images set")
        set_themes()
        print("Themes images set")
        set_time_periods()
        print("Time Periods images set")
        set_topics()
        print("Topics images set")
        set_career_interests()
        print("Career Interests images set")
        set_activity()
        print("Activity images set")
        set_characters()
        print("Characters images set")
        set_media()
        print("Media images set")
        print("All images set successfully")
