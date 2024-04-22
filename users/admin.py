from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Register/Display User Model to Django Admin
    """

    fieldsets = (
        (
            None,
            {"fields": ("username", "email", "password", "email_otp")},
        ),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (_("Profile info"), {"fields": ("is_ally",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_email_verified",
                    "terms_and_conditions_accepted",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )
    ordering = ("-created_at",)
