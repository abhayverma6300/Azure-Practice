
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('text_extract_pii/',views.text_extract_pii),
    path('text_extract_key_phrases/', views.text_extract_key_phrases),
    path('text_recognize_linked_entities/', views.text_recognize_linked_entities),
    path('text_extract_named_entities/', views.text_extract_named_entities),
]