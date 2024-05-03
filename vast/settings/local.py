from .base import *


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Add your React.js frontend URL here
    "http://44.210.118.15:8000",
    # Add other allowed origins as needed
]

# Optional CORS configuration
CORS_ALLOW_CREDENTIALS = True  # Allow cookies to be included in CORS requests
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]  # Add headers you want to allow in CORS requests
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]  # Add HTTP methods you want to allow in CORS requests

AWS_S3_CUSTOM_DOMAIN = ""

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

SITE_HEADER = "VAST-LOCAL administration"
SITE_TITLE = "VAST-LOCAL administration"
DISABLE_OTP = True
