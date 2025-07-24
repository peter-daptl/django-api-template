from django.urls import include, path

urlpatterns = [
    # Include the URLs defined in api.cars.urls.
    # The 'cars/' prefix here will make all URLs from api.cars.urls accessible under /api/cars/
    path('/', include('api.cars.urls')),
    # You would add other API endpoints here for other apps/modules, e.g.:
    # path('users/', include('api.users.urls')),
]
