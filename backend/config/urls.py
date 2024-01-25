from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("vendor/", include("vendor_api.urls")),
    path("customer/", include("customer_api.urls")),
]
