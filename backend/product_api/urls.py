from django.urls import path

from .views import (
    ProductCategoryListView,
    ProductSubCategoryListView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
)

urlpatterns = [
    # GET localhost:8092/product/
    path(route="", view=ProductListView.as_view(), name="products"),
    # GET localhost:8092/product/category/
    path(
        route="category/",
        view=ProductCategoryListView.as_view(),
        name="product_category",
    ),
    # GET localhost:8092/product/subcategory/
    path(
        route="subcategory/",
        view=ProductSubCategoryListView.as_view(),
        name="product_subcategory",
    ),
    # POST localhost:8092/product/create/
    path(route="create/", view=ProductCreateView.as_view(), name="product_create"),
    # PATCH localhost:8092/product/update/
    path(route="update/", view=ProductUpdateView.as_view(), name="product_update"),
]
