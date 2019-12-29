from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):

    def validate_email(self, email):
        """ Verify email arguemnt and return normalised value

        :param email: expect str
        :returns: normalised email str if correct
        :raises ValueError: invalid param email
        :raises Exception: existing email
        """
        if email is None:
            raise ValueError("Missing email value")
        elif type(email) is not str:
            raise ValueError("Invalid email value, expect str")

        normalized_email = self.normalize_email(email)

        existing_email = \
            self.model.objects.filter(email=normalized_email).first()

        if existing_email:
            raise Exception("This email is already assigned to another User")

        return normalized_email

    def create_user(self, email, name, password=None):
        """ Creates and saves a User

        :param email: expect str
        :param name: expect str
        :param password: expect str or None, default None
        :returns: User model
        """
        user = self.model(
            email=self.validate_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """ Creates and saves a User with superuser privileges

        :param email: expect str
        :param name: expect str
        :param password: expect str or None, default None
        :returns: User model
        """
        user = self.model(
            email=self.validate_email(email),
            name=name
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """ User model class (AbstractUser with modified properties)

    removes: username, first_name, last_name
    adds: name
    """
    email = models.EmailField(
        verbose_name="email address",
        error_messages={
            'unique': "A user with that email already exists.",
        },
        help_text="Required. 150 characters or fewer.",
        max_length=150,
        unique=True,
        validators=[EmailValidator],
    )
    username = None
    first_name = None
    last_name = None
    name = models.CharField(
        verbose_name="name",
        max_length=150,
        help_text=(
            "Required. 150 characters or fewer. "
            "Letters, digits and @/./+/-/_ only."
        ),
        validators=[UnicodeUsernameValidator]
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        db_table = "users"
