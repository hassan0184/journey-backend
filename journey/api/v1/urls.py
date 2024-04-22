from rest_framework.routers import DefaultRouter
from journey.api.v1.viewsets.challenges_viewset import (
    UserChallengeRequest,
    UserChallengeView,
)
from journey.api.v1.viewsets.onboard_viewset import OnBoardView
from journey.api.v1.viewsets.quests_viewset import UserQuestRequest, SelectQuestsView
from journey.api.v1.viewsets.obstacles_viewset import (
    ObstacleTypes,
    ObstacleThreatLevels,
    CustomObstacle,
    ObstaclesView,
)
from journey.api.v1.viewsets.powerups_viewset import (
    PowerupTypes,
    CustomPowerUp,
    PowerUpView,
)
from journey.api.v1.viewsets.allies import InviteAlliesView, AlliesQuestsView


app_name = "journey"

router = DefaultRouter()
router.register(r"onboard", OnBoardView, basename="onboard")
router.register(r"user_challenge", UserChallengeView, basename="user_challenge")
router.register(
    r"challenge_request", UserChallengeRequest, basename="challenge_request"
)
# Quests API
router.register(r"challenge_quests", SelectQuestsView, basename="challenge_quests")
router.register(r"quest_request", UserQuestRequest, basename="quest_request")


# Obstacle API

router.register(r"obstacle_types", ObstacleTypes, basename="obstacle_types")
router.register(
    r"obstacle_threat_levels", ObstacleThreatLevels, basename="obstacle_threat_levels"
)
router.register(r"custom_obstacle", CustomObstacle, basename="custom_obstacle")
router.register(r"obstacles", ObstaclesView, basename="obstacles")

# PowerUp API
router.register(r"powerup_types", PowerupTypes, basename="powerup_types")
router.register(r"custom_powerup", CustomPowerUp, basename="custom_powerup")
router.register(r"powerups", PowerUpView, basename="powerups")

# Allies API
router.register(r"invite_ally", InviteAlliesView, basename="invite_ally")
router.register(r"ally_quests", AlliesQuestsView, basename="ally_quests")


urlpatterns = router.urls
