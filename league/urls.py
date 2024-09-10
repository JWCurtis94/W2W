from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('register/', views.registration_view, name='register'),  # Registration page
    path('profile/', views.driver_profile_view, name='profile'),  # Driver profile page
]
