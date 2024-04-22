from rest_framework import serializers

from journey.models import RecommendationType


class RecommendationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationType
        fields = ("id", "image", "label")
