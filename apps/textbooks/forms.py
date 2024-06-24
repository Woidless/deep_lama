# textbooks/forms.py
from django import forms
from .models import Textbooks
from apps.subjects.models import Subjects

class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbooks
        fields = ['name', 'quantity', 'subject']
        widgets = {
            'subject': forms.Select(choices=[(subject.id, subject.name) for subject in Subjects.objects.all()])
        }

class SelectSubjectForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subjects.objects.all(), label="Выберите предмет")

class SelectTextbookForm(forms.Form):
    textbook = forms.ChoiceField(label="Выберите книгу")

    def __init__(self, *args, **kwargs):
        textbooks = kwargs.pop('textbooks', [])
        super(SelectTextbookForm, self).__init__(*args, **kwargs)
        self.fields['textbook'].choices = [(textbook.id, textbook.name) for textbook in textbooks]
