from django.urls import path,include
from . import views

urlpatterns = [
     path('clu/',views.hit_clu)
     
]