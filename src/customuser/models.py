from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.snippets.models import register_snippet


from customuser.managers import UserManager

GENDER_CHOICES = (("male", "Male"), ("female", "Female"))

@register_snippet
class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={"required": "Role must be provided"})
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(
        unique=True, blank=False, error_messages={"unique": "A user with that email already exists."}
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
