from django.core.exceptions import ValidationError
from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema


from journey.api.v1.serializers import ChallengeSerializer
from journey.models import Challenges
from common.custom_response import vj_response
from common.messages import INVALID_FILTER
from journey.enums import OnboardFilter
from journey.services.utils import get_recommendations_type_list
from .extend_schema import onboard_list_parameters

from journey.services.utils import get_onboarding_data


class OnBoardView(viewsets.ViewSet):
    @extend_schema(parameters=onboard_list_parameters)
    def list(self, request):
        data_filter = self.request.query_params.get("key", "")
        if data_filter not in (
            onboard_filter.value for onboard_filter in OnboardFilter
        ):
            raise ValidationError(INVALID_FILTER)
        data = {}
        if data_filter == OnboardFilter.all.value:
            data = get_onboarding_data(d_filter=data_filter)
            challenges = Challenges.objects.filter(is_active=True)
            ch_data = ChallengeSerializer(challenges, many=True).data

            recommendation_types = get_recommendations_type_list()
            data["challenges"] = ch_data
            data["recommendation_type"] = recommendation_types

        elif data_filter in [
            OnboardFilter.roles.value,
            OnboardFilter.ethnicity.value,
            OnboardFilter.gender.value,
        ]:
            data = get_onboarding_data(d_filter=data_filter)
        elif data_filter == OnboardFilter.challenges.value:
            challenges = Challenges.objects.filter(is_active=True)
            ch_data = ChallengeSerializer(challenges, many=True).data
            data["challenges"] = ch_data
        elif data_filter == OnboardFilter.recommendation_type.value:
            recommendation_type = get_recommendations_type_list()
            data["recommendation_type"] = recommendation_type
        else:
            data = {}

        return vj_response(data)
