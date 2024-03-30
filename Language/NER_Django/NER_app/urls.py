from django.urls import path,include
from . import views

urlpatterns = [
    
    path('recognize_custom_entities_local/',views.recognize_custom_entities_local)
    
]