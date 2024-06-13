# webMaterials/forms.py
from django import forms
from .models import WebMaterials
from django.forms import modelformset_factory

WebMaterialFormSet = modelformset_factory(WebMaterials, fields=('name', 'web_link'), extra=0)
