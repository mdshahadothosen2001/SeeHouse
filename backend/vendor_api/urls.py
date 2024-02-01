from django.urls import path, include

from .views import ServiceView


urlpatterns = [
    # GET localhost/vendor/service/
    path(
        route="service/",
        view=ServiceView.as_view(),
        name="services",
    ),
    
    path("", include("vendor_api.token_api.urls")),
    path("", include("vendor_api.register_api.urls")),
]
