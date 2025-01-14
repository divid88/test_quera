
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Alpha Apartments API",
        default_version="v1",
        description="An Apartment Management API for Real Estate",
        contact=openapi.Contact(email="api.imperfect@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
        path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),

    path("supersecret/", admin.site.urls),

    path('api/v1/users/', include('core_apps.users.urls')),
    path('api/v1/subjects/', include('core_apps.reading.urls')),
     path('api/v1/query/', include('core_apps.quera.urls')),
]
