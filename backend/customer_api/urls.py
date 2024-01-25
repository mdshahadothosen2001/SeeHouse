from django.urls import path, include


urlpatterns = [
    path("", include("customer_api.token_api.urls")),
]
