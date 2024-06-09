from django import forms
from .models import Teachers
from apps.positions.models import Positions

class TeachersForm(forms.ModelForm):
    position = forms.ModelChoiceField(queryset=Positions.objects.all(), label="Position")

    class Meta:
        model = Teachers
        fields = ['first_name', 'middle_name', 'last_name', 'position', 'photo', 'username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].label_from_instance = lambda obj: obj.name