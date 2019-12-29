# Django Basic Email User

Used to replace default Django User model with 'email', instead of the 'username', as the unique identifer. Also removes ['username', 'first_name', 'last_name'] fields and adding a 'name' field (required).

The Django admin panel is customised to accommodate these changes, along with the User forms basic_email_user.forms.CustomUserCreationForm and basic_email_user.forms.CustomUserChangeForm

Simply add basic_email_user to your installed apps, configure the AUTH_USER_MODEL, and run the migrations

```
INSTALLED_APPS = [
    ...
    'basic_email_user'
]

AUTH_USER_MODEL = 'basic_email_user.User'
```