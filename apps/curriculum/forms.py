# curriculum/forms.py
from django import forms
from ..subjects.models import Subjects
from ..textbooks.models import Textbooks
from ..webMaterials.models import WebMaterials

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['name', 'education_form', 'study_cycle', 'number_of_students']


class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbooks
        fields = ['name', 'quantity']


class WebMaterialForm(forms.ModelForm):
    class Meta:
        model = WebMaterials
        fields = ['name', 'web_link']
