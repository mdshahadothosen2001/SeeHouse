from django.urls import path, include


urlpatterns = [
    path("", include("vendor_api.token_api.urls")),
]
