from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        "email",
        "user_name",
        "first_name",
        "is_freelancer","is_client","is_job_seeker"
    )
    list_filter = ("email", "user_name", "first_name", "is_active", "is_staff","is_freelancer","is_client","is_job_seeker")
    ordering = ("-start_date",)
    list_display = ("email", "user_name", "first_name", "is_active", "is_staff","is_freelancer","is_client","is_job_seeker")
    fieldsets = (
        (
            None,
            {
                "fields": (
                "email",
                "user_name",
                "first_name",
                "password",
                "is_freelancer",
                "is_client",
                "is_job_seeker",
            )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Personal", {"fields": ("about",)}),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "password",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_freelancer","is_client","is_job_seeker"
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
