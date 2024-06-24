# webMaterials/urls.py
from django.urls import path
from .views import create_web_material, delete_web_material

urlpatterns = [
    path('create/', create_web_material, name='create_web_material'),
    path('delete/', delete_web_material, name='delete_web_material'),
]
