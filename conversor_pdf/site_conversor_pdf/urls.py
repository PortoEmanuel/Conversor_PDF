from django.urls import path
from . import views

urlpatterns = [
    path('', views.converter, name='converter'),
    path('detalhes/<int:pk>/', views.detalhes, name='detalhes'),
]