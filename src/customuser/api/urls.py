from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenRefreshView

from .custom_claims import MyTokenObtainPairView
from .views import EditEmployeeProfileAPIView, registration

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view()),
    path("register/", registration, name="register"),
    path("login/", MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("employee/", include([path("profile/", EditEmployeeProfileAPIView.as_view(), name="employee-profile")])),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
    # path("oauth/login/", SocialLoginAPIView.as_view()),
]
