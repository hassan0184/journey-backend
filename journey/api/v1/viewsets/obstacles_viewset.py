from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.status import HTTP_201_CREATED
from drf_spectacular.utils import extend_schema, extend_schema_field
from drf_extra_fields.fields import Base64ImageField

from journey.api.v1.serializers.obstacle_serializer import (
    CreateCustomObstacleSerializer,
    ObstacleSerializer,
)
from common.custom_permissions import EmailVerified
from common.custom_response import vj_response
from common.messages import QUEST_REQUEST_ADDED, QUEST_ID_REQUIRED, INVALID_QUEST_ID
from journey.api.v1.viewsets.extend_schema import quest_param
from journey.enums import ObstacleThreatTypes, ObstacleThreatLevel
from rest_framework.parsers import MultiPartParser

from journey.models import Quests, Obstacles


class ObstaclesView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(responses={200: ObstacleSerializer}, parameters=quest_param)
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
        obstacles = Obstacles.objects.filter(quest=quest)
        obstacles = obstacles.filter(q)
        return vj_response(ObstacleSerializer(obstacles, many=True).data)


class CustomObstacle(viewsets.ViewSet):
    parser_classes = [MultiPartParser]
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(
        request=CreateCustomObstacleSerializer, responses={201: ObstacleSerializer}
    )
    def create(self, request):
        serializer = CreateCustomObstacleSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        obstacle = serializer.save()
        obstacle.is_custom = True
        obstacle.save()
        return vj_response(ObstacleSerializer(obstacle).data, status=HTTP_201_CREATED)


class ObstacleTypes(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(responses={200: list})
    def list(self, request):
        types = [type.value for type in ObstacleThreatTypes]
        return vj_response(types)


class ObstacleThreatLevels(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(responses={200: list})
    def list(self, request):
        levels = [level.value for level in ObstacleThreatLevel]
        return vj_response(levels)
