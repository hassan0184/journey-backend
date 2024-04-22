from django.core.management.base import BaseCommand
from common.models import Ethnicity, Gender
from journey.models import RoleType, HeroTypes, RecommendationType, Challenges

ETHNICITY = [
    {
        "label": "South Asian",
        "is_active": True,
        "id": "cea5aef9-4d8b-446a-b963-e984b9d21468",
    },
    {
        "label": "Middle Eastern",
        "is_active": True,
        "id": "f588460e-43af-4691-98e2-5b50b47a376f",
    },
    {
        "label": "Hispanic/Latinx",
        "is_active": True,
        "id": "d9e2d6b1-4c7c-40da-a736-c3314e92b292",
    },
    {
        "label": "East Asian",
        "is_active": True,
        "id": "bf70fc18-ab17-4314-8115-881c991f59cc",
    },
    {"label": "White", "is_active": True, "id": "e23c66d5-f194-40e3-9c82-9975502043ee"},
    {"label": "Black", "is_active": True, "id": "f03919eb-e27c-4435-84ed-6df6d750db8d"},
]

GENDER = [
    {
        "label": "Agender",
        "id": "3d83c179-8f34-4e8e-9729-95f5cb8a7a62",
        "is_active": True,
    },
    {
        "label": "Non-Binary",
        "id": "b3765ba1-11c7-4f22-9f9e-4f3d757a47c5",
        "is_active": True,
    },
    {
        "label": "Gender Neutral",
        "id": "646c4b19-8f65-4243-919e-8ecd6ead8264",
        "is_active": True,
    },
    {
        "label": "Transgender Male",
        "id": "f08282e2-a840-44c7-82bc-585ed67fa743",
        "is_active": True,
    },
    {
        "label": "Transgender Female",
        "id": "6dfa5686-b4b7-4e77-8ff1-65f0ce1bff92",
        "is_active": True,
    },
    {
        "label": "Female",
        "id": "16050992-da11-4e8e-85ea-10ab99e57324",
        "is_active": True,
    },
    {"label": "Male", "id": "653fd8a7-59e3-46bf-a219-7740804e9ece", "is_active": True},
]
ROLE_TYPE = [
    {
        "id": "04c670d9-ec61-4ee1-baa6-0b440bb5341d",
        "type": "self",
        "label": "I am the hero!",
        "label_description": "I am here to address my own challenge.",
        "is_active": True,
    },
    {
        "id": "f6521b10-fbe2-4ed3-92eb-01127b912bc4",
        "type": "mentor",
        "label": "They are my hero!",
        "label_description": "I am here to help someone else with a challenge.",
        "is_active": True,
    },
]
HERO_TYPES = [
    {
        "label": "Student",
        "role_type_id": "f6521b10-fbe2-4ed3-92eb-01127b912bc4",
        "is_active": True,
    },
    {
        "label": "Family Member",
        "role_type_id": "f6521b10-fbe2-4ed3-92eb-01127b912bc4",
        "is_active": True,
    },
    {
        "label": "Client",
        "role_type_id": "f6521b10-fbe2-4ed3-92eb-01127b912bc4",
        "is_active": True,
    },
    {
        "label": "Colleague",
        "role_type_id": "f6521b10-fbe2-4ed3-92eb-01127b912bc4",
        "is_active": True,
    },
    {
        "label": "Friend",
        "role_type_id": "f6521b10-fbe2-4ed3-92eb-01127b912bc4",
        "is_active": True,
    },
]
RECOMMENDATION_TYPE = [
    {
        "image": "recommendations/1578686304237.png",
        "label": "Engage",
        "is_active": True,
        "id": "2f3dd514-b4de-4494-9373-1ce46c5aa1ad",
    },
    {
        "image": "recommendations/1578686304237.png",
        "label": "Interact",
        "is_active": True,
        "id": "ba550e0f-8e23-4e0a-bb05-e7c6f5588558",
    },
    {
        "image": "recommendations/1578686304237.png",
        "label": "Play",
        "is_active": True,
        "id": "ef7271d1-b288-4f1f-acde-3af8b310a61a",
    },
    {
        "image": "recommendations/1578686304237.png",
        "label": "Listen",
        "is_active": True,
        "id": "6ca8ecd3-a775-4aea-ad25-27a359f40956",
    },
    {
        "image": "recommendations/1578686304237.png",
        "label": "Read",
        "is_active": True,
        "id": "fbc0db62-589f-4f1b-9d86-734803a1d976",
    },
    {
        "image": "recommendations/1578686304237.png",
        "label": "Watch",
        "is_active": True,
        "id": "eacc0bd1-0829-4316-b1f8-3bb3ea288e8e",
    },
]

CHALLENGES = [
    {"id": "ae232ef2-1f80-457d-81a5-fdb23b2253cc", "label": "Abuse", "is_active": True},
    {
        "id": "f19ec7f9-250f-4fcf-bf78-3218798eff8c",
        "label": "Addiction",
        "is_active": True,
    },
    {
        "id": "166e03f5-48b3-4b1d-b70a-1b8b76f8ef03",
        "label": "Anger Management",
        "is_active": True,
    },
    {
        "id": "1d569a2f-6623-41b5-8b6f-172675563888",
        "label": "Boredom",
        "is_active": True,
    },
    {
        "id": "5170ebbe-82de-4318-829c-cd763aba5a5c",
        "label": "Career Path",
        "is_active": True,
    },
    {"id": "2b029fd2-a6fc-4711-8a81-365bcc0c1abd", "label": "Death", "is_active": True},
    {
        "id": "c1514c29-044b-4d88-9cf9-097bffbcc559",
        "label": "Childcare",
        "is_active": True,
    },
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in ETHNICITY:
            Ethnicity.objects.get_or_create(**obj)
        for obj in GENDER:
            Gender.objects.get_or_create(**obj)
        for obj in ROLE_TYPE:
            RoleType.objects.get_or_create(**obj)
        for obj in HERO_TYPES:
            HeroTypes.objects.get_or_create(**obj)
        for obj in RECOMMENDATION_TYPE:
            RecommendationType.objects.get_or_create(**obj)
        for obj in CHALLENGES:
            Challenges.objects.get_or_create(**obj)
