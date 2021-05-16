from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Anasayfa" ),
    path('acmestore/', views.acmestore, name="Acmestore")
]