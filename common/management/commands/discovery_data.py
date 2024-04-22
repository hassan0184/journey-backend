import json
from django.core.management.base import BaseCommand
from common.models import AgeGroup
from discovery.models import (
    CharacterTraits,
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
    MediaIdentifier,
    MediaCredits,
    MediaCreditsReference,
    MediaPurchaseOppurtunity,
    MediaCareerInterest,
    MediaCharacter,
    MediaTheme,
    MediaTopic,
    MediaActivity,
    MediaPlace,
    MediaGenre,
    MediaTimePeriod,
    RelatedMedia,
    MediaItem,
    ActivityPlace,
)

AGE_GROUP = [
    {
        "label": "0-1",
        "min_age": 0,
        "max_age": 1,
    },
    {
        "label": "2",
        "min_age": 2,
        "max_age": 2,
    },
    {
        "label": "3-5",
        "min_age": 3,
        "max_age": 5,
    },
    {
        "label": "6-10",
        "min_age": 6,
        "max_age": 10,
    },
    {
        "label": "11-13",
        "min_age": 11,
        "max_age": 13,
    },
    {
        "label": "14-18",
        "min_age": 14,
        "max_age": 18,
    },
    {
        "label": "19-25",
        "min_age": 19,
        "max_age": 25,
    },
    {
        "label": "26-41",
        "min_age": 26,
        "max_age": 41,
    },
    {
        "label": "42-57",
        "min_age": 42,
        "max_age": 57,
    },
    {
        "label": "58-67",
        "min_age": 58,
        "max_age": 67,
    },
    {
        "label": "68-76",
        "min_age": 68,
        "max_age": 76,
    },
    {
        "label": "77-94",
        "min_age": 77,
        "max_age": 94,
    },
    {
        "label": "95+",
        "min_age": 95,
        "max_age": 100,
    },
]


def add_age_groups():
    for age_group in AGE_GROUP:
        AgeGroup.objects.get_or_create(**age_group)


