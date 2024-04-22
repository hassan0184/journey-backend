from django.db import models

# Create your models here.
import uuid

# Create your models here.
from users.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_by",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_by",
    )


class Gender(BaseModel):
    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Gender"

    label = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class Ethnicity(BaseModel):
    class Meta:
        verbose_name = "Ethnicity"
        verbose_name_plural = "Ethnicity"

    label = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class AgeGroup(BaseModel):
    class Meta:
        verbose_name = "Age Group"
        verbose_name_plural = "Age Group"

    label = models.CharField(max_length=50, unique=True)
    min_age = models.IntegerField()
    max_age = models.IntegerField()

    def __str__(self):
        return self.label
