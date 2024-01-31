from django.urls import path

from .views import (
    ProductView,
    ProductCategoryView,
    ProductSubCategoryView
    )

urlpatterns = [
    # GET localhost/product/
    path(
        route="",
        view=ProductView.as_view(),
        name="products"
    ),

    # GET localhost/product/category/
    path(
        route="category",
        view=ProductCategoryView.as_view(),
        name="product_category"
    ),
    
    # GET localhost/product/category/subcategory/
    path(
        route="category/subcategory/",
        view=ProductSubCategoryView.as_view(),
        name="product_subcategory"
    ),
]
