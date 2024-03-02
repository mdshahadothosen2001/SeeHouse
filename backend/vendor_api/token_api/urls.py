from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import (
    MyTokenObtainPairView,
    login_view,
)


urlpatterns = [
    # POST: localhost:8092/vendor/token/
    path(route="", view=MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # POST: localhost:8092/vendor/token/refresh/
    path(route="refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
    # GET: localhost:8092/vendor/token/login/
    path(route="login/", view=login_view.as_view(), name="login"),
]
