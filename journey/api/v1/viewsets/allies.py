from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions
from rest_framework.status import HTTP_201_CREATED

from common.custom_permissions import EmailVerified
from common.custom_response import vj_response
from common.messages import ALLY_INVITATION_SENT
from journey.api.v1.serializers.allies import InviteAllySerializer, AllyQuestsSerializer
from journey.models.allies import AlliesQuests
from journey.services.utils import send_ally_invite


class InviteAlliesView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(request=InviteAllySerializer, responses={201: str})
    def create(self, request):
        serializer = InviteAllySerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        ally = serializer.save()

        # ToDo send email or sms to a user
        send_ally_invite(ally)
        return vj_response(ALLY_INVITATION_SENT, status=HTTP_201_CREATED)


class AlliesQuestsView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(responses={200: AllyQuestsSerializer})
    def list(self, request):
        user = request.user
        ally_quests = AlliesQuests.objects.filter(ally__user=user).select_related()
        # shared_user_challenge_ids = ally_quests.distinct(
        #     "user_quests__user_challenge_id"
        # ).values_list("user_quests__user_challenge_id", flat=True)

        serializer = AllyQuestsSerializer(ally_quests, many=True)
        return vj_response(serializer.data)
