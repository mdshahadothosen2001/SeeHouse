from django.urls import path, include

from .views import CustomerRegisterView


urlpatterns = [
    # POST localhost/customer/register/
    path(
        route="register/",
        view=CustomerRegisterView.as_view(),
        name="customer_register",
    ),
    path("", include("customer_api.token_api.urls")),
]
