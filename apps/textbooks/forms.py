# textbooks/forms.py
from django import forms
from .models import Textbooks
from django.forms import modelformset_factory

TextbookFormSet = modelformset_factory(Textbooks, fields=('name', 'quantity'), extra=0)
