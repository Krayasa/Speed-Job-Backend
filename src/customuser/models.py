from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.documents import get_document_model
from customuser.managers import CustomUserManager

# GENDER_CHOICES = (("male", "Male"), ("female", "Female"))
ROLE_CHOICES = (
    ("employer", "employer"),
    ("employee", "employee"),
)


class User(AbstractUser):
    username = None
    role = models.CharField(choices=ROLE_CHOICES,error_messages={"required": "Role must be provided"})
    # gender = models.CharField(choices=GENDER_CHOICES,max_length=10, blank=True, null=True, default="")
    email = models.EmailField(
        unique=True, blank=False, error_messages={"unique": "A user with that email already exists."}
    )
    document1 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document1")
    document2 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document2")
    document3 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document3")
    document4 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document4")
    document5 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document5")
    document6 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document6")
    document7 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document7")
    document8 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document8")
    document9 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document9")
    document10 = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="document10")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __unicode__(self):
        return self.email

    objects = CustomUserManager()
