from django.db import models
from django.urls import reverse
from django.utils import timezone
from wagtail.snippets.models import register_snippet
from wagtail.documents import get_document_model

from customuser.models import User

from taggit.managers import TaggableManager

from .manager import JobManager

JOB_TYPE = (("FullTime", "Full time"), ("PartTime", "Part time"), ("Contract", "Contract"))
ALLOWANCE = (("Yes", "Yes"), ("No", "No"))
GENDER = (("Male", "Male"), ("Female", "Female"), ("Any", "Any"))

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    salary = models.CharField(blank=True, default="")
    food_allowance = models.CharField(choices=ALLOWANCE, max_length=10, null=True, blank=True)
    accommodation = models.CharField(choices=ALLOWANCE, max_length=10, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, null=True, blank=True)
    working_hours = models.CharField(max_length=100, null=True, blank=True)
    working_days = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    tags = TaggableManager()
    vacancy = models.IntegerField(default=1)
    job_offer_letter = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="job_offer_letter")
    job_work_permit = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="job_work_permit")
    job_project_agreement = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="job_project_agreement")
    job_employment_requirement_agreement = models.ForeignKey(get_document_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="job_employment_requirement_agreement")
    

    objects = JobManager()

    class Meta:
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse("jobs:jobs-detail", args=[self.id])

    def __str__(self):
        return self.title

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants")
    created_at = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ["id"]
        unique_together = ["user", "job"]

    def __str__(self):
        return self.user.get_full_name()

    @property
    def get_status(self):
        if self.status == 1:
            return "Pending"
        elif self.status == 2:
            return "Accepted"
        else:
            return "Rejected"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(default=timezone.now)
    soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.job.title
