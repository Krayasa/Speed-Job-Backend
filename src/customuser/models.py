from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.documents import get_document_model
from customuser.managers import CustomUserManager

GENDER_CHOICES = (("male", "Male"), ("female", "Female"))
ROLE_CHOICES = (
    ("employer", "employer"),
    ("employee", "employee"),
)


@register_snippet
class User(AbstractUser):
    role = models.CharField(choices=ROLE_CHOICES,error_messages={"required": "Role must be provided"})
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10, blank=True, null=True, default="")
    email = models.EmailField(
        unique=True, blank=False, error_messages={"unique": "A user with that email already exists."}
    )
    cv = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="cv")
    passport = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="passport")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __unicode__(self):
        return self.email

    objects = CustomUserManager()
