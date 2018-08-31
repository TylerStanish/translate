from django.urls import path, include

from .views import practice


urlpatterns = [
    path('', practice, name='practice')
]
