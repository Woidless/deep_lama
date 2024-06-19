# additionalMaterials/urls.py
from django.urls import path
from .views import AdditionalMaterialsCreateView

urlpatterns = [
    path('create/', AdditionalMaterialsCreateView.as_view(), name='additional_materials_create'),
]
