from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path, include

from vendor_api.views.shop import (
    ServiceListView,
    CreateServiceView,
    ServiceUpdateView,
)

from .views.token import CustomTokenObtainPairView


urlpatterns = [
    # POST localhost:8092/vendor/login/
    path(
        route="login/",
        view=CustomTokenObtainPairView.as_view(),
        name="vendor_login",
    ),
    # POST localhost:8092/vendor/login/refresh/
    path(
        route="login/refresh/",
        view=TokenRefreshView.as_view(),
        name="vendor_login_refresh",
    ),
    # GET localhost:8092/vendor/service/
    path(
        route="service/",
        view=ServiceListView.as_view(),
        name="services",
    ),
    # POST localhost:8092/vendor/service/create/
    path(
        route="service/create/",
        view=CreateServiceView.as_view(),
        name="service_create",
    ),
    # PATCH localhost:8092/vendor/service/update/
    path(
        route="service/update/",
        view=ServiceUpdateView.as_view(),
        name="service_update",
    ),
    path("register/", include("vendor_api.register_api.urls")),
]
