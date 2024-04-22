from journey.enums import OnboardFilter
from journey.api.v1.serializers import (
    RoleSerializer,
    RecommendationTypeSerializer,
)
from common.serializers import EthnicitySerializer, GenderSerializer
from journey.models import RoleType, RecommendationType
from common.models import Ethnicity, Gender
from journey.services.emails import send_invite_email_to_ally


def get_onboarding_data(d_filter=None):
    onboarding_data = {}

    if d_filter == OnboardFilter.all.value:
        roles = RoleType.objects.filter(is_active=True)
        roles_data = RoleSerializer(roles, many=True).data

        ethnicity = Ethnicity.objects.filter(is_active=True)
        ethnicity_data = EthnicitySerializer(ethnicity, many=True).data

        gender = Gender.objects.filter(is_active=True)
        gender_data = GenderSerializer(gender, many=True).data

        onboarding_data["roles"] = roles_data
        onboarding_data["ethnicity"] = ethnicity_data
        onboarding_data["gender"] = gender_data
    elif d_filter == OnboardFilter.roles.value:
        roles = RoleType.objects.filter(is_active=True)
        roles_data = RoleSerializer(roles, many=True).data
        onboarding_data["roles"] = roles_data
    elif d_filter == OnboardFilter.ethnicity.value:
        ethnicity = Ethnicity.objects.filter(is_active=True)
        ethnicity_data = EthnicitySerializer(ethnicity, many=True).data
        onboarding_data["ethnicity"] = ethnicity_data
    elif d_filter == OnboardFilter.gender.value:
        gender = Gender.objects.filter(is_active=True)
        gender_data = GenderSerializer(gender, many=True).data
        onboarding_data["gender"] = gender_data
    else:
        pass

    return onboarding_data


def get_recommendations_type_list():
    recom = RecommendationType.objects.filter(is_active=True)
    return RecommendationTypeSerializer(recom, many=True).data


def send_ally_invite(ally):
    if ally.email:
        send_invite_email_to_ally(ally)
    if ally.phone_number:
        # TODO send invite via text on phone number
        pass
    return
