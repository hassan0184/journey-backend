from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.status import HTTP_201_CREATED
from drf_spectacular.utils import extend_schema

from common.messages import QUEST_ID_REQUIRED, INVALID_QUEST_ID
from journey.api.v1.serializers.powerup_serializer import (
    CreateCustomPowerUpSerializer,
    PowerUpSerializer,
)
from common.custom_permissions import EmailVerified
from common.custom_response import vj_response
from journey.api.v1.viewsets.extend_schema import quest_param
from journey.enums import PowerUpTypes
from rest_framework.parsers import MultiPartParser

from journey.models import Quests, PowerUps


class PowerUpView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(responses={200: PowerUpSerializer}, parameters=quest_param)
    def list(self, request):
        quest_id = self.request.query_params.get("quest")
        if not quest_id:
            raise ValidationError(QUEST_ID_REQUIRED)

        try:
            quest = Quests.objects.get(id=quest_id)
            if quest.user is not None:
                if not quest.user == request.user:
                    raise ValidationError(INVALID_QUEST_ID)
        except Quests.DoesNotExist:
            raise ValidationError(INVALID_QUEST_ID)

        q = Q(user__isnull=True, is_active=True) | Q(user=request.user, is_active=True)
        powerups = PowerUps.objects.filter(quest=quest)
        powerups = powerups.filter(q)
        return vj_response(PowerUpSerializer(powerups, many=True).data)


class CustomPowerUp(viewsets.ViewSet):
    parser_classes = [MultiPartParser]
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(
        request=CreateCustomPowerUpSerializer, responses={201: PowerUpSerializer}
    )
    def create(self, request):
        serializer = CreateCustomPowerUpSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        powerup = serializer.save()
        powerup.is_custom = True
        powerup.save()
        return vj_response(PowerUpSerializer(powerup).data, status=HTTP_201_CREATED)


class PowerupTypes(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(responses={200: list})
    def list(self, request):
        types = [type.value for type in PowerUpTypes]
        return vj_response(types)
