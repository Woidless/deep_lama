# textbooks/urls.py
from django.urls import path
from .views import create_textbook, delete_textbook

urlpatterns = [
    path('create/', create_textbook, name='create_textbook'),
    path('delete/', delete_textbook, name='delete_textbook'),
]
