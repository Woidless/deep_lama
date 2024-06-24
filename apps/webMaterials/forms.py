# webMaterials/forms.py
from django import forms
from .models import WebMaterials
from apps.subjects.models import Subjects

class WebMaterialForm(forms.ModelForm):
    class Meta:
        model = WebMaterials
        fields = ['name', 'web_link', 'subject']
        widgets = {
            'subject': forms.Select(choices=[(subject.id, subject.name) for subject in Subjects.objects.all()])
        }

class SelectSubjectForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subjects.objects.all(), label="Выберите предмет")

class SelectWebMaterialForm(forms.Form):
    web_material = forms.ChoiceField(label="Выберите веб-материал")

    def __init__(self, *args, **kwargs):
        web_materials = kwargs.pop('web_materials', [])
        super(SelectWebMaterialForm, self).__init__(*args, **kwargs)
        self.fields['web_material'].choices = [(web_material.id, f"{web_material.name} ({web_material.web_link})") for web_material in web_materials]

