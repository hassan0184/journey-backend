from django.core.exceptions import ValidationError
from rest_framework import viewsets, permissions
from rest_framework.status import HTTP_201_CREATED
from drf_spectacular.utils import extend_schema

from journey.api.v1.serializers import UserChallengeSerializer
from journey.api.v1.serializers.quests_serializer import (
    GetChallengeQueststSerializer,
    QuestsRequestSerializer,
    AddUserQueststSerializer,
)
from journey.api.v1.viewsets.extend_schema import select_quest_list_param
from journey.models import UserChallenges, Quests, PowerUps, Obstacles
from common.custom_permissions import EmailVerified
from common.custom_response import vj_response
from common.messages import (
    QUEST_REQUEST_ADDED,
    CHALLENGE_ID_REQUIRED,
    INVALID_CHALLENGE_ID,
)


class UserQuestRequest(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(request=QuestsRequestSerializer, responses={201: str})
    def create(self, request):
        serializer = QuestsRequestSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return vj_response(QUEST_REQUEST_ADDED, status=HTTP_201_CREATED)


class SelectQuestsView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(
        responses={200: GetChallengeQueststSerializer},
        parameters=select_quest_list_param,
    )
    def list(self, request):
        user_challenge_id = self.request.query_params.get("user_challenge")

        if not user_challenge_id:
            raise ValidationError(CHALLENGE_ID_REQUIRED)

        try:
            user_challenge = UserChallenges.objects.get(
                id=user_challenge_id, user=request.user
            )
        except UserChallenges.DoesNotExist:
            raise ValidationError(INVALID_CHALLENGE_ID)

        challenge_hero_age = user_challenge.hero_age
        challenge_id = user_challenge.hero_challenge_id

        quests = Quests.objects.filter(
            challenge_id=challenge_id,
            is_active=True,
            # age_group__min_age__lt=challenge_hero_age,
            # age_group__max_age__gte=challenge_hero_age
        ).prefetch_related("powerups", "obstacles")

        serializer = GetChallengeQueststSerializer(
            quests, many=True, context={"user": self.request.user}
        )

        return vj_response(serializer.data)

    @extend_schema(
        request=AddUserQueststSerializer, responses={200: UserChallengeSerializer}
    )
    def create(self, request):
        serializer = AddUserQueststSerializer(
            data=request.data, context={"request": self.request}
        )

        serializer.is_valid(raise_exception=True)
        user_challenge = serializer.validated_data["user_challenge"]
        serializer.save()

        return vj_response(UserChallengeSerializer(instance=user_challenge).data)
