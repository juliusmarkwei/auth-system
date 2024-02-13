from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny


admin.site.site_herder = "Auth System Admin Panel"
admin.site.index_title = "Admin"

schema_info = {
    
}

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")), #default drf authentincation
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("docs/", include_docs_urls(
        title = "Authentication System's Docs",
        description = """
                        A simple authentication system build be extending the functionalities\
                            of the Djoser library. This project utilizes allthe nasic CRUD \
                                operation.
                      """,
        permission_classes = [AllowAny],
    )),
]
