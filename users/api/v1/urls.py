from rest_framework.routers import DefaultRouter
from users.api.v1 import viewsets

app_name = "users"
router = DefaultRouter()
router.register(r"register", viewsets.UserRegistration, basename="register")
router.register(r"login", viewsets.UserLogin, basename="login")
router.register(r"profile", viewsets.UserProfile, basename="profile")
router.register(r"logout", viewsets.Logout, basename="logout")
router.register(r"verify_otp", viewsets.VerifyOTP, basename="verify_otp")
router.register(r"update_email", viewsets.UpdateUserEmail, basename="update_email")
router.register(r"resend_otp", viewsets.ResendEmailOTP, basename="resend_otp")
router.register(r"google", viewsets.GoogleLogin, basename="google")
router.register(r"apple", viewsets.AppleLogin, basename="facebook")
router.register(
    r"forget_password", viewsets.ForgetPasswordEmail, basename="forget_email"
)
router.register(
    r"reset_password_otp",
    viewsets.VerifyResetPasswordOTP,
    basename="reset_password_otp",
)
router.register(r"reset_password", viewsets.SetPassword, basename="reset_password")

urlpatterns = router.urls
