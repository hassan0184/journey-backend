from django.contrib.auth import authenticate
from django.db import transaction
from django.db.models import Q
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from drf_extra_fields.fields import Base64ImageField

from common.messages import (
    EMAIL_ALREADY_USED,
    ACCEPT_TERMS_AND_CONDITIONS,
    USER_DOESNOT_EXIST,
    INVALID_CREDENTIALS,
    INCLUDE_EMAIL_PASSWORD,
    EMAIL_REQUIRED,
    CANNOT_UPDATE_EMAIL,
    USER_NOT_FOUND_EMAIL,
    INVALID_REF_CODE,
)
from journey.models import Allies
from users.enums import HERO_TYPE_CHOICES
from users.models import User
from users.services.social_services import social_services


class UserRegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    terms_and_conditions_accepted = serializers.BooleanField(required=True)
    ref_by = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "terms_and_conditions_accepted",
            "password",
            "ref_by",
        )

    def validate(self, data):
        res = super(UserRegisterSerializer, self).validate(data)
        email = data.get("email").lower()
        ref_by = data.get("ref_by")
        privacy_policy = data.get("terms_and_conditions_accepted")
        q2 = Q(email=email)

        if User.objects.filter(q2).exists():
            raise ValidationError(EMAIL_ALREADY_USED)

        if not privacy_policy:
            raise ValidationError(ACCEPT_TERMS_AND_CONDITIONS)

        if ref_by:
            if not Allies.objects.filter(
                invite_code=ref_by, user__isnull=True
            ).exists():
                raise ValidationError(INVALID_REF_CODE)

        res["username"] = email
        res["email"] = email.lower()
        return res

    def create(self, validated_data):
        with transaction.atomic():
            # challenge_info = validated_data.pop("challenge_info")
            user = super(UserRegisterSerializer, self).create(validated_data)
            ref_by = validated_data.get("ref_by", None)
            user.set_password(validated_data["password"])
            user.is_active = True
            name = user.full_name.split()
            user.first_name = name[0]
            if len(name) > 1:
                user.last_name = name[1]
            user.save()

            if ref_by:
                allies = Allies.objects.filter(invite_code=ref_by, user__isnull=True)
                if allies.exists():
                    ally = allies.first()
                    ally.user = user
                    ally.invite_code = ""
                    ally.save()
                    user.is_ally = True
                    user.save()
        return user


class PostRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    # invited_by = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "terms_and_conditions_accepted",
            # "ref_by",
            # "ref_code",
            "is_email_verified",
            "token",
            "is_ally",
            "onboarding_completed",
        )

    # def get_invited_by(self, obj):
    #
    #
    #     if hasattr(obj, "user_ally_details"):
    #         invited_by = obj.user_ally_details.invited_by
    #         return invited_by.email
    #     else:
    #         return None

    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key


class UserOTPVerifySerializer(serializers.Serializer):
    code = serializers.CharField()


class UpdateEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = ("user", "email")

    def validate(self, data):
        email = data.get("email")
        user = data.get("user")
        if not user.email or not email:
            raise ValidationError(EMAIL_REQUIRED)
        if user.is_email_verified:
            raise ValidationError(CANNOT_UPDATE_EMAIL)
        if email:
            email = email.lower()
            if user.email.lower() != email:
                if (
                    User.objects.filter(
                        email=email, is_email_verified=True, username=email
                    )
                    .exclude(id=user.id)
                    .exists()
                ):
                    raise ValidationError(EMAIL_ALREADY_USED)

        return data


class UserLoginSerializer(serializers.Serializer):
    """
    User Login Serializer
    """

    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise ValidationError(USER_DOESNOT_EXIST)

            user = authenticate(
                request=self.context.get("request"),
                username=user.username,
                password=password,
            )
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                raise ValidationError(INVALID_CREDENTIALS)
        else:
            raise ValidationError(INCLUDE_EMAIL_PASSWORD)

        attrs["user"] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(required=False)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "avatar",
            "onboarding_completed",
        )

    def update(self, instance, validated_data):
        email = validated_data.get("email")
        if email:
            email = email.lower()
            if User.objects.filter(email=email).exclude(id=instance.id).exists():
                raise ValidationError(EMAIL_ALREADY_USED)
            validated_data["email"] = email.lower()
        return super(UserProfileSerializer, self).update(instance, validated_data)


class SocialSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    full_name = serializers.CharField(max_length=100, required=False)
    ref_by = serializers.CharField(max_length=100, required=False)

    def social_login(self, user_info):
        try:
            user = User.objects.get(
                email__iexact=user_info["email"], username__iexact=user_info["email"]
            )
            user.is_email_verified = True
        except User.DoesNotExist:
            user_dict = social_services.get_user_social_dict(user_info)
            user = User(**user_dict)
            user.set_unusable_password()
            user.is_email_verified = True
        user.save()
        return user


class ForgetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        res = super(ForgetEmailSerializer, self).validate(data)
        email = data.get("email").lower()

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise ValidationError(USER_NOT_FOUND_EMAIL)

        res["email"] = email.lower()
        return res


class ResetPasswordOTPVerifySerializer(serializers.Serializer):
    code = serializers.CharField()
    email = serializers.EmailField()


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()


class OnboardingCompletedSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = ("user", "onboarding_completed")
