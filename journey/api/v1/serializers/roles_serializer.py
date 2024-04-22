from rest_framework import serializers
from journey.models import RoleType, HeroTypes


class HeroTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroTypes
        fields = ("id", "label")


class RoleSerializer(serializers.ModelSerializer):
    hero_type = HeroTypeSerializer(source="role_hero", many=True, read_only=True)

    class Meta:
        model = RoleType
        fields = ("id", "type", "label", "label_description", "hero_type")
