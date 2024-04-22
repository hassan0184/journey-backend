from django.core.exceptions import ValidationError
from django.utils import timezone

from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.status import HTTP_201_CREATED

from drf_spectacular.utils import extend_schema

from common.custom_permissions import EmailVerified
from common.custom_response import vj_response
from common.messages import (
    ACCOUNT_VERIFIED,
    INVALID_OTP,
    EMAIL_OTP_SENT,
    UNABLE_TO_SEND,
    USER_NOT_FOUND_EMAIL,
    PASSWORD_SUCCESS_RESET,
)
from users.api.v1.serializers import (
    UserRegisterSerializer,
    PostRegisterSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    UserOTPVerifySerializer,
    UpdateEmailSerializer,
    SocialSerializer,
    ForgetEmailSerializer,
    PasswordSerializer,
    ResetPasswordOTPVerifySerializer,
    OnboardingCompletedSerializer,
)
from users.models import User

from users.services.emails import (
    send_acc_verification_email,
    send_email_for_forgot_password,
)
from users.services.social_services import social_services


class UserRegistration(viewsets.ViewSet):
    @extend_schema(
        request=UserRegisterSerializer, responses={201: PostRegisterSerializer}
    )
    def create(self, request):
        request_data = request.data.copy()
        serializer = UserRegisterSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        # create new user
        user_obj = serializer.save()
        user_obj.is_active = True
        user_obj.save(update_fields=["is_active"])
        send_acc_verification_email(user_obj)
        return vj_response(
            PostRegisterSerializer(user_obj).data, status=HTTP_201_CREATED
        )


class VerifyOTP(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        request=UserOTPVerifySerializer, responses={200: PostRegisterSerializer}
    )
    def create(self, request):
        serializer = UserOTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user

        if user.is_email_verified:
            raise ValidationError(ACCOUNT_VERIFIED)

        if not hasattr(user, "account_verification_details"):
            raise ValidationError(INVALID_OTP)

        account_verification_details = user.account_verification_details
        if (
            not account_verification_details.email_otp
            == serializer.validated_data["code"]
        ):
            raise ValidationError(INVALID_OTP)
        else:
            user.is_email_verified = True
            account_verification_details.email_otp_verified_at = timezone.now()
            user.save()
            account_verification_details.save()

        return vj_response(PostRegisterSerializer(user).data)


class UpdateUserEmail(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        request=UpdateEmailSerializer, responses={200: PostRegisterSerializer}
    )
    def create(self, request):
        user = request.user
        serializer = UpdateEmailSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user.email = email
        user.username = email
        user.is_email_verified = False
        user.save(update_fields=["email", "username", "is_email_verified"])

        send_acc_verification_email(user)
        return vj_response(PostRegisterSerializer(user).data)


class ResendEmailOTP(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(responses={200: str})
    def list(self, request):
        user = request.user
        if not user.is_email_verified:
            send_acc_verification_email(user)
            return vj_response(EMAIL_OTP_SENT)
        else:
            raise ValidationError(UNABLE_TO_SEND)


class UserLogin(viewsets.ViewSet):
    @extend_schema(request=UserLoginSerializer, responses={200: PostRegisterSerializer})
    def create(self, request):
        request_data = request.data.copy()
        if request_data.get("email"):
            request_data["email"] = request_data["email"].lower()
        serializer = UserLoginSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        try:
            auth_token = user.auth_token
            auth_token.delete()
        except Token.DoesNotExist:
            pass
        return vj_response(PostRegisterSerializer(user).data)


class UserProfile(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, EmailVerified)

    @extend_schema(responses={200: UserProfileSerializer})
    def list(self, request):
        serializer = UserProfileSerializer(request.user)
        return vj_response(serializer.data)

    @extend_schema(
        request=UserProfileSerializer, responses={200: UserProfileSerializer}
    )
    def update(self, request, pk=None):
        serializer = UserProfileSerializer(
            request.user, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return vj_response(serializer.data)

    @extend_schema(
        request=OnboardingCompletedSerializer, responses={200: UserProfileSerializer}
    )
    @action(
        detail=False,
        methods=["post"],
        url_path="onboarding_completed",
        url_name="onboarding_completed",
    )
    def onboarding_completed(self, request):
        user = request.user
        serializer = OnboardingCompletedSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)

        onboarding = serializer.validated_data["onboarding_completed"]
        user.onboarding_completed = onboarding
        user.save()
        serializer = UserProfileSerializer(request.user)
        return vj_response(serializer.data)


class Logout(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, format=None):
        request.user.auth_token.delete()
        return vj_response("LOGGED OUT")


class GoogleLogin(viewsets.ViewSet):
    @extend_schema(request=SocialSerializer, responses={200: PostRegisterSerializer})
    def create(self, request):
        device = request.data.get("device", "ios")
        serializer = SocialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_info = social_services.google_user_details(
            serializer.validated_data["access_token"], device=device
        )
        user = SocialSerializer(context={"request": request}).social_login(user_info)

        try:
            auth_token = user.auth_token
            auth_token.delete()
        except Token.DoesNotExist:
            pass
        return vj_response(PostRegisterSerializer(user).data)


class AppleLogin(viewsets.ViewSet):
    @extend_schema(request=SocialSerializer, responses={200: PostRegisterSerializer})
    def create(self, request):
        serializer = SocialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_info = social_services.apple_user_details(
            serializer.validated_data["access_token"],
            serializer.validated_data.get("full_name"),
        )
        user = SocialSerializer(context={"request": request}).social_login(user_info)

        try:
            auth_token = user.auth_token
            auth_token.delete()
        except Token.DoesNotExist:
            pass
        return vj_response(PostRegisterSerializer(user).data)


class ForgetPasswordEmail(viewsets.ViewSet):
    @extend_schema(request=ForgetEmailSerializer, responses={200: EMAIL_OTP_SENT})
    def create(self, request):
        data = request.data
        serializer = ForgetEmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise ValidationError(USER_NOT_FOUND_EMAIL)

        send_email_for_forgot_password(user)
        return vj_response(EMAIL_OTP_SENT)


class VerifyResetPasswordOTP(viewsets.ViewSet):
    @extend_schema(
        request=ResetPasswordOTPVerifySerializer,
        responses={200: PostRegisterSerializer},
    )
    def create(self, request):
        serializer = ResetPasswordOTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise ValidationError(USER_NOT_FOUND_EMAIL)

        if not hasattr(user, "account_verification_details"):
            raise ValidationError(INVALID_OTP)

        account_verification_details = user.account_verification_details
        if not (
            account_verification_details.email_otp == serializer.validated_data["code"]
        ):
            raise ValidationError(INVALID_OTP)
        else:
            user.is_email_verified = False
            account_verification_details.email_otp_verified_at = timezone.now()
            user.save()
            account_verification_details.save()
            try:
                auth_token = user.auth_token
                auth_token.delete()
            except Token.DoesNotExist:
                pass
        return vj_response(PostRegisterSerializer(user).data)


class SetPassword(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(request=PasswordSerializer, responses={200: PostRegisterSerializer})
    def create(self, request):
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data["password"]
        user = request.user
        user.set_password(password)
        user.is_email_verified = True
        user.save()
        return vj_response(PostRegisterSerializer(user).data)
