from django.urls import path
from .views import signin, register

urlpatterns = [
    path("login", signin, name="signin"),
    path("regitser", register, name="register"),
]
