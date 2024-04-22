from django.db import models


from common.models import BaseModel
from journey.enums import JOURNEY_MEDIA_TYPE_CHOICES


class JourneyMedia(BaseModel):
    class Meta:
        verbose_name = "Journey Media"
        verbose_name_plural = "Journey Media"

    media_type = models.CharField(choices=JOURNEY_MEDIA_TYPE_CHOICES, max_length=10)
    title = models.CharField(max_length=250)
    link = models.TextField()
    image = models.ImageField(upload_to="media_journey/")
