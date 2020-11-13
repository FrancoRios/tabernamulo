from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homex),
    path('recetas/', views.recetax),
    path('bares/', views.barex),
    path('login/', views.logix),
]
