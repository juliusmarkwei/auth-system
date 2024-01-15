from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    #default drf authentincation
    path("api-auth/", include("rest_framework.urls")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
   
    path("admin/", admin.site.urls),
    
    path("accounts/", include("accounts.urls", namespace="accounts")),
    
    # path("", include_docs_urls(title="Authentication System's Docs")),
]
