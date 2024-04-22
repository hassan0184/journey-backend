from django.db import models
import uuid

# Create your models here.
from users.enums import HERO_TYPE_CHOICES
from common.models import BaseModel


class RoleType(BaseModel):
    class Meta:
        verbose_name = "Role Types"
        verbose_name_plural = "Role Types"

    type = models.CharField(choices=HERO_TYPE_CHOICES, null=True, blank=True)
    label = models.CharField(max_length=30, unique=True)
    label_description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class HeroTypes(BaseModel):
    class Meta:
        verbose_name = "Hero Types"
        verbose_name_plural = "Hero Types"

    label = models.CharField(max_length=30, unique=True)
    role_type = models.ForeignKey(
        RoleType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="role_hero",
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.label
