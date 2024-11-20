from rest_framework import serializers
from wagtail.documents import get_document_model

from customuser.api.serializers import UserSerializer
# from tags.api.serializers import TagSerializer
from jobs.models import Job, Applicant
from rest_framework.pagination import PageNumberPagination


# class JobSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     job_tags = serializers.SerializerMethodField()

#     class Meta:
#         model = Job
#         fields = "__all__"

#     def get_job_tags(self, obj):
#         if obj.tags:
#             return TagSerializer(obj.tags.all(), many=True).data
#         else:
#             return None


# class DashboardJobSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     job_tags = serializers.SerializerMethodField()
#     total_candidates = serializers.SerializerMethodField()

#     class Meta:
#         model = Job
#         fields = "__all__"

#     def get_job_tags(self, obj):
#         if obj.tags:
#             return TagSerializer(obj.tags.all(), many=True).data
#         else:
#             return None

#     def get_total_candidates(self, obj):
#         return obj.applicants.count()


# class NewJobSerializer(serializers.ModelSerializer):
#     user = UserSerializer(default=serializers.CurrentUserDefault())

#     class Meta:
#         model = Job
#         fields = "__all__"


# class ApplyJobSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Applicant
#         fields = ("job")


# class ApplicantSerializer(serializers.ModelSerializer):
#     applied_user = serializers.SerializerMethodField()
#     job = serializers.SerializerMethodField()
#     status = serializers.SerializerMethodField()

#     class Meta:
#         model = Applicant
#         fields = ("id", "job_id", "applied_user", "job", "status", "created_at", "comment")

#     def get_status(self, obj):
#         return obj.get_status

#     def get_job(self, obj):
#         return JobSerializer(obj.job).data

#     def get_applied_user(self, obj):
#         return UserSerializer(obj.user).data


# class AppliedJobSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     applicant = serializers.SerializerMethodField("_applicant")

#     class Meta:
#         model = Job
#         fields = "__all__"

#     def _applicant(self, obj):
#         user = self.context.get("request", None).user
#         return ApplicantSerializer(Applicant.objects.get(user=user, job=obj)).data

class ApplicantSerializer(serializers.ModelSerializer):
    applied_user = serializers.SerializerMethodField()
    job = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Applicant
        fields = ("id", "job", "applied_user", "status", "created_at", "comment")

    def get_status(self, obj):
        return obj.get_status

    def get_job(self, obj):
        return JobSerializer(obj.job).data

    def get_applied_user(self, obj):
        return UserSerializer(obj.user).data
    
class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    job_offer_letter = serializers.FileField(use_url=True)
    job_work_permit = serializers.FileField(use_url=True)
    job_project_agreement = serializers.FileField(use_url=True)
    job_employment_requirement_agreement = serializers.FileField(use_url=True)
    # job_tags = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"

    # def get_job_tags(self, obj):
    #     return TagSerializer(obj.tags.all(), many=True).data


class DashboardJobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    applicants = ApplicantSerializer(many=True, read_only=True)
    job_offer_letter = serializers.FileField(use_url=True)
    job_work_permit = serializers.FileField(use_url=True)
    job_project_agreement = serializers.FileField(use_url=True)
    job_employment_requirement_agreement = serializers.FileField(use_url=True)
    # job_tags = serializers.SerializerMethodField()
    total_candidates = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"        


    # def get_job_tags(self, obj):
    #     return TagSerializer(obj.tags.all(), many=True).data

    def get_total_candidates(self, obj):
        return obj.applicants.count()


class NewJobSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    job_offer_letter = serializers.FileField(use_url=True, required=False, allow_null=True)
    job_work_permit = serializers.FileField(use_url=True, required=False, allow_null=True)
    job_project_agreement = serializers.FileField(use_url=True, required=False, allow_null=True)
    job_employment_requirement_agreement = serializers.FileField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Job
        fields = "__all__"
        
    def create_or_update_document(self, validated_data, field_name):
        if field_name in validated_data:
            document_model = get_document_model()
            document_instance = document_model.objects.create(file=validated_data[field_name])
            validated_data[field_name] = document_instance

    def update(self, instance, validated_data):
        document_fields = [
            'job_offer_letter', 'job_work_permit', 'job_project_agreement', 'job_employment_requirement_agreement'
        ]
        for field in document_fields:
            self.create_or_update_document(validated_data, field)
        
        return super().update(instance, validated_data)

    def create(self, validated_data):
        document_fields = [
            'job_offer_letter', 'job_work_permit', 'job_project_agreement', 'job_employment_requirement_agreement'
        ]
        for field in document_fields:
            self.create_or_update_document(validated_data, field)

        return super().create(validated_data)


class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ("job",)





class AppliedJobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    applicant = serializers.SerializerMethodField("_applicant")

    class Meta:
        model = Job
        fields = "__all__"

    def _applicant(self, obj):
        user = self.context.get("request", None).user
        try:
            return ApplicantSerializer(Applicant.objects.get(user=user, job=obj)).data
        except Applicant.DoesNotExist:
            return None
