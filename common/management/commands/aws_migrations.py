import boto3
from django.core.management.base import BaseCommand
from django.conf import settings
from .images import MEDIA_IMAGES

aws_access_key_id = settings.AWS_ACCESS_KEY_ID
aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY


class Command(BaseCommand):
    def handle(self, *args, **options):
        # destination_s3 = boto3.client(
        #     "s3",
        #     aws_access_key_id=aws_access_key_id,
        #     aws_secret_access_key=aws_secret_access_key,
        # )

        # # Copy object from source bucket to destination bucket
        # source_bucket = "vast-media"
        # destination_bucket = "vast-journey-dev"
        # for key, value in MEDIA_IMAGES.items():
        #     source_key = value

        #     destination_key = "media/discovery/media/" + value
        #     try:
        #         copy_source = {"Bucket": source_bucket, "Key": source_key}
        #         destination_s3.copy_object(
        #             CopySource=copy_source, Bucket=destination_bucket, Key=destination_key
        #         )
        #     except Exception as e:
        #         print(key, value)
        #         print(f"Error: {e}")

        #         continue
        print(len(set(MEDIA_IMAGES.values())))
