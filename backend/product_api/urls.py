from django.urls import path

from .views import (
    ProductView,
    ProductCategoryView,
    ProductSubCategoryView,
    ProductCreateView,
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

    # GET localhost/product/create/
    path(
        route="create/",
        view=ProductCreateView.as_view(),
        name="product_create"
    ),
]
