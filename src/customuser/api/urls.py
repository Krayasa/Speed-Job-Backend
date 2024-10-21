from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenRefreshView

from .custom_claims import MyTokenObtainPairView
# from .views import EditEmployeeProfileAPIView, registration, EditEmployerProfileAPIView
from .views import registration
from oauth2_provider import urls as oauth2_urls


urlpatterns = [
    # path('login/', TokenObtainPairView.as_view()),
    path("register/", registration, name="register"),
    path("login/", MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('o/', include(oauth2_urls)),
    # path("employee/", include([path("profile/", EditEmployeeProfileAPIView.as_view(), name="employee-profile")])),
    # path("employer/", include([path("profile/", EditEmployerProfileAPIView.as_view(), name="employer-profile")])),

]
