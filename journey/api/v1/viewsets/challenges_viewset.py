from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.status import HTTP_201_CREATED
from drf_spectacular.utils import extend_schema

from journey.api.v1.serializers import (
    ChallengeRequestSerializer,
    UserChallengeSerializer,
    CreateUserChallengeSerializer,
)

from journey.models import UserChallenges
from common.custom_permissions import EmailVerified
from common.custom_response import vj_response
from common.messages import CHALLENGE_REQUEST_ADDED


class UserChallengeRequest(viewsets.ViewSet):
    @extend_schema(request=ChallengeRequestSerializer, responses={201: str})
    def create(self, request):
        serializer = ChallengeRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return vj_response(CHALLENGE_REQUEST_ADDED, status=HTTP_201_CREATED)


class UserChallengeView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(
        request=CreateUserChallengeSerializer, responses={201: UserChallengeSerializer}
    )
    def create(self, request):
        serializer = CreateUserChallengeSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        user_challenge = serializer.save()

        return vj_response(
            UserChallengeSerializer(user_challenge).data, status=HTTP_201_CREATED
        )

    @extend_schema(responses={200: UserChallengeSerializer})
    def list(self, request):
        u_chal = UserChallenges.objects.filter(user=request.user).prefetch_related(
            "user_challenge_quests"
        )
        serializer = UserChallengeSerializer(u_chal, many=True)
        return vj_response(serializer.data)

    @extend_schema(responses={200: UserChallengeSerializer})
    def retrieve(self, request, pk=None):
        queryset = UserChallenges.objects.filter(user=request.user).prefetch_related(
            "user_challenge_quests"
        )
        user_challenge = get_object_or_404(queryset, pk=pk)
        serializer = UserChallengeSerializer(user_challenge)
        return vj_response(serializer.data)
