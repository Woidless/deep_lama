# additionalMaterials.py
from django import forms
from .models import AdditionalMaterials

class AdditionalMaterialsForm(forms.ModelForm):
    class Meta:
        model = AdditionalMaterials
        fields = ['name', 'material_type', 'file_link', 'subject']
