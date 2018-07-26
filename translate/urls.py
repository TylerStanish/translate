from django.urls import include, path

from .views import translation


urlpatterns = [
    path('', translation)
]
