from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Почетна страница
    path('ads/', views.ad_list, name='ad_list'),  # Листа на огласи
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),  # Детали за оглас
    path('create/', views.ad_create, name='ad_create'),  # Додавање оглас
]