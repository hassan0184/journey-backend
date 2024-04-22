from .base import *


ALLOWED_HOSTS = ["*"]
AWS_S3_CUSTOM_DOMAIN = ""

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

SITE_HEADER = "VAST-LOCAL administration"
SITE_TITLE = "VAST-LOCAL administration"
DISABLE_OTP = True
