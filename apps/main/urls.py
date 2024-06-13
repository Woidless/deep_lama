# main/urls.py

from django.urls import path
from .views import view_subjects, update_subject, update_textbook, update_web_material

urlpatterns = [
    path('', view_subjects, name='view_subjects'),
    path('update_subject/<int:subject_id>/', update_subject, name='update_subject'),
    path('update_textbook/<int:textbook_id>/', update_textbook, name='update_textbook'),
    path('update_web_material/<int:web_material_id>/', update_web_material, name='update_web_material'),
]
