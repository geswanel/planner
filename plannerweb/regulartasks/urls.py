from django.urls import path

from . import views

app_name = 'regulartasks'
urlpatterns = [
    path('', views.regular, name='regular'),
    path('add/', views.add, name='add')
]