from django.urls import path

from . import views

urlpatterns = [
    path("", views.regular, name="regular"),
]