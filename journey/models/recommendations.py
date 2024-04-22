from django.db import models
from common.models import BaseModel


# Create your models here.
class RecommendationType(BaseModel):
    class Meta:
        verbose_name = "Recommendation Types"
        verbose_name_plural = "Recommendation Types"

    image = models.ImageField(upload_to="recommendations/")
    label = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.label
