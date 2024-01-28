from django.urls import path

from .views import VendorRegisterView


urlpatterns = [
    #POST localhost/vendor/register/
    path(
        route="register/",
        view=VendorRegisterView.as_view(),
        name="vendor_register"
    ),
]