from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


onboard_list_parameters = [
    OpenApiParameter(
        name="key",
        type=str,
        description="Filter type",
        examples=[
            OpenApiExample("all", summary="all", description="all list", value="all"),
            OpenApiExample(
                "roles", summary="roles", description="roles list", value="roles"
            ),
            OpenApiExample(
                "ethnicity",
                summary="ethnicity",
                description="longer list",
                value="ethnicity",
            ),
            OpenApiExample(
                "gender",
                summary="gender",
                description="longer list",
                value="gender",
            ),
            OpenApiExample(
                "challenges",
                summary="challenges",
                description="longer list",
                value="challenges",
            ),
            OpenApiExample(
                "recommendations",
                summary="recommendation_type",
                description="longer list",
                value="recommendation_type",
            ),
        ],
    ),
]


select_quest_list_param = [
    OpenApiParameter(
        name="user_challenge",
        required=True,
        description="User Challenge ID",
        type=OpenApiTypes.UUID,
    ),
]


quest_param = [
    OpenApiParameter(
        name="quest", required=True, description="Quest ID", type=OpenApiTypes.UUID
    ),
]
