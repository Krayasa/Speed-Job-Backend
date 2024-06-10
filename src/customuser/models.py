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
   
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __unicode__(self):
        return self.email

    objects = CustomUserManager()
    
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer_profile")
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_phone = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.URLField(max_length=255, blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee_profile")
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
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


    def __str__(self):
        return self.name