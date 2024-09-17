from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Todo list Api",
        default_version="v1",
        description="API documentation description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/registration/account-confirm-email/<str:key>/", confirm_email),
    path("accounts/registration/", include("dj_rest_auth.registration.urls")),
    path("todos/", include("tasks.urls", namespace="tasks")),
]
