from enum import Enum


class HeroType(Enum):
    self = "self"
    mentor = "mentor"


HeroType.self.label = "Self"
HeroType.mentor.label = "Mentor"

HERO_TYPE_CHOICES = [(t.value, t.label) for t in HeroType]
