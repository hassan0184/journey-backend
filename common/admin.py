from django.contrib import admin
from common.models import Gender, Ethnicity, AgeGroup

# Register your models here.


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")


@admin.register(Ethnicity)
class EthnicityAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "is_active")
    ordering = ("-created_at",)
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")


@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ("label",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    exclude = ("created_by", "updated_by")
