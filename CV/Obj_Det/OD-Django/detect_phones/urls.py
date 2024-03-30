from django.urls import path
from . import views

urlpatterns = [
    path('url/',views.url),
    path('local/', views.local),
  
]