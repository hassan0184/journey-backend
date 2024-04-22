from rest_framework import serializers
from common.models import Ethnicity, Gender


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = ("id", "label")


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ("id", "label")
