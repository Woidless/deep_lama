from django import forms


class SubjectDetailsForm(forms.Form):
    study_cycle = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=255)
    education_form = forms.CharField(max_length=255)
    number_of_students = forms.IntegerField()