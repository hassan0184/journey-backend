import requests
import base64
from datetime import timedelta

import jwt
from google.oauth2 import id_token
from google.auth.transport import requests as google_auth_request
from django.utils import timezone
from django.conf import settings
from rest_framework.exceptions import ValidationError


class social_services:
    @classmethod
    def get_user_social_dict(cls, user):
        user_dict = {"email": user.get("email"), "username": user.get("email")}
        user_dict["first_name"] = user.get("first_name", "")
        user_dict["last_name"] = user.get("last_name", "")
        if user.get("name"):
            user_dict["first_name"] = user.get("name")
        return user_dict

    @classmethod
    def google_user_details(cls, access_token, device=None):
        try:
            if device == "ios":
                GOOGLE_CLIENT_ID = settings.IOS_GOOGLE_CLIENT_ID
            elif device == "android":
                GOOGLE_CLIENT_ID = settings.AND_GOOGLE_CLIENT_ID
            else:
                raise ValidationError("Invalid device")
            idinfo = id_token.verify_oauth2_token(
                access_token, google_auth_request.Request(), GOOGLE_CLIENT_ID
            )
            if idinfo["iss"] not in [
                "accounts.google.com",
                "https://accounts.google.com",
            ]:
                raise Exception("Wrong issuer.")
        except ValueError as e:
            raise ValidationError(str(e))
        user_info = {}
        user_info["id"] = idinfo["sub"]
        user_info["email"] = idinfo["email"]
        user_info["name"] = idinfo["name"]
        return user_info

    @classmethod
    def apple_user_details(cls, access_token, name):
        apple_client_id = settings.APPLE_CLIENT_ID
        client_id, client_secret = cls.get_key_and_secret(apple_client_id)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": access_token,
            "grant_type": "authorization_code",
        }

        response = requests.post(
            settings.APPLE_ACCESS_TOKEN_URL, data=data, headers=headers
        )
        response_dict = response.json()
        if response_dict.get("error", ""):
            raise ValidationError("Invalid access token")
        id_token = response_dict.get("id_token")  # contains user information
        decoded = jwt.decode(id_token, "", verify=False)
        user_info = {}
        user_info["id"] = decoded["sub"]
        user_info["email"] = decoded["email"]
        user_info["name"] = name
        return user_info

    @classmethod
    def get_key_and_secret(cls, apple_client_id):
        key = cls.get_apple_private_key()
        headers = {"kid": settings.APPLE_KEY_ID}

        payload = {
            "iss": settings.APPLE_TEAM_ID,
            "iat": timezone.now(),
            "exp": timezone.now() + timedelta(days=180),
            "aud": "https://appleid.apple.com",
            "sub": apple_client_id,
        }
        client_secret = jwt.encode(
            payload, key, algorithm="ES256", headers=headers
        ).decode("utf-8")
        return apple_client_id, client_secret

    @classmethod
    def get_apple_private_key(cls):
        B64_BYTES = settings.ENC_APPLE_PRIVATE_KEY.encode("ascii")
        KEY_BYTES = base64.b64decode(B64_BYTES)
        return KEY_BYTES.decode("ascii")
