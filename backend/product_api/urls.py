from django.urls import path

from .views import ProductView

urlpatterns = [
    # GET localhost/product/
    path(
        route="",
        view=ProductView.as_view(),
        name="products"
    )
]
