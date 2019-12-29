from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from basic_email_user.models import User
from basic_email_user.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ((None), {
            'fields': (
                "id", "email", "password",
            )
        }),
        (("Personal info"), {
            'fields': (
                "name",
            )
        }),
        (("Permissions"), {
            'fields': (
                "is_active", "is_staff", "is_superuser", "groups",
                "user_permissions",
            ),
        }),
        (("Important dates"), {
            'fields': (
                "last_login", "date_joined",
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ("wide",),
            'fields': ("email", "name", "password1", "password2",)
        }),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = (
        "id", "email", "name", "is_staff",
    )
    readonly_fields = ("id",)
    search_fields = ("name", "email",)
    ordering = ("name",)


admin.site.register(User, CustomUserAdmin)
