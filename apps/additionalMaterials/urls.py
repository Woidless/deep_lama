# additionalMaterials/urls.py
from django.urls import path
from .views import (
    additional_materials_create,
    additional_materials_list,
    additional_materials_detail,
    additional_materials_update,
    additional_materials_delete,
)

urlpatterns = [
    path('create/', additional_materials_create, name='additional_materials_create'),
    path('', additional_materials_list, name='additional_materials_list'),
    path('<int:pk>/', additional_materials_detail, name='additional_materials_detail'),
    path('<int:pk>/update/', additional_materials_update, name='additional_materials_update'),
    path('<int:pk>/delete/', additional_materials_delete, name='additional_materials_delete'),
]

