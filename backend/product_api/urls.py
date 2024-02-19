from django.urls import path

from .views import (
    ProductCategoryListView,
    ProductSubCategoryListView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
)

urlpatterns = [
    # GET localhost/api/v1/category/
    path(
        route="category/",
        view=ProductCategoryListView.as_view(),
        name="product_category",
    ),
    # GET localhost/api/v1/subcategory/
    path(
        route="subcategory/",
        view=ProductSubCategoryListView.as_view(),
        name="product_subcategory",
    ),
    # GET localhost/api/v1/products/
    path(route="products/", view=ProductListView.as_view(), name="products"),
    # GET localhost/product/create/
    path(route="create/", view=ProductCreateView.as_view(), name="product_create"),
    # GET localhost/product/update/
    path(route="update/", view=ProductUpdateView.as_view(), name="product_update"),
]
