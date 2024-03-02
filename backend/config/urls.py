from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        route="admin/",
        view=admin.site.urls,
        name="admin",
    ),
    path(
        route="vendor/",
        view=include("vendor_api.urls"),
        name="vendor",
    ),
    path(
        route="customer/",
        view=include("customer_api.urls"),
        name="customer",
    ),
    path(
        route="product/",
        view=include("product_api.urls"),
        name="product",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
