from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from basic_email_user.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = tuple(
            x for x in UserCreationForm.Meta.fields
            if x not in ["username"]
        ) + ("name",)
        # field_classes = None


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'
        # field_classes = None
