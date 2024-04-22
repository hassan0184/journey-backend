from enum import Enum


class OnboardFilter(Enum):
    all = "all"
    roles = "roles"
    ethnicity = "ethnicity"
    gender = "gender"
    challenges = "challenges"
    recommendation_type = "recommendation_type"


OnboardFilter.all.label = "All"
OnboardFilter.roles.label = "Roles"
OnboardFilter.ethnicity.label = "Ethnicity"
OnboardFilter.gender.label = "Gender"
OnboardFilter.challenges.label = "Challenges"
OnboardFilter.recommendation_type.label = "Recommendation Type"

ONBOARD_FILTER_CHOICES = [(ob.value, ob.label) for ob in OnboardFilter]


class ObstacleThreatTypes(Enum):
    trap = "trap"
    trigger = "trigger"
    symptom = "symptom"
    mental_block = "mental_block"


ObstacleThreatTypes.trap.label = "Trap"
ObstacleThreatTypes.trigger.label = "Trigger"
ObstacleThreatTypes.symptom.label = "Symptom"
ObstacleThreatTypes.mental_block.label = "Mental Block"


OBSTACLE_THREAT_TYPE_CHOICES = [(tt.value, tt.label) for tt in ObstacleThreatTypes]


class ObstacleThreatLevel(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


ObstacleThreatLevel.one.label = "1"
ObstacleThreatLevel.two.label = "2"
ObstacleThreatLevel.three.label = "3"
ObstacleThreatLevel.four.label = "4"
ObstacleThreatLevel.five.label = "5"


OBSTACLE_THREAT_LEVEL_CHOICES = [(tl.value, tl.label) for tl in ObstacleThreatLevel]


class PowerUpTypes(Enum):
    tool = "tool"
    trait = "trait"
    ally = "ally"


PowerUpTypes.tool.label = "Tool"
PowerUpTypes.trait.label = "Trait"
PowerUpTypes.ally.label = "Ally"


POWER_UPS_TYPE_CHOICES = [(pt.value, pt.label) for pt in PowerUpTypes]


class JourneyMediaTypes(Enum):
    book = "book"
    video = "video"
    audio = "audio"
    website = "website"
    game = "game"
    activity = "activity"


JourneyMediaTypes.book.label = "Book"
JourneyMediaTypes.video.label = "Video"
JourneyMediaTypes.audio.label = "Audio"
JourneyMediaTypes.website.label = "Website"
JourneyMediaTypes.game.label = "Game"
JourneyMediaTypes.activity.label = "Activity"


JOURNEY_MEDIA_TYPE_CHOICES = [(jm.value, jm.label) for jm in JourneyMediaTypes]


class QuestChallendeRequestStatus(Enum):
    added = "Added"
    exist = "Existed"
    discard = "Discard"
    pending = "Pending"


QuestChallendeRequestStatus.added.label = "Added"
QuestChallendeRequestStatus.exist.label = "Already Exist"
QuestChallendeRequestStatus.discard.label = "Discarded"
QuestChallendeRequestStatus.pending.label = "Pending"

QUEST_CHALLENGE_REQUESTS_STATUS = [
    (item.value, item.label) for item in QuestChallendeRequestStatus
]
