from django.contrib.auth import get_user_model, login
from requests.exceptions import HTTPError
from rest_framework import decorators, permissions, response, status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from customuser.models import EmployeeProfile, EmployerProfile
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser
# from social_core.backends.oauth import BaseOAuth2
# from social_core.exceptions import AuthForbidden, AuthTokenError, MissingBackend
# from social_django.utils import load_backend, load_strategy

from jobs.api.permissions import IsEmployee, IsEmployer

from .custom_claims import MyTokenObtainPairSerializer
from .serializers import SocialSerializer, UserCreateSerializer, UserSerializer, EmployeeProfileSerializer, EmployerProfileSerializer

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


class EditEmployeeProfileAPIView(RetrieveUpdateAPIView, CreateAPIView):
    serializer_class = EmployeeProfileSerializer
    http_method_names = ["get", "put", "post"]
    permission_classes = [IsAuthenticated, IsEmployee]
    parser_classes = [MultiPartParser]

    def get_object(self):
        try:
            return self.request.user.employee_profile
        except EmployeeProfile.DoesNotExist:
            return None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []

        return super().get_parsers()

class EditEmployerProfileAPIView(RetrieveUpdateAPIView, CreateAPIView):
    serializer_class = EmployerProfileSerializer
    http_method_names = ["get", "put", "post"]
    permission_classes = [IsAuthenticated, IsEmployer]
    parser_classes = [MultiPartParser]

    def get_object(self):
        try:
            return self.request.user.employer_profile
        except EmployerProfile.DoesNotExist:
            return None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
    
        return super().get_parsers()


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
