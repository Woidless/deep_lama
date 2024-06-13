# main/urls.py
from django.urls import path
from .views import view_subjects, update_subject, update_all_textbooks, update_all_web_materials

urlpatterns = [
    path('', view_subjects, name='view_subjects'),
    path('update_subject/<int:subject_id>/', update_subject, name='update_subject'),
    path('update_all_textbooks/<int:subject_id>/', update_all_textbooks, name='update_all_textbooks'),
    path('update_all_web_materials/<int:subject_id>/', update_all_web_materials, name='update_all_web_materials'),
]
