from django.contrib.auth import get_user_model, login
from requests.exceptions import HTTPError
from rest_framework import decorators, permissions, response, status
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customuser.models import EmployeeProfile, EmployerProfile
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser


from jobs.api.permissions import IsEmployee, IsEmployer

from .custom_claims import MyTokenObtainPairSerializer
from .serializers import UserCreateSerializer, UserSerializer, EmployeeProfileSerializer, EmployerProfileSerializer

User = get_user_model()


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)

    if not serializer.is_valid(raise_exception=True):
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    res = {"status": True, "message": "Successfully registered"}
    return response.Response(res, status.HTTP_201_CREATED)


# class EditEmployeeProfileAPIView(GenericAPIView):
#     serializer_class = EmployeeProfileSerializer
#     permission_classes = [IsAuthenticated, IsEmployee]
#     parser_classes = [MultiPartParser]
#     http_method_names = ['patch', 'put', 'get','post']

#     def get_object(self):
#         profile, created = EmployeeProfile.objects.get_or_create(user=self.request.user)
#         return profile

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
        
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', True)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)
    


# class EditEmployerProfileAPIView(GenericAPIView):
#     serializer_class = EmployerProfileSerializer
#     permission_classes = [IsAuthenticated, IsEmployer]
#     http_method_names = ['patch', 'put', 'get','post']


#     def get_object(self):
#         profile, created = EmployerProfile.objects.get_or_create(user=self.request.user)
#         return profile

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
        
    
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', True)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         print(serializer)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)
        

# class SocialLoginAPIView(GenericAPIView):
#     """Log in using facebook"""

#     serializer_class = SocialSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         """Authenticate user through the provider and access_token"""
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         provider = serializer.data.get("provider", None)
#         strategy = load_strategy(request)

#         try:
#             backend = load_backend(strategy=strategy, name=provider, redirect_uri=None)

#         except MissingBackend:
#             return Response({"error": "Please provide a valid provider"}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             if isinstance(backend, BaseOAuth2):
#                 access_token = serializer.data.get("access_token")
#             user = backend.do_auth(access_token)
#         except HTTPError as error:
#             return Response(
#                 {"error": {"access_token": "Invalid token", "details": str(error)}}, status=status.HTTP_400_BAD_REQUEST
#             )
#         except AuthTokenError as error:
#             return Response({"error": "Invalid credentials", "details": str(error)}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             authenticated_user = backend.do_auth(access_token, user=user)

#         except HTTPError as error:
#             return Response({"error": "invalid token", "details": str(error)}, status=status.HTTP_400_BAD_REQUEST)

#         except AuthForbidden as error:
#             return Response({"error": "invalid token", "details": str(error)}, status=status.HTTP_400_BAD_REQUEST)

#         if authenticated_user and authenticated_user.is_active:
#             # generate JWT token
#             login(request, authenticated_user)
#             # data = {"token": jwt_encode_handler(jwt_payload_handler(user))}
#             # token = RefreshToken.for_user(user)
#             token = MyTokenObtainPairSerializer.get_token(user)
#             # customized response
#             context = {
#                 "email": authenticated_user.email,
#                 "role": authenticated_user.role,
#                 "username": authenticated_user.username,
#                 "access": str(token.access_token),
#                 "refresh": str(token),
#             }

#             return Response(status=status.HTTP_200_OK, data=context)

# Create Employee Profile
class CreateEmployeeProfileAPIView(CreateAPIView):
    serializer_class = EmployeeProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployee]
    parser_classes = [MultiPartParser]
    
    def create(self, request, *args, **kwargs):
        # Allow partial creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # Save the profile with the authenticated user
        serializer.save(user=self.request.user)

# Update Employee Profile
class UpdateEmployeeProfileAPIView(UpdateAPIView):
    serializer_class = EmployeeProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployee]
    parser_classes = [MultiPartParser]

    def get_object(self):
        return EmployeeProfile.objects.get(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete Employee Profile
class DeleteEmployeeProfileAPIView(DestroyAPIView):
    serializer_class = EmployeeProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def get_object(self):
        return EmployeeProfile.objects.get(user=self.request.user)

# Retrieve Employee Profile
class RetrieveEmployeeProfileAPIView(RetrieveAPIView):
    serializer_class = EmployeeProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def get_object(self):
        try:
            return EmployeeProfile.objects.get(user=self.request.user)
        except EmployeeProfile.DoesNotExist:
            return None  # Return None if the profile does not exist

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile is None:
            return Response({"error": "Employee profile not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(profile)
        return Response(serializer.data)

# Create Employer Profile
class CreateEmployerProfileAPIView(CreateAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployer]
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        # Allow partial creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # Save the profile with the authenticated user
        serializer.save(user=self.request.user)

# Update Employer Profile
class UpdateEmployerProfileAPIView(UpdateAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployer]
    parser_classes = [MultiPartParser]

    def get_object(self):
        return EmployerProfile.objects.get(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete Employer Profile
class DeleteEmployerProfileAPIView(DestroyAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployer]

    def get_object(self):
        return EmployerProfile.objects.get(user=self.request.user)

# Retrieve Employer Profile
class RetrieveEmployerProfileAPIView(RetrieveAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployer]

    def get_object(self):
        try:
            return EmployerProfile.objects.get(user=self.request.user)
        except EmployerProfile.DoesNotExist:
            return None  # Return None if the profile does not exist

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile is None:
            return Response({"error": "Employer profile not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(profile)
        return Response(serializer.data)
