from .base import *

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.0:8000',
    'http://44.210.118.15:8000/',
    'http://localhost:3000/',
]
AWS_S3_CUSTOM_DOMAIN = ""

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

SITE_HEADER = "VAST-LOCAL administration"
SITE_TITLE = "VAST-LOCAL administration"
DISABLE_OTP = True
