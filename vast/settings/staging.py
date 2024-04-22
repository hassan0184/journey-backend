from .base import *
print("Loading staging settings...")

# ALLOWED_HOSTS = ["journey-dev.projectvast.io"]
ALLOWED_HOSTS = ["journey-dev.projectvast.io"]


MEDIA_ROOT = "/media/"
STATIC_ROOT = "/static/"

STATICFILES_LOCATION = "static"
STATICFILES_STORAGE = "vast.storage_backend.StaticStorage"

MEDIAFILES_LOCATION = "media"
DEFAULT_FILE_STORAGE = "vast.storage_backend.MediaStorage"

AWS_S3_CUSTOM_DOMAIN = "d3tzzn5ci4hmjp.cloudfront.net"

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATIC_ROOT)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIA_ROOT)


SITE_HEADER = "VAST-DEV administration"
SITE_TITLE = "VAST-DEV administration"
DISABLE_OTP = True
