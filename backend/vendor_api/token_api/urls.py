from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import (
    MyTokenObtainPairView,
    login_view,
)


urlpatterns = [
    # POST: localhost:8000/vendor/token/
    path(
        route="token/", 
        view=MyTokenObtainPairView.as_view(), 
        name="token_obtain_pair"
    ),

    # localhost:8000/vendor/token/refresh/
    path(route="token/refresh/", 
        view=TokenRefreshView.as_view(), 
        name="token_refresh"
    ),

    # GET: localhost:8000/vendor/login/
    path(route="login/", 
        view=login_view.as_view(), 
        name="login"),
]
