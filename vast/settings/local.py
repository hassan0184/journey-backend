from .base import *


CORS_ALLOWED_ORIGINS = [
    "*"
]


CORS_ALLOW_CREDENTIALS = True  
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
] 
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
] 

ALLOWED_HOSTS = [
    '*'
]

AWS_S3_CUSTOM_DOMAIN = ""

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

SITE_HEADER = "VAST-LOCAL administration"
SITE_TITLE = "VAST-LOCAL administration"
DISABLE_OTP = True
DEBUG=True