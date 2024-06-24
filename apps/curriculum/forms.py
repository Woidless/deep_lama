# curriculum/forms.py
from django import forms
from ..subjects.models import Subjects
from ..textbooks.models import Textbooks
from ..webMaterials.models import WebMaterials
from django.forms import modelformset_factory

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['name', 'education_form', 'study_cycle', 'number_of_students']

TextbookFormSet = modelformset_factory(Textbooks, fields=('name', 'quantity'), extra=0)

WebMaterialFormSet = modelformset_factory(WebMaterials, fields=('name', 'web_link'), extra=0)