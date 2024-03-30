from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path, include

from .views.register import CustomerRegisterView
from .views.login import CustomTokenObtainPairView


urlpatterns = [
    # POST localhost:8092/customer/register/
    path(
        route="register/",
        view=CustomerRegisterView.as_view(),
        name="customer_register",
    ),
    # POST localhost:8092/customer/login/
    path(
        route="login/",
        view=CustomTokenObtainPairView.as_view(),
        name="customer_login",
    ),
    # POST localhost:8092/customer/login/refresh/
    path(
        route="login/refresh/",
        view=TokenRefreshView.as_view(),
        name="customer_login_refresh",
    ),
]
