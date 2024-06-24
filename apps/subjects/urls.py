# subjects/urls.py
from django.urls import path
from .views import subject_delete

urlpatterns = [
    path('subjects/<int:pk>/delete/', subject_delete, name='subject_delete'),
]
