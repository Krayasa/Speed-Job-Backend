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
    resume = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="resume")
    experience_letter = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="experience_letter")
    police_report = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="police_report")
    medical_report = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="medical_report")
    offer_letter = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="offer_letter")
    work_permit = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="work_permit")
    project_agreement = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="project_agreement")
    employment_requirement_agreement = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="employment_requirement_agreement")
    visa = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="visa")
    ticket = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="ticket")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __unicode__(self):
        return self.email

    objects = CustomUserManager()