def add_character_traits():
    with open("common/management/commands/discoverytraits.json") as file:
        data = json.load(file)
        for item in data:
            CharacterTraits.objects.get_or_create(
                label=item["name"],
                active=item["active"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
                mongo_id=item["_id"]["$oid"],
            )


def add_genres():
    with open("common/management/commands/genres.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            for i, a in enumerate(item.get("format", [])):
                if a == "song":
                    item.get("format", [])[i] = "music"
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            Genres.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                applicable_formats=item.get("format", []),
            )
        print(images)


def add_items():
    with open("common/management/commands/items.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            Items.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )
        print(images)


def add_places():
    with open("common/management/commands/places.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            Places.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
                o_type="real" if item.get("real") else "fiction",
            )
        print(images)


def add_purchase_oppurtunities():
    with open("common/management/commands/purchaseopportunities.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            PurchaseOppurtunities.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                link=item.get("link", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )
        print(images)


def add_themes():
    with open("common/management/commands/themes.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            Themes.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )
        print(images)


def add_time_period():
    with open("common/management/commands/timeperiods.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            TimePeriods.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )
        print(images)


def add_topics():
    with open("common/management/commands/topics.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            Topics.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )

        print(images)


def add_career_interests():
    with open("common/management/commands/careerinterests.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            CareerInterests.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )
        print(images)


def add_activities():
    with open("common/management/commands/discoveryactivities.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            act, _ = Activity.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                no_of_participants=item.get("numParticipants", 0),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )
            places_id = [obj["$oid"] for obj in item.get("placeList", [])]
            places = Places.objects.filter(mongo_id__in=places_id)
            for place in places:
                ActivityPlace.objects.get_or_create(
                    place_activity=act,
                    place=place,
                )
        print(images)


def add_characters():
    with open("common/management/commands/characters.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            char, _ = Characters.objects.get_or_create(
                name=item["name"],
                active=item["active"],
                description=item.get("description", ""),
                mongo_id=item["_id"]["$oid"],
                created_at=item["created"]["$date"],
                updated_at=item["updated"]["$date"],
            )
            traits_id = [
                obj["$oid"] if type(obj) == dict else obj
                for obj in item.get("traits", [])
            ]
            traits = CharacterTraits.objects.filter(mongo_id__in=traits_id)
            char.traits.set(traits)
        print(images)


def add_media_identifiers(media, identifier):
    try:
        MediaIdentifier.objects.get_or_create(
            discovery_media=media,
            identifier=identifier,
        )
    except Exception as e:
        print(e)
        pass


def add_media_credits(media, media_type, credits):
    MEDIA_TYPE_CREDITS = {
        "podcast": "host",
        "movie": "director",
        "book": "author",
        "song": "composer",
        "tvshow": "creator",
        "artifact": "creator",
        "game": "developer",
        "theater": "play_wright",
    }

    credits_list = []
    for credit in credits:
        mc, _ = MediaCredits.objects.get_or_create(
            name=credit["name"],
            role=MEDIA_TYPE_CREDITS[media_type],
        )
        credits_list.append(mc)

    for credit in credits_list:
        MediaCreditsReference.objects.get_or_create(
            discovery_media=media,
            media_credit=credit,
        )


def add_media_items(media, items):
    items_id = [obj["$oid"] if type(obj) == dict else obj for obj in items]
    items = Items.objects.filter(mongo_id__in=items_id)
    for item in items:
        MediaItem.objects.get_or_create(
            discovery_media=media,
            item=item,
        )


def add_media_themes(media, themes):
    themes_id = [obj["$oid"] if type(obj) == dict else obj for obj in themes]
    themes = Themes.objects.filter(mongo_id__in=themes_id)
    for theme in themes:
        MediaTheme.objects.get_or_create(
            discovery_media=media,
            theme=theme,
        )


def add_media_carrier(media, carrier):
    carrier_id = [obj["$oid"] if type(obj) == dict else obj for obj in carrier]
    carriers = CareerInterests.objects.filter(mongo_id__in=carrier_id)
    for c in carriers:
        MediaCareerInterest.objects.get_or_create(
            discovery_media=media,
            career_interest=c,
        )


def add_media_characters(media, characters):
    characters_id = [obj["$oid"] if type(obj) == dict else obj for obj in characters]
    characters = Characters.objects.filter(mongo_id__in=characters_id)
    for character in characters:
        MediaCharacter.objects.get_or_create(
            discovery_media=media,
            character=character,
        )


def add_media_topics(media, topics):
    topics_id = [obj["$oid"] if type(obj) == dict else obj for obj in topics]
    topics = Topics.objects.filter(mongo_id__in=topics_id)
    for topic in topics:
        MediaTopic.objects.get_or_create(
            discovery_media=media,
            topic=topic,
        )


def add_media_target_audience(media, target_audience):
    age_groups = [obj.replace("_", "-") for obj in target_audience]
    age_groups = AgeGroup.objects.filter(label__in=age_groups)
    media.target_audience.set(age_groups)


def add_genre(media, genres):
    genres_id = [obj["$oid"] if type(obj) == dict else obj for obj in genres]
    genres = Genres.objects.filter(mongo_id__in=genres_id)
    for genre in genres:
        MediaGenre.objects.get_or_create(
            discovery_media=media,
            genre=genre,
        )


def add_media_time_period(media, time_period):
    time_period_id = [obj["$oid"] if type(obj) == dict else obj for obj in time_period]
    time_period = TimePeriods.objects.filter(mongo_id__in=time_period_id)
    for tp in time_period:
        MediaTimePeriod.objects.get_or_create(
            discovery_media=media,
            time_period=tp,
        )


def add_media_activities(media, activities):
    activities_id = [obj["$oid"] if type(obj) == dict else obj for obj in activities]
    activities = Activity.objects.filter(mongo_id__in=activities_id)
    for activity in activities:
        MediaActivity.objects.get_or_create(
            discovery_media=media,
            media_activity=activity,
        )


def add_media_places(media, places):
    places_id = [obj["$oid"] if type(obj) == dict else obj for obj in places]
    places = Places.objects.filter(mongo_id__in=places_id)
    for place in places:
        MediaPlace.objects.get_or_create(
            discovery_media=media,
            place=place,
        )


def add_purchase_oppurtunities_media(media, purchase_oppurtunities):
    purchase_oppurtunities_id = [
        obj["$oid"] if type(obj) == dict else obj for obj in purchase_oppurtunities
    ]
    purchase_oppurtunities = PurchaseOppurtunities.objects.filter(
        mongo_id__in=purchase_oppurtunities_id
    )
    for po in purchase_oppurtunities:
        MediaPurchaseOppurtunity.objects.get_or_create(
            discovery_media=media,
            purchase_oppurtunity=po,
        )


def add_mentioned_media(media, mentioned_media):
    for obj in mentioned_media:
        if obj["ref"] == "Item":
            item_id = obj["id"]["$oid"]
            item = Items.objects.filter(mongo_id=item_id)
            for i in item:
                MediaItem.objects.get_or_create(discovery_media=media, item=i)
        elif obj["ref"] == "Place":
            place_id = obj["id"]["$oid"]
            place = Places.objects.filter(mongo_id=place_id)
            for p in place:
                MediaPlace.objects.get_or_create(discovery_media=media, place=p)
        elif obj["ref"] == "Theme":
            theme_id = obj["id"]["$oid"]
            theme = Themes.objects.filter(mongo_id=theme_id)
            for t in theme:
                MediaTheme.objects.get_or_create(discovery_media=media, theme=t)
        elif obj["ref"] == "Genre":
            genre_id = obj["id"]["$oid"]
            genre = Genres.objects.filter(mongo_id=genre_id)
            for g in genre:
                MediaGenre.objects.get_or_create(discovery_media=media, genre=g)
        elif obj["ref"] == "Topic":
            topic_id = obj["id"]["$oid"]
            topic = Topics.objects.filter(mongo_id=topic_id)
            for to in topic:
                MediaTopic.objects.get_or_create(discovery_media=media, topic=to)
        elif obj["ref"] == "TimePeriod":
            time_period_id = obj["id"]["$oid"]
            time_period = TimePeriods.objects.filter(mongo_id=time_period_id)
            for tp in time_period:
                MediaTimePeriod.objects.get_or_create(
                    discovery_media=media, time_period=tp
                )
        elif obj["ref"] == "Character":
            character_id = obj["id"]["$oid"]
            character = Characters.objects.filter(mongo_id=character_id)
            for c in character:
                MediaCharacter.objects.get_or_create(discovery_media=media, character=c)


def add_media():
    MEDIA_TYPE = {
        "podcast": "podcast",
        "movie": "movie",
        "book": "book",
        "song": "music",
        "tvshow": "tv_show",
        "artifact": "artifact",
        "game": "game",
        "theater": "theater",
        "discovery": "discovery",
    }
    MEDIA_FORMAT = {
        "Cassette": "cassette",
        "VHS": "vhs",
        "CD": "cd",
        "video game": "video_game",
        "paperback": "paperback",
        "tabletop RPG": "tabletop_game",
        "Streaming": "streaming",
        "DVD": "dvd",
        "Vinyl": "vinyl",
        "hardcover": "hardcover",
        None: None,
    }
    with open("common/management/commands/media.json") as file:
        data = json.load(file)
        images = {}
        for item in data:
            if item.get("image"):
                images[item["_id"]["$oid"]] = item.get("image")
            media, _ = Media.objects.get_or_create(
                media_type=MEDIA_TYPE[item["mediaType"]],
                title=item["title"],
                active=item["active"],
                summary=item.get("summary", ""),
                link=item.get("link", ""),
                origin=item.get("origin", None),
                format=MEDIA_FORMAT.get(item.get("format")),
                mongo_id=item["_id"]["$oid"],
                stub=item.get("stub", False),
            )
            if item.get("identifier"):
                add_media_identifiers(media, item["identifier"])
            if item.get("creator"):
                add_media_credits(media, item["mediaType"], item["creator"])
            if item.get("items"):
                add_media_items(media, item["items"])
            if item.get("themes"):
                add_media_themes(media, item["themes"])
            if item.get("careerInterests"):
                add_media_carrier(media, item["careerInterests"])
            if item.get("characters"):
                add_media_characters(media, item["characters"])
            if item.get("topics"):
                add_media_topics(media, item["topics"])
            if item.get("targetAudience"):
                add_media_target_audience(media, item["targetAudience"])
            if item.get("genres"):
                add_genre(media, item["genres"])
            if item.get("timePeriods"):
                add_media_time_period(media, item["timePeriods"])
            if item.get("activities"):
                add_media_activities(media, item["activities"])
            if item.get("places"):
                add_media_places(media, item["places"])
            if item.get("purchaseOpportunities"):
                add_purchase_oppurtunities_media(media, item["purchaseOpportunities"])
            if item.get("mentionedMedia"):
                add_mentioned_media(media, item["mentionedMedia"])
        print(images)


def add_related_media():
    with open("common/management/commands/media.json") as file:
        data = json.load(file)
        for item in data:
            media = Media.objects.get(mongo_id=item["_id"]["$oid"])
            related_media_id = [
                obj["$oid"] if type(obj) == dict else obj
                for obj in item.get("relatedMedia", [])
            ]
            related_media = Media.objects.filter(mongo_id__in=related_media_id)
            for rm in related_media:
                RelatedMedia.objects.get_or_create(
                    discovery_media=media, related_media=rm
                )


class Command(BaseCommand):
    def handle(self, *args, **options):
        add_age_groups()
        print("Age groups added successfully")
        add_character_traits()
        print("Character traits added successfully")
        add_genres()
        print("Genres added successfully")
        add_items()
        print("Items added successfully")
        add_places()
        print("Places added successfully")
        add_purchase_oppurtunities()
        print("Purchase oppurtunities added successfully")
        add_themes()
        print("Themes added successfully")
        add_time_period()
        print("Time periods added successfully")
        add_topics()
        print("Topics added successfully")
        add_career_interests()
        print("Career interests added successfully")
        add_activities()
        print("Activities added successfully")
        add_characters()
        print("Characters added successfully")
        add_media()
        print("Media added successfully")
        add_related_media()
        print("Done!")
