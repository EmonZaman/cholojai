from django.urls import path
from .views import Demo
app_name = "accounts-api-v1"

urlpatterns = [
    path('demo/',Demo.as_view(),name="Demo"),
]