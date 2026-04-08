from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('register/', views.register_farmer, name='register_farmer'),
    path('farmer/<int:pk>/', views.farmer_detail, name='farmer_detail'),
    path('farmer/<int:pk>/edit/', views.edit_farmer, name='edit_farmer'),
    path('farmer/<int:pk>/delete/', views.delete_farmer, name='delete_farmer'),
]