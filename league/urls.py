from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.registration_view, name='register'),
    path('profile/', views.driver_profile_view, name='profile'),
    path('rules/', views.rules_view, name='rules'),
    path('information/', views.information_view, name='information'),
    path('info/', views.information_view, name='info'),  # New URL pattern
    path('calendar/', views.calendar_view, name='calendar'),
    path('standings/', views.standings_view, name='standings'),
]