from django.urls import path

from .views import VendorRegisterView


urlpatterns = [
    # POST localhost:8092/vendor/register/
    path(route="", view=VendorRegisterView.as_view(), name="vendor_register"),
]
