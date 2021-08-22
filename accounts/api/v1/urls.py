from django.urls import path
from .views import RegisterAPI
from django.urls import path

app_name = "accounts-api-v1"

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
]


