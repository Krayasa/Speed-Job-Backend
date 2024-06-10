from rest_framework import serializers

from customuser.models import User, EmployeeProfile, EmployerProfile

class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs["partial"] = True
        super(UserSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        # fields = "__all__"
        exclude = ("password", "user_permissions", "groups", "is_staff", "is_active", "is_superuser", "last_login")
        
class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    resume = serializers.FileField(use_url=True)
    experience_letter = serializers.FileField(use_url=True)
    police_report = serializers.FileField(use_url=True)
    medical_report = serializers.FileField(use_url=True)
    offer_letter = serializers.FileField(use_url=True)
    work_permit = serializers.FileField(use_url=True)
    project_agreement = serializers.FileField(use_url=True)
    employment_requirement_agreement = serializers.FileField(use_url=True)
    visa = serializers.FileField(use_url=True)
    ticket = serializers.FileField(use_url=True)
    
    class Meta:
        model = EmployeeProfile
        fields = "__all__"
        
class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    resume = serializers.FileField(use_url=True)
    experience_letter = serializers.FileField(use_url=True)
    police_report = serializers.FileField(use_url=True)
    medical_report = serializers.FileField(use_url=True)
    offer_letter = serializers.FileField(use_url=True)
    work_permit = serializers.FileField(use_url=True)
    project_agreement = serializers.FileField(use_url=True)
    employment_requirement_agreement = serializers.FileField(use_url=True)
    visa = serializers.FileField(use_url=True)
    ticket = serializers.FileField(use_url=True)
    class Meta:
        model = EmployerProfile
        fields = "__all__"



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = ["email", "password", "password2", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        role = validated_data["role"]
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError({"password": "The two passwords differ."})
        user = User(email=email, role=role)
        user.set_password(password)
        user.save()
        return user


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token and provider.
    """

    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)
    
