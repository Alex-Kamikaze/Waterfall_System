from django.urls import path
from .views import get_sessions_info

urlpatterns = [
    path("get_sessions", get_sessions_info)
]