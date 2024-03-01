from django.urls import path, include

from vendor_api.views.shop import (
    ServiceListView,
    CreateServiceView,
    ServiceUpdateView,
)


urlpatterns = [
    # GET localhost/vendor/service/
    path(
        route="service/",
        view=ServiceListView.as_view(),
        name="services",
    ),
    # GET localhost/vendor/service/create/
    path(
        route="service/create/",
        view=CreateServiceView.as_view(),
        name="service_create",
    ),
    # GET localhost/vendor/service/update/
    path(
        route="service/update/",
        view=ServiceUpdateView.as_view(),
        name="service_update",
    ),
    path("", include("vendor_api.token_api.urls")),
    path("", include("vendor_api.register_api.urls")),
]
