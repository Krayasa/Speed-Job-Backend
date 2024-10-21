from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenRefreshView

from .custom_claims import MyTokenObtainPairView
from .views import *
from oauth2_provider import urls as oauth2_urls


urlpatterns = [
    # path('login/', TokenObtainPairView.as_view()),
    path("register/", registration, name="register"),
    path("login/", MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('o/', include(oauth2_urls)),
 # Employee profile
    path("employee/profile/create/", CreateEmployeeProfileAPIView.as_view(), name="employee-profile-create"),
    path("employee/profile/update/", UpdateEmployeeProfileAPIView.as_view(), name="employee-profile-update"),
    path("employee/profile/delete/", DeleteEmployeeProfileAPIView.as_view(), name="employee-profile-delete"),
    path("employee/profile/", RetrieveEmployeeProfileAPIView.as_view(), name="employee-profile-get"),

    # Employer profile
    path("employer/profile/create/", CreateEmployerProfileAPIView.as_view(), name="employer-profile-create"),
    path("employer/profile/update/", UpdateEmployerProfileAPIView.as_view(), name="employer-profile-update"),
    path("employer/profile/delete/", DeleteEmployerProfileAPIView.as_view(), name="employer-profile-delete"),
    path("employer/profile/", RetrieveEmployerProfileAPIView.as_view(), name="employer-profile-get"),

]
