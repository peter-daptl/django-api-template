"""
URL configuration for {{ cookiecutter.project_slug }} project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ cookiecutter.django_version.split('.')[0] }}.{{ cookiecutter.django_version.split('.')[1] }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView # For redirecting base URL

# Import drf-spectacular views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect the project base URL ("/") to the Swagger UI at "/swagger/"
    # This aligns with the "swagger docs should be at the base url" request.
    path("", RedirectView.as_view(url='/swagger/', permanent=False)),

    # API endpoints for the 'api' app
    path('api/', include('api.urls')),

    # DRF Spectacular URLs for OpenAPI schema and UI
    path('schema/', SpectacularAPIView.as_view(), name='schema'), # OpenAPI schema in YAML/JSON
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Swagger UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # ReDoc UI
]
